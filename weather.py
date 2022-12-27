#currently weather remains experimental, but this comment will be updated accordingly when weather enters into the alpha stage

####ATTENTION Weather is now in alpha*******************

####ATTENTION Weather has entered beta phase

############We are pleased to release weather module v1







#import requests

#all of the below was from google, it doesnt really work, so i left it here to refer to, its not even that helpful
"""
city_name = "Vancouver"
api_key = "a87d5e24ba113d24c19a7d97ed3213b7"#typing an api key directly into a public replit is a bad idea for so many reasons, yet here I am doing it anyway. 

def get_weather(api_key, city, tempstate):

		
	
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    temp = response['main']['temp']
    #temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F
		
		
    feels_like = response['main']['feels_like']
    #feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F
		#for temp in celcius all we need to do is subtract 273.15 
    humidity = response['main']['humidity']
		
	
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }


weather = get_weather(api_key, city_name, f)

#root = Tk()
#root.geometry("600x300")
#root.title(f'{city_name} Weather')

#def display_city_name(city):
#    city_label = Label(root, text=f"{city_name}")
    
#    city_label.pack(side='top')

#def display_stats(weather):
#    temp = Label(root, text=f"Temperature: {weather['temp']} K")
#    feels_like = Label(root, text=f"Feels Like: {weather['feels_like']}K")
#    humidity = Label(root, text=f"Humidity: {weather['humidity']} %")

  
#    temp.pack(side='top')
#    feels_like.pack(side='top')
#    humidity.pack(side='top')


#display_city_name(city_name)
#display_stats(weather)

#mainloop()

"""


#real weather function for final use, now in beta stage

def weather(tempstate="C", city="Nanaimo"):
	import requests
	"""The weather function tells the weather, what else were you expecting...

	This uses the openweathermap api (free version, so if it stops working that means openweather map went bust)
	
	OPTIONALLY, YOU CAN PASS IT A TEMPSTATE OF C AND A DIFFERENT CITY, OTHERWISE THE DEFAULTS OF CELSIUS AND 
    NANAIMO WILL BE USED"""

	print("Weather Function called, beginning weather retrival sequence")#######


	if tempstate=="C":
		print("Selected Temperature state is default of Celsius")
		
	elif tempstate=="K":
		print("This user is chose to use Kelvin, what a Chad")
		#too bad he can't spell
	else: print("Invalid temperature unit passed, and no, Farenheit is not a valid temperature unit. For users that disagree, we recommend the guilotine. ")

	api_key = "a87d5e24ba113d24c19a7d97ed3213b7"#typing an api key directly into a public replit is a bad idea for 	so many reasons, yet here I am doing it anyway. 
	#												
	#										 ^
	#					 API KEY RIGHT HERE / \
	#										 |
	#										 |      USE IT RESPONSIBLY
	#										 |

	url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"#here is the url that we can ping a maximum of once every hour I believe, if we pay for openweathermap it would be more than that. 

	response = requests.get(url).json()#THIS LINE IS ENTIRELY MAGIC, NOBODY REALLY KNOWS WHAT IT DOES, BUT STUFF DONT WORK IF WE REMOVE IT
	
	# the city was not found
	if response["cod"] == 404:
		return None
	
	temp = response["main"]['temp']#obtain the current temperature from openweathermap
	if tempstate=="C":
		temp-=273.15
	elif tempstate == "R":
		temp -= 273.15
		temp *= 0.8
		
	feels_like = response['main']['feels_like']#obtain current "feels like" temperature from openweathermap
	if tempstate=="C":
		feels_like-=273.15
	elif tempstate == "R":
		feels_like -= 273.15
		feels_like *= 0.8
		
	humidity = response['main']['humidity']#obtain current humidity from openweathermap

	description = response['weather'][0]['description']#Obtain current weather description from openweathermap, this one was a pain to actually get working, turns out I needed a new api key. 

	icon = response['weather'][0]['icon']#this started magically working at the same time as description, so i havent messed with it since then. 

	if tempstate == "C":
		tempstate = "°C"
	if tempstate == "R":
		tempstate = "°Ré"

#here we are returning a dictionary with each value as its own key.
	return {
		'temp' : temp, #this one is just temperature
		'feels_like' : feels_like, #the feels like temperature
		'humidity' : humidity, #humidity, again self explanatory
		'description' : description, #this one is for the description of the weather, examples include sunny, light rain, cloudy, mist, etc.
		'icon': icon,#icon code provided to set the correct icon, icons are prenamed and provided by openweathermap.
		"tempstate" : tempstate#Temp state, relevant temperature states such as Kelvin and Celsius are available, for users that prefer farenheit, there is always the huitine
	}



#For the record no body in this group actually speaks chinese so I am not sure how or why this is here. 
#def 哔哔生菜():
#	raise 哔哔生菜




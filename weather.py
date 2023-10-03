import requests

def get_Weather_Status() :

    api_key = "your API KEY here"
    
    city = input("Enter city name : \n")

    print("\n")
    # Url used for sending get request
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    # Using the get method from the requests module, it creates a get request to get the data for the given city
    response = requests.get(url)
    
    # It checks if the get request was successfull if yes then the data sent back is converted to json and printed
    if response.status_code == 200 :

        data = response.json()
        
        city = data["location"]["name"]

        region = data["location"]["region"]

        country = data["location"]["country"]

        temp_c = data["current"]["temp_c"]

        temp_f = data["current"]["temp_f"]

        Weather_condition = data["current"]["condition"]["text"]

        print(f"City : {city}\nRegion : {region}\nCountry : {country}\nTemperature in celsius : {temp_c}C\nTemperature in fahrenheit : {temp_f}F\nWeather Condition : {Weather_condition}\n")


    else :

        print("Invalid city name.\n")    


get_Weather_Status()        

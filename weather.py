import requests

def get_Weather_Status() :
    
    api_key = "6f76b51e06c848808c5113655230110"
    
    city = input("Enter city name : \n")

    print("\n")

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)

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
import json

import requests


def get_current_weather(url:str, key: str, city: str = "Bucharest"):
    try:
        response = requests.get(url + city, headers={"key": key})
        if response.status_code == 200:
            weather_dict = json.loads(response.text)
            if weather_dict.get('error'):
                raise Exception("Orasul nu exista in baza noastra de date")
            return weather_dict
        else:
            raise Exception(f"Something wrong with the api \n"
                            f"Code: {response.status_code}\n"
                            f"Message: {response.text}")
    except Exception as e:
        print(e)


def city_info(url:str, key: str, city: str = "Bucharest"):
    try:
        response = requests.get(url + city, headers={"key": key})
        if response.status_code == 200:
            weather_dict = json.loads(response.text)
            curr_temp = weather_dict['current']['temp_c']
            curr_status = weather_dict['current']['condition']['text']
            curr_hour = weather_dict['location']['localtime']
            return curr_temp, curr_status, curr_hour
    except Exception as e:
        print(e)

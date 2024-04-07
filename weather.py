import json

import emoji
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
            # return curr_temp, curr_status, curr_hour
    except Exception as e:
        print(e)
    else:
        if curr_status == "Clear":
            return emoji.emojize(f" In the  city {city}, at local :four_o’clock: {curr_hour} is currently :sun:, with {curr_temp}:thermometer:")
        elif curr_status == "Partly cloudy":
            return  emoji.emojize(f" In the city {city}, at local :four_o’clock: {curr_hour} is currently :sun_behind_cloud:, with {curr_temp}:thermometer:")
        elif curr_status == "Rain":
            return emoji.emojize(
                f" In the city {city}, at local :four_o’clock: {curr_hour} is currently :cloud_with_rain:, with {curr_temp}:thermometer:")

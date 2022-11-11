import json


def parse_weather_data(data):
    data = json.loads(data)
    print(data)
    return data

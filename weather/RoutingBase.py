import requests

from parser import WeatherParser

_upstream_url = "https://wttr.in/{location}?format=j1"


def fetch_weather_from_upstream(location):
    url = _upstream_url.format(location=location)
    print(f"Hitting url => {url}")
    data = requests.get(url).content

    data = WeatherParser.parse_weather_data(data)
    return data


if __name__ == '__main__':
    fetch_weather_from_upstream("Windsor")

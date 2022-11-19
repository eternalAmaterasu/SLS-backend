import requests

from parser.WeatherParser import DataParser


class RoutingBase:

    def __init__(self):
        self.upstream_url = "https://wttr.in/{location}?format=j1"
        self.server_to_upstream_timeout = 60

    def fetch_weather_from_upstream(self, location):
        url = self.upstream_url.format(location=location)
        print(f"Hitting url => {url}")
        data, parsed_data = "", ""
        try:
            response = requests.get(url, timeout=self.server_to_upstream_timeout)
            data = response.content
        except Exception as e:
            print(f"Exception whilst upstream procedure: {e}")

        if not data: return parsed_data
        print("Upstream hit successful, going for data parsing now!")
        weather_parser = DataParser()
        parsed_data = weather_parser.parse_weather_data(data)
        if parsed_data: print("Data parsing done!")
        return parsed_data

import unittest

import requests_mock

from weather.RoutingBase import RoutingBase


class RoutingBaseTest(unittest.TestCase):

    def test_routing_base(self):
        routing_base = RoutingBase()
        routing_base.server_to_upstream_timeout = 10

        self.assertEqual(10, routing_base.server_to_upstream_timeout)
        self.assertEqual("https://wttr.in/{location}?format=j1", routing_base.upstream_url)

    @requests_mock.mock()
    def test_routing_base_fetch_weather_from_upstream(self, req_mock):
        routing_base = RoutingBase()
        with open('weather/windsor.json', 'r') as file: test_response = file.read()

        req_mock.get('https://wttr.in/windsor?format=j1', text=test_response)
        weather_data = routing_base.fetch_weather_from_upstream('windsor')
        expected_result = """{"data": {"date": "2022-11-12", "feels_like": "-3", "temperature": "1", "description": "Overcast", "cloud_cover": "100", "humidity": "85", "precipitation_mm": "0.0", "visibility_km": "16", "avg_temperature": "3", "max_temperature": "4", "min_temperature": "1", "total_snow_cm": "2.9", "total_sun_hour": "8.3"}}"""
        self.assertEqual(expected_result, weather_data)


if __name__ == '__main__':
    unittest.main()

import json


class DataParser:
    class Sampler:
        def __init__(self):
            self.data = {}

        def set_key_val(self, key, val):
            self.data[key] = val

        def __repr__(self):
            return json.dumps(self.__dict__)

    def parse_weather_data(self, data):
        data = json.loads(data)
        # print(data)

        # Initiate data parsing and extraction of info required
        sample = self.Sampler()
        date_time = data['current_condition'][0]['localObsDateTime']
        sample.set_key_val("date", date_time[0: date_time.index(' ')])
        sample.set_key_val("feels_like", data['current_condition'][0]['FeelsLikeC'])
        sample.set_key_val("temperature", data['current_condition'][0]['temp_C'])
        sample.set_key_val("description", data['current_condition'][0]['weatherDesc'][0]['value'])
        sample.set_key_val("cloud_cover", data['current_condition'][0]['cloudcover'])
        sample.set_key_val("humidity", data['current_condition'][0]['humidity'])
        sample.set_key_val("precipitation_mm", data['current_condition'][0]['precipMM'])
        sample.set_key_val("visibility_km", data['current_condition'][0]['visibility'])

        conditions = data['weather'][0]
        sample.set_key_val("avg_temperature", conditions['avgtempC'])
        sample.set_key_val("max_temperature", conditions['maxtempC'])
        sample.set_key_val("min_temperature", conditions['mintempC'])
        sample.set_key_val("total_snow_cm", conditions['totalSnow_cm'])
        sample.set_key_val("total_sun_hour", conditions['sunHour'])

        return sample.__repr__()

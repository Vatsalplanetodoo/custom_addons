
from odoo import api, models, fields
import requests
import json

class Weather1Info(models.Model):
    _name = 'weather1.info'
    _rec_name = 'city_name'

    city_name = fields.Char('City Name')
    state_code = fields.Integer('State Code',readonly=True)
    wind_direction = fields.Integer('Wind Direction',readonly=True)
    temperature = fields.Integer('Temperature',readonly=True)
    clouds = fields.Integer('Clouds',readonly=True)
    description = fields.Char('Description',readonly=True)

    def weather_io(self):
        key = '6846bd4e19c54123b855a98d89190f1c'
        url = f'https://api.weatherbit.io/v2.0/current?&city={self.city_name}&key=' + key
        response = requests.get(url)
        dict_res = json.loads(response.text)
        attendances = self.env['weather1.info'].search([
            ('id', '=', self.id),
        ])
        weather_data = attendances.update({
            'city_name': self.city_name,
            'state_code': dict_res["data"][0]["state_code"],
            'wind_direction': dict_res["data"][0]["wind_dir"],
            'temperature': dict_res["data"][0]["temp"],
            'clouds': dict_res["data"][0]["clouds"],
            'description': dict_res["data"][0]["weather"]["description"],})

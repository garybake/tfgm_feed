import requests


class Tfgm:

    def __init__(self, subs_key):
        self.subs_key = subs_key
        self.url = "https://api.tfgm.com/odata/Metrolinks"
        self.headers = {'Ocp-Apim-Subscription-Key': self.subs_key}
        self.params = {}

    def get_data(self, row_count=10):
        self.params["$top"] = row_count
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            return response.json()

        except Exception as e:
            print(f"Error getting data {e}")

    def get_departures(self):
        data = self.get_data()
        return data['value']

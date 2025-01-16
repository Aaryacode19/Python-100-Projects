import requests
from twilio.rest import Client

OWN_ENDPOINT = "ur own_endpoint"
api_key = "ur api key"
account_sid = "ur acc_sid"
auth_token = "ur auth token"



weather_params = {
    "lat": #ur latitide,
    "lon": #ur longitude,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today!! Carry Umbrella With Ya!!",
        from_='twilio no (u will get it once u login)',
        to='ur number'
    )
    print(message.status)


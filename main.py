import requests
from SendEmail import send_email

api_key = "" #replace with your own api key from https://openweathermap.org/api
latitude = 42.314938
longitude = -83.036362

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
status = response.status_code
data = response.json()

print(f"status: {status}")

hourly_data_list = []

will_rain:bool = False
snow:bool = False
for hour_data in data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    description = hour_data["weather"][0]["description"]
    dt_text = hour_data["dt_txt"]

    if condition_code<700:
        if condition_code>=600:
            snow = True
        else: will_rain=True

    hourly_data_list.append(
        {
            "dt": dt_text,
            "description": description,
            "code": condition_code
        }
    )
for x in hourly_data_list:
    print(x)
print('\n')


# Sending email notification now. 
recipient_email = "any email" #receipient email address
subject = "Weather notification!"


if will_rain:
    body = f"""Hello,

    It might rain today. You may want to bring an umbrella with you.

    Best regards,
    Your Name
    """
    send_email(recipient_email, subject, body)
    print("It may rain, bring an umbrella.")
if snow:
    body = f"""Hello,

        It might rain today. You may want to bring an umbrella with you.

        Best regards,
        Your Name
        """
    send_email(recipient_email, subject, body)
    print("It might snow today")




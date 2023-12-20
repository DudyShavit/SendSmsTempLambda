try:
    import json
    import os
    import shutil
    import uuid
    import datetime
    import requests

    print("All Modules are ok ...")

except Exception as e:
    print("Error in Imports ")


def send_sms(message):
    url = "https://api.sms4free.co.il/ApiSMS/v2/SendSMS"
    # Declare Some Variables
    key = "SMS_KEY"
    user = "USER"
    _pass = "PASSWORD"
    sender = "SENDER_NUM"
    recipient = "RECIPIENT_NUM"

    # Object that have the data we want to POST
    data = {}
    data["key"] = key
    data["user"] = user
    data["pass"] = _pass
    data["sender"] = sender
    data["recipient"] = recipient
    data["msg"] = message
    # Post Data
    response = requests.post(url, json=data, verify=False)
    print(response)  # Should GET Status 200 (SUCCESS)


def send_email(message):
    # Send message to SNS
    MY_SNS_TOPIC_ARN = 'ARN_ID'
    # sns_client = boto3.client('sns')
    # sns_client.publish(
    #     TopicArn=MY_SNS_TOPIC_ARN,
    # Subject='TOPIC_SUBJECT',
    # Message=message
    # )


def get_weather(api_key, city):
    base_url = '    /data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        print(f"Error: {response.status_code}")
        return None


def lambda_handler(event, context):
    api_key = 'MY_API_KEY'
    city = 'Tel-Aviv'

    temperature = get_weather(api_key, city)

    send_sms(temperature)

    return True

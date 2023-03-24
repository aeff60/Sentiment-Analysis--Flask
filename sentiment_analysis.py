import urllib.request
import json
import ssl
from config import API_KEY, MODEL_URL
import os

def allow_self_signed_https(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def get_sentiment(text):
    allow_self_signed_https(True)

    data = {"inputs": text}
    body = str.encode(json.dumps(data))

    headers = {
        'Content-Type': 'application/json',
        'Authorization': ('Bearer ' + API_KEY),
        'azureml-model-deployment': 'main'
    }

    req = urllib.request.Request(MODEL_URL, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        sentiment_output = json.loads(result)

        sentiment = sentiment_output[0]['label']
        return sentiment

    except urllib.error.HTTPError as error:
        return {"error": str(error.code)}

# Python Beast Series
# Mastering Mocking in Python
import requests

def fetch_data (url):
    try:
        response = requests.get (url, timeout=5)
        return response.json()
    except requests.Timeout:
        return {"error": "---> Request timed out"}
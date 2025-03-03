# Python Beast Series
# Mastering Mocking in Python

import requests

def get_user_data (User_id):

    response = requests.get (f"https://api.example.com/users/{user_id}")

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def process_user_data(user_id):
    data = get_user_data (user_id)

    if data:
        return f" ---> Usuario {data['name']} tem {data['age']} anos de idade"
    else:
        return " ***> Usuario nao encontrado"
import requests
import json

question_data = []
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}
response = requests.get('https://opentdb.com/api.php', params=parameters).json()
question_list = response['results']

for question in question_list:
    question_data.append(question)

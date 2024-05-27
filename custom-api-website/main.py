from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime

app = Flask(__name__)

def fetch_random_user(gender):
    response = requests.get(f"https://randomuser.me/api?gender={gender}")
    if response.status_code == 200:
        data = response.json()
        raw_date = data['results'][0]['dob']['date']
        formatted_date = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
        user_info = {
            'gender': data['results'][0]['gender'],
            'fname': data['results'][0]['name']['first'],
            'lname': data['results'][0]['name']['last'],
            'city': data['results'][0]['location']['city'],
            'state': data['results'][0]['location']['state'],
            'country': data['results'][0]['location']['country'],
            'email': data['results'][0]['email'],
            'username': data['results'][0]['login']['username'],
            'password': data['results'][0]['login']['password'],
            'date': formatted_date,
            'age': data['results'][0]['dob']['age'],
            'phone': data['results'][0]['phone']
        }
        return user_info
    else:
        return None

@app.route('/')
def index():
    gender = request.args.get('gender', 'random')
    user_info = fetch_random_user(gender)
    if user_info:
        return render_template('index.html', **user_info)
    else:
        return jsonify({'error': 'Failed to fetch user data'})



if __name__ == "__main__":
    app.run(debug=True)
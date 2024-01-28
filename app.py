from flask import Flask, jsonify, request
import pytz
import requests
import datetime

app = Flask(__name__)
session_url = "the url from the intersact.sh session"


@app.route('/api/getURL', methods=['GET'])
def get_url():
    full_url = f"https://{session_url}"
    return jsonify({'url': full_url})

@app.route('/api/getInteractions', methods=['GET'])
def get_interactions():
    full_url = f"https://{session_url}"
    start_timestamp = request.args.get('start', None)
    end_timestamp = request.args.get('end', None)
    # Assuming 'interactions-endpoint' is a valid endpoint for interact.sh
    response = requests.get(f"{full_url}/interactions-endpoint", params={
        'start': start_timestamp,
        'end': end_timestamp
    })
    return response.text
    

if __name__ == '__main__':
    app.run(debug=True)

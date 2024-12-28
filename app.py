from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/zoom-webhook', methods=['POST'])
def zoom_webhook():
    event_data = request.json
    
    # Log or process the event data from Zoom (You can print to debug)
    print(event_data)
    
    # Respond to Zoom's challenge for webhook verification
    if event_data.get('event') == 'endpoint.url_validation':
        return jsonify({
            'url_validation_token': event_data.get('event'),
            'status': 'success'
        })

    # Process other events here (e.g., meeting started, user joined)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)

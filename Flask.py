from flask import Flask, jsonify

app = Flask(__name__)

# Simulated intersection-based tracking
current_location = {'x': 175.2, 'y': 145.0}  # Example initial intersection

@app.route('/location', methods=['GET'])
def get_location():
    # Return current intersection coordinates
    return jsonify({'x': current_location['x'], 'y': current_location['y']})

@app.route('/update_location', methods=['POST'])
def update_location():
    global current_location
    data = request.get_json()
    current_location = {'x': data['x'], 'y': data['y']}
    return jsonify({'status': 'updated', 'new_location': current_location})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

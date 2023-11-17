from flask import Flask, jsonify, render_template, request
import pyrebase

app = Flask(__name__)

# Configure Firebase
config = {
    'apiKey': "AIzaSyCsXPeq9GgTyAqXEFg-rRKEQqJ9B2zB5fs",
    'authDomain': "dyte-task.firebaseapp.com",
    'databaseURL': "https://dyte-task-default-rtdb.firebaseio.com",
    'projectId': "dyte-task",
    'storageBucket': "dyte-task.appspot.com",
    'messagingSenderId': "466846795130",
    'appId': "1:466846795130:web:fa8ffa0ef683eaf8b6c2c3",
    'measurementId': "G-SPKEPGJCZ4"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Route to get error logs
@app.route('/get_logs', methods=['POST', 'GET'])
def get_error_logs():
    # Query the data
    if request.method == 'POST':
        # data = request.get_json()
        
        val = request.form['value']
        option = request.form['option']
        print(val)
        print(option)
        
        if option == "parentResourceId":
            data = db.child("logs").order_by_child("metadata/"+option).equal_to(val).get()
        else:
            data = db.child("logs").order_by_child(option).equal_to(val).get()
            print(data.val())

        # Convert the data to a list
        error_logs = [log.val() for log in data.each()]
        print(error_logs)

        # return jsonify(error_logs)
        return render_template('log_query.html', result = "ok", data = error_logs)
    return render_template('log_query.html')

@app.route('/insert_logs', methods = ['POST', 'GET'])
def insert_logs():
    if request.method == 'POST':
        data = request.get_json()
        
        # Check if required keys are present
        required_keys = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'metadata']
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Key '{key}' is missing in the JSON data")

        level = data['level']
        message = data['message']
        resourceId = data['resourceId']
        timestamp = data['timestamp']
        traceId = data['traceId']
        spanId = data['spanId']
        commit = data['commit']
        metadata = data['metadata']

        # Access metadata values
        parentResourceId = metadata['parentResourceId']
        
        data_db  = {
            
            "level": level,
            "message": message,
            "resourceId": resourceId,
            "timestamp": timestamp,
            "traceId": traceId,
            "spanId": spanId,
            "commit": commit
            }
        # Add metadata to the pushed data
        meta_data = {
            "parentResourceId": parentResourceId
        }

        # Combine the data and metadata
        data_db["metadata"] = meta_data
                
        # Push data to Firebase
        db.child('logs').push(data_db)
        
        return render_template('insert_log.html', result = "ok")
    
    return render_template('insert_log.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/time')
def time():
    timezone = pytz.timezone('Europe/Amsterdam') # Change timezone as needed
    now = datetime.now(timezone)
    time_string = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    return jsonify(time=time_string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

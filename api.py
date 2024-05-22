from flask import *
import random
import json, time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def health_data():
    heart_rate = random.randint(40,120)
    spo2_level = random.randint(60,100)
    stress_level = random.randint(60,85)
    data_set = {
        'Heart Rate': heart_rate,
        'SPO2': spo2_level,
        'Stress Level': stress_level
    }
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port = 7776)
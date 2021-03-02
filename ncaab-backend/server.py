from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin

import os
import json
import time
import calculator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

times = {}

PASSWORD = "carsontakes"

with open('last_updated.json') as f:
  times = json.load(f)

@app.route("/calculate")
@cross_origin()
def calculate():
    away_team = request.args.get("awayTeam")
    home_team = request.args.get("homeTeam")
    
    away_predicted_score, home_predicted_score, away_win_percentage_game, home_win_percentage_game, total_score, home_spread = calculator.calculate(away_team, home_team)

    response = {"away_predicted_score": away_predicted_score,
    "home_predicted_score": home_predicted_score,
    "away_win_percentage_game": away_win_percentage_game,
    "home_win_percentage_game": home_win_percentage_game,
    "total_score": total_score,
    "home_spread": home_spread}

    return jsonify(response)

@app.route("/settings", methods=['GET', 'POST'])
@cross_origin()
def settings():
    if(request.method == 'GET'):
        a = calculator.getM()
        res = {"hcao": a[0],"hcad": a[1], **times}
        return jsonify(res), 200
    else:
        if(request.form.get("password") != PASSWORD):
            res = {"msg": "Incorrect password!"}
            return jsonify(res), 403
        else:
            
            if('uploadedFile' in request.files):
                request.files['uploadedFile'].save(os.path.join("C:\\Users\\james\\OneDrive\\Projects\\ncaab\\ncaab-backend", "kenpom.csv"))
                calculator.updateCache()
                res = {"msg": "Successfully updated CSV!"}
                times["last_updated_csv"] = time.asctime()

            
            hcad = 2 - float(request.form.get("hcam"))
            hcao = float(request.form.get("hcam"))
            calculator.setM(hcao, hcad)
            times["last_updated_values"] = time.asctime()
            
            with open('last_updated.json', 'w') as outfile:
                json.dump(times, outfile)
            
            a = calculator.getM()
            res = {"hcao": hcao,"hcad": hcad,**times}
            return jsonify(res), 200

            
            

app.run(host='0.0.0.0')

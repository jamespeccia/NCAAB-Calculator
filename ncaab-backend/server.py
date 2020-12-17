
from calculator import calculate as calc
import json

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/calculate")
@cross_origin()
def calculate():
    away_team = request.args.get("awayTeam")
    home_team = request.args.get("homeTeam")
    
    away_predicted_score, home_predicted_score, away_win_percentage_game, home_win_percentage_game, total_score, home_spread = calc(away_team, home_team)

    response = {"away_predicted_score": away_predicted_score,
    "home_predicted_score": home_predicted_score,
    "away_win_percentage_game": away_win_percentage_game,
    "home_win_percentage_game": home_win_percentage_game,
    "total_score": total_score,
    "home_spread": home_spread}

    return jsonify(response)

app.run()

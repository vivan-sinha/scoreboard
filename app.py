# ngrok http 8080

from flask import Flask, flash, request, redirect, url_for, render_template, Response
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
app.secret_key = "super secret key"
socketio = SocketIO(app)

home_team = 'VIVAN/ALEX'
away_team = 'AWAY'

@app.route('/', methods=['GET'])
def home():
    return view_scoreboard()

@app.route('/edit', methods=['GET'])
def edit_scoreboard():
    return render_template('edit.html', home=home_team, away=away_team)

@app.route('/view', methods=['GET', 'POST'])
def view_scoreboard():
    return render_template('scoreboard.html', home=home_team, away=away_team)

@socketio.on('update')
def updateBoard(data):
    # homePoints, awayPoints, homeSets, awaySets, awayServe
    print(data)
    socketio.emit('updateBoard', data=(data['awayServe'], data['homeSets'], data['homePoints'], data['awaySets'], data['awayPoints']))
    return Response(status=204)

if __name__ == '__main__':
    socketio.run(app=app, port=8080)
    
    # edit at {url}/edit")
    # to host, run app.py and run command in terminal: ngrok http 8080

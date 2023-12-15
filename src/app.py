from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOPositions import DAOPositions
from dao.DAOTeams import DAOTeams
from dao.DAOPlayers import DAOPlayers

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
dbPositions = DAOPositions()
dbTeams = DAOTeams()
dbPlayers = DAOPlayers()

@app.route('/')
def inicio():
    return render_template('index.html')

#clasificacion:
@app.route('/positions/')
def positions():
    data = dbPositions.read(None)
    return render_template('positions/index.html', data = data)

@app.route('/positions/updatePage')
def positionsPageUpdate():
    data = dbPositions.read(None)
    return render_template('positions/updatePage.html', data = data)

@app.route('/positions/update/update/<string:idEquipo>/')
def positionsUpdate(idEquipo):
    data = dbPositions.read(idEquipo);

    if len(data) == 0:
        return redirect(url_for('positionsPageUpdate'))
    else:
        session['update'] = idEquipo
        return render_template('positions/update/update.html', data = data)

@app.route('/positions/update/updatePositions', methods = ['POST'])
def updatePositions():
    if request.method == 'POST' and request.form['update']:

        if dbPositions.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')
        
        session.pop('update', None)

        return redirect(url_for('positionsPageUpdate'))
    else:
        return redirect(url_for('positionsPageUpdate'))

#equipos:
@app.route('/teams/')
def teams():
    data = dbTeams.read(None)
    return render_template('/teams/index.html', data = data)

#jugadores:
@app.route('/teams/players/<string:idEquipo>/')
def players(idEquipo):
    data = dbPlayers.read(idEquipo)
    return render_template('/players/index.html', data = data)

@app.route('/players/update')
def playersPage():
    data = dbPlayers.readUpdate()
    return render_template('/players/index.html', data = data)

@app.route('/players/add/')
def playersAdd():
    return render_template('/players/add.html')

@app.route('/players/addplayer/', methods = ['POST', 'GET'])
def addPlayers():
    if request.method == 'POST' and request.form['save']:
        if dbPlayers.insert(request.form):
            flash("Nuevo jugador creado")
        else:
            flash("ERROR al crear jugador")

        return redirect(url_for('teams'))
    else:
        return redirect(url_for('teams'))

@app.route('/players/update/<int:id>/')
def playersUpdate(id):
    data = dbPlayers.readUpdate(id);

    if len(data) == 0:
        return redirect(url_for('playersPage'))
    else:
        session['update'] = id
        return render_template('/players/update.html', data = data)
    
@app.route('/players/updatePlayers', methods = ['POST'])
def updatePlayers():
    if request.method == 'POST' and request.form['update']:

        if dbPlayers.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR al actualizar')
        
        session.pop('update', None)

        return redirect(url_for('teams'))
    else:
        return redirect(url_for('teams'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)

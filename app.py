from flask import *
import mlab
from mongoengine import *
app = Flask(__name__)
app.secret_key = 'a-super-secret-key'
mlab.connect()
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        if username == 'paty0504' and password == 'paty0504':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)

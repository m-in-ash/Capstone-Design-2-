from flask import Flask, render_template
from map import make_map

app = Flask(__name__,  static_folder = "/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/contactweb')
def contactweb():
    return render_template('contactweb.html')

@app.route('/contactarea')
def contactarea():
    return render_template('contactarea.html')

@app.route('/map')
def seoul_map():
    return make_map().get_root().render()

@app.route('/map/<region>')
def gu_map(region):
    return make_map(region).get_root().render()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import logging
from client.cls_client import Endpoints

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def smoke_test():
    smoke = {'hello': 'world'}
    return {'results': smoke}

@app.route('/pop')
def get_all():
    return {"results": client_obj.get_all()}

@app.route('/pop/color/<pop_color>')
def get_by_color(pop_color):    
    return {"results": client_obj.get_by_color(pop_color)}

@app.route('/pop/name/<pop_name>')
def get_by_name(pop_name):
    return {"results": client_obj.get_by_name(pop_name)}

@app.route('/pop/name/<pop_name>/color/<pop_color>')
def insert(pop_name, pop_color):
    return {"results": client_obj.insert(pop_name, pop_color)}

if __name__ == "__main__":
    client_obj = Endpoints()
    app.run(host ='0.0.0.0', port = 5000, debug = True)

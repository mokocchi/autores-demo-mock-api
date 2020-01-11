from flask import Flask, json, Response
from flask_cors import CORS, cross_origin
import os

f = open("respuestas/actividades_15")
actividad_15 = f.read()
f = open("respuestas/actividades_15_tareas")
actividad_15_tareas = f.read()

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'


@api.route('/api/v1.0/actividades/<int:id>', methods=['GET'])
@cross_origin()
def get_actividad(id):
    item = id
    parsed = json.loads(actividad_15)
    return Response(json.dumps(parsed, indent=4), mimetype='application/json')


@api.route('/api/v1.0/actividades/<int:id>/tareas', methods=['GET'])
@cross_origin()
def get_actividad_tareas(id):
    item = id
    parsed = json.loads(actividad_15_tareas)
    return Response(json.dumps(parsed, indent=4), mimetype='application/json')


@api.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    api.run(threaded=True, host='0.0.0.0',
            port=int(os.environ.get("PORT", 5000)))

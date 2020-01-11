from flask import Flask, json, Response
import os

f = open("respuestas/actividades_15")
actividad_15 = f.read()

api = Flask(__name__)


@api.route('/api/v1.0/actividades/<int:id>', methods=['GET'])
def get_actividad(id):
    item = id
    parsed = json.loads(actividad_15)
    return Response(json.dumps(parsed, indent=4), mimetype='application/json')


@api.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    api.run(threaded=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

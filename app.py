from flask import Flask, json, Response
import sys

f = open("respuestas/actividades_15")
actividad_15 = f.read()

api = Flask(__name__)


@api.route('/api/v1.0/actividades/<port = sys.argv[1]id>', methods=['GET'])
def get_actividad(id):
    item = id
    parsed = json.loads(actividad_15)
    return Response(json.dumps(parsed, indent=4), mimetype='application/json')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        port = sys.argv[1]
        api.run(threaded=True, port=port)

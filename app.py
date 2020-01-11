from flask import Flask, json, Response
from flask_cors import CORS, cross_origin
import os

DIR = "respuestas"
API_BASE_URI = "/api/v1.0"

f = open(DIR + "/actividades_15.json")
actividades_15 = f.read()
f = open(DIR + "/actividades_15_tareas.json")
actividades_15_tareas = f.read()
f = open(DIR + "/dominios.json")
dominios = f.read()
f = open(DIR + "/idiomas.json")
idiomas = f.read()
f = open(DIR + "/tipos-tarea.json")
tipos_tarea = f.read()
f = open(DIR + "/tipos-planificacion.json")
tipos_planificacion = f.read()


def formatResponse(file_read):
    parsed = json.loads(file_read)
    return Response(json.dumps(parsed, indent=4), mimetype='application/json')


api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'


@api.errorhandler(404)
def page_not_found(error):
    error_message = "Recurso no encontrado"
    response = {}
    response["errors"] = error_message
    return Response(json.dumps(response)), 404


@api.route(API_BASE_URI + '/actividades/<int:id>', methods=['GET'])
@cross_origin()
def get_actividad(id):
    return formatResponse(actividades_15)


@api.route(API_BASE_URI + '/actividades/<int:id>/tareas', methods=['GET'])
@cross_origin()
def get_actividad_tareas(id):
    return formatResponse(actividades_15_tareas)


@api.route(API_BASE_URI + '/dominios')
@cross_origin()
def get_dominios():
    return formatResponse(dominios)


@api.route(API_BASE_URI + '/idiomas')
@cross_origin()
def get_idiomas():
    return formatResponse(idiomas)


@api.route(API_BASE_URI + '/tipos-tarea')
@cross_origin()
def get_tipos_tarea():
    return formatResponse(tipos_tarea)


@api.route(API_BASE_URI + '/tipos-planificacion')
@cross_origin()
def get_tipos_planificacion():
    return formatResponse(tipos_planificacion)


@api.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    api.run(threaded=True, host='0.0.0.0',
            port=int(os.environ.get("PORT", 5000)))

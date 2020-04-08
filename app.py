from flask import Flask, json, Response, request
from flask_cors import CORS, cross_origin
from db_init import db_init
from base import session_factory
import os

from entities.dominio import Dominio
from entities.estado import Estado
from entities.tipo_tarea import TipoTarea

DIR = "respuestas"
API_BASE_URI = "/api/v1.0"

f = open(DIR + "/me.json")
me = f.read()
f = open(DIR + "/actividades_15.json")
actividades_15 = f.read()
f = open(DIR + "/actividades_15_tareas.json")
actividades_15_tareas = f.read()
f = open(DIR + "/idiomas.json")
idiomas = f.read()
f = open(DIR + "/tipos-planificacion.json")
tipos_planificacion = f.read()
f = open(DIR + "/planificacion.json")
planificacion = f.read()
f = open(DIR + "/tareas.json")
tareas = f.read()


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


@api.route('/api/oauth/v2/token', methods=['POST'])
@cross_origin()
def get_token():
    response = {}
    response["access_token"] = 1
    response["expires_in"] = 3600
    return Response(json.dumps(response)), 200


@api.route(API_BASE_URI + '/me', methods=['GET'])
@cross_origin()
def get_me():
    return formatResponse(me)


@api.route(API_BASE_URI + '/tareas/user', methods=['GET'])
@cross_origin()
def get_tareas():
    return formatResponse(tareas)


@api.route(API_BASE_URI + '/actividades/<int:id>', methods=['GET'])
@cross_origin()
def get_actividad(id):
    return formatResponse(actividades_15)


@api.route(API_BASE_URI + '/public/actividades/<int:id>', methods=['GET'])
@cross_origin()
def get_actividad_public(id):
    return formatResponse(actividades_15)


@api.route(API_BASE_URI + '/actividades/<int:id>/tareas', methods=['GET'])
@cross_origin()
def get_actividad_tareas(id):
    return formatResponse(actividades_15_tareas)


@api.route(API_BASE_URI + '/public/actividades/<int:id>/tareas', methods=['GET'])
@cross_origin()
def get_actividad_tareas_public(id):
    return formatResponse(actividades_15_tareas)


@api.route(API_BASE_URI + '/planificaciones/<int:id>', methods=['GET'])
@cross_origin()
def get_planificacion(id):
    return formatResponse(planificacion)


@api.route(API_BASE_URI + '/public/planificaciones/<int:id>', methods=['GET'])
@cross_origin()
def get_planificacion_public(id):
    return formatResponse(planificacion)


@api.route(API_BASE_URI + '/public/dominios', methods=['GET'])
@cross_origin()
def get_dominios():
    session = session_factory()
    dominios = session.query(Dominio).all()
    dominios_json = []
    for dominio in dominios:
        dominios_json.append(dominio.to_json())
    response = {}
    response["results"] = dominios_json
    return Response(json.dumps(response)), 200


@api.route(API_BASE_URI + '/public/estados', methods=['GET'])
@cross_origin()
def get_estados():
    session = session_factory()
    estados = session.query(Estado).all()
    estados_json = []
    for estado in estados:
        estados_json.append(estado.to_json())
    response = {}
    response["results"] = estados_json
    return Response(json.dumps(response)), 200


@api.route(API_BASE_URI + '/public/idiomas', methods=['GET'])
@cross_origin()
def get_idiomas():
    return formatResponse(idiomas)


@api.route(API_BASE_URI + '/public/tipos-tarea', methods=['GET'])
@cross_origin()
def get_tipos_tarea():
    session = session_factory()
    tipos_tarea = session.query(TipoTarea).all()
    tipos_tarea_json = []
    for tipo_tarea in tipos_tarea:
        tipos_tarea_json.append(tipo_tarea.to_json())
    response = {}
    response["results"] = tipos_tarea_json
    return Response(json.dumps(response)), 200


@api.route(API_BASE_URI + '/public/tipos-planificacion', methods=['GET'])
@cross_origin()
def get_tipos_planificacion():
    return formatResponse(tipos_planificacion)


@api.route("/init-database", methods=['POST'])
def init_database():
    key = request.form.get('key')
    init_key = os.environ.get("INIT_KEY")
    response = {}
    if(init_key == None):
        response["status"] = "UNAVAILABLE"
        status = 500
    elif (key == init_key):
        db_init()
        response["status"] = "OK"
        status = 200
    else:
        response["status"] = "WRONG KEY"
        status = 403
    return Response(json.dumps(response)), status


@api.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    api.run(threaded=True, host='0.0.0.0',
            port=int(os.environ.get("PORT", 5000)))

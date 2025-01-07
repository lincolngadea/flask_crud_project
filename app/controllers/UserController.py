from flask import Response, request
from app.models.User import User
from app.extensions import db

import json

def index():
    session = db.session()
    users = session.query(User).all()
    users_json = [user.serialize() for user in users]
    session.close()
    return Response(json.dumps(users_json))

def store():
    body = request.get_json()
    session = db.session()
    try:
        user = User(name=body['name'], age=body['age'], address=body['address'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return Response(json.dumps({"Erro":f"Não foi possível criar o usuário - Erro: {e}"}),
                        status=500, mimetype='application/json')
    finally:
        session.close()

def show(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return Response(json.dumps({"Erro":"Não foi possível retornar o usuário"}),
                        status=404, mimetype='application/json')
    finally:
        session.close()

def update(user_id):
    session = db.session()
    try:
        body = request.get_json()
        user = session.query(User).get(user_id)

        if body and body['name']:
            user.name = body['name']
        if body and body['age']:
            user.age = body['age']
        if body and body['address']:
            user.address = body['address']
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return Response(json.dumps({"Erro": f"Não foi possível atualizar o usuário - Erro: {e}"}),
                        status=500, mimetype='application/json')
    finally:
        session.close()
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ClientModel
from schemas import ClientSchema, ClientUpdateSchema, ClientDeleteSchema

blp = Blueprint(
    "Clients", "clients", url_prefix="/clients", description="Operations on clients"
)


@blp.route("/")
class ClientList(MethodView):
    @blp.response(200, ClientSchema(many=True))
    def get(self):
        clients = ClientModel.query.all()
        return clients

    @blp.arguments(ClientSchema)
    @blp.response(201, ClientSchema)
    def post(self, client_data):
        user_id = client_data["user_id"]
        app_version = client_data["app_version"]
        added_date = client_data.get("added_date")

        client = ClientModel(
            user_id=user_id, app_version=app_version, added_date=added_date
        )

        db.session.add(client)
        db.session.commit()

        return client

    @blp.response(204)
    def delete(self):
        ClientModel.query.delete()
        db.session.commit()
        return ""


@blp.route("/<int:client_id>")
class ClientItem(MethodView):
    @blp.response(200, ClientSchema)
    def get(self, client_id):
        client = ClientModel.query.get_or_404(client_id)
        return client

    @blp.arguments(ClientUpdateSchema)
    @blp.response(200, ClientSchema)
    def put(self, client_data, client_id):
        client = ClientModel.query.get(client_id)

        if client:
            client.app_version = client_data["app_version"]
            client.added_date = client_data.get("added_date")
        else:
            client = ClientModel(id=client_id, **client_data)

        db.session.add(client)
        db.session.commit()

        return client

    @blp.arguments(ClientDeleteSchema)
    @blp.response(204)
    def delete(self, client_data, client_id):
        client = ClientModel.query.get_or_404(client_id)
        db.session.delete(client)
        db.session.commit()
        return ""

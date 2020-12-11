from .service import FreeFairService
from .model import Fair
from ..utils.encoder import AlchemyEncoder
from flask import request, Blueprint, Response
import json

import uuid

free_fair = Blueprint('free_fair_api', __name__)


@free_fair.route('/', methods=['GET'])
def get_filtered():
    return json.dumps(FreeFairService().filter(nome_feira=request.args.get('nome_feira'),
                                               distrito=request.args.get('distrito'),
                                               regiao5=request.args.get('regiao5'),
                                               bairro=request.args.get('bairro')), cls=AlchemyEncoder)


@free_fair.route('/<fair_uuid>', methods=['GET'])
def get_by_uuid(fair_uuid: uuid.uuid4):
    fair = FreeFairService().find_by_uuid(fair_uuid)
    if fair is None:
        return Response(status=404)

    return json.dumps(fair, cls=AlchemyEncoder)


@free_fair.route('', methods=['POST'])
def insert():
    FreeFairService().save(Fair(**request.get_json()))
    return Response(status=201)


@free_fair.route('/<fair_uuid>', methods=['DELETE'])
def delete(fair_uuid: uuid.uuid4):
    deleted = FreeFairService().delete(fair_uuid)
    if deleted is None:
        return Response(status=404)

    return Response(status=204)


@free_fair.route('/<fair_uuid>', methods=['PUT'])
def update(fair_uuid: uuid.uuid4):
    fair = Fair(**request.get_json())
    updated = FreeFairService().update(fair_uuid, fair)
    if updated is None:
        return Response(status=404)

    return Response(status=204)

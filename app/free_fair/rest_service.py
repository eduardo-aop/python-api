from .service import FreeFairService
from .model import Fair
from ..utils.encoder import AlchemyEncoder
from flask import request, Blueprint, Response
import json

free_fair = Blueprint('free_fair_api', __name__)


@free_fair.route('/', methods=['GET'])
def get_filtered():
    nome_feira = request.args.get('nome_feira')
    distrito = request.args.get('distrito')
    regiao5 = request.args.get('regiao5')
    bairro = request.args.get('bairro')
    return json.dumps(FreeFairService().filter(nome_feira=nome_feira,
                                               distrito=distrito,
                                               regiao5=regiao5,
                                               bairro=bairro), cls=AlchemyEncoder)


@free_fair.route('', methods=['GET'])
def get_all():
    return json.dumps(FreeFairService().find_all(), cls=AlchemyEncoder)


@free_fair.route('', methods=['POST'])
def insert():
    FreeFairService().save(Fair(**request.get_json()))
    return Response(status=201)


@free_fair.route('/<register_id>', methods=['DELETE'])
def delete(register_id):
    return f'deleted free fair {register_id}'


@free_fair.route('/<register_id>', methods=['PUT'])
def update(register_id):
    return f'deleted free fair {register_id}'

from flask import Blueprint
from .service import FreeFairService

free_fair = Blueprint('free_fair_api', __name__)


@free_fair.route('/<register_id>', methods=['GET'])
def get_by_id(register_id):
    return f'{register_id} free fair id'


@free_fair.route('', methods=['GET'])
def get_all():
    return FreeFairService().find_all()


@free_fair.route('', methods=['POST'])
def insert():
    return 'all free fairs'


@free_fair.route('/<register_id>', methods=['DELETE'])
def delete(register_id):
    return f'deleted free fair {register_id}'


@free_fair.route('/<register_id>', methods=['PUT'])
def update(register_id):
    return f'deleted free fair {register_id}'

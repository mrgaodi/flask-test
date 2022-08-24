from flask import Blueprint, request
from app.service import whitelist_service as WhitelistService

whitelist = Blueprint('whitelist', __name__)


@whitelist.route('/whitelists', methods=['GET'])
def get_whitelists():
    return WhitelistService.get_whitelists()


@whitelist.route('/whitelists/<int:id>', methods=['GET'])
def get_whtelist(id):
    return WhitelistService.get_whitelist(id)


@whitelist.route('/whitelists', methods=['POST'])
def add_whtelist():
    ip, desc = request.json.get('ip'), request.json.get('desc')
    return WhitelistService.add_whitelists(ip, desc)


@whitelist.route('/whitelists/<int:id>', methods=['PATCH'])
def update_whtelist(id):
    ip, desc = request.json.get('ip'), request.json.get('desc')
    return WhitelistService.update_whitelist(id, ip, desc)


@whitelist.route('/whitelists/<int:id>', methods=['DELETE'])
def del_whtelist(id):
    return WhitelistService.del_whtelist(id)

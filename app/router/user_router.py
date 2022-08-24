from flask import Blueprint, request
from app.service import user_service as UserService

user = Blueprint('user', __name__)


@user.route('/register', methods=['POST'])
def register():
    username, password, confirm = request.form.get(
        'username'), request.form.get('password'), request.form.get('confirm')
    return UserService.register(username, password, confirm)


@user.route('/login', methods=['POST'])
def login():
    username, password = request.form.get(
        'username'), request.form.get('password')
    return UserService.login(username, password)

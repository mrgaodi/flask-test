from app import db
from app.model.user_model import User
from app.utils.response import RET, resp


@resp
def register(username, password, confirm):
    """
    用户注册
    注意：没有添加token存储，用户密码应该传递时通过rsa进行加密
    """
    if not all([username, password, confirm]):
        return RET.PARAMS_ERR, '用户名或密码不能为空'
    if confirm != password:
        return RET.PARAMS_ERR, '两次密码不一致'
    user = User(username=username)
    user.password = password

    db.session.add(user)
    db.session.commit()

    return RET.OK, '注册成功'


@resp
def login(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return RET.NO_DATA_ERR, '用户名或密码错误'
    if not user.check_password(password):
        return RET.PARAMS_ERR, '用户名或密码错误'
    return RET.OK, '登录成功'

from app.model.whitelist_model import WhiteList
from app.utils.response import RET, resp
from app import db


@resp
def get_whitelists():
    rows = WhiteList.query.all()
    return RET.OK, [row.json() for row in rows]


@resp
def get_whitelist(id):
    row = WhiteList.query.filter_by(id=id).first()
    if not row:
        return RET.NO_DATA_ERR, '未发现数据'
    return RET.OK, row.json()


@resp
def add_whitelists(ip, desc):
    if not ip:
        return RET.PARAMS_ERR, '参数异常'
    row = WhiteList(ip=ip, desc=desc)
    db.session.add(row)
    db.session.commit()
    return RET.OK, 'OK'


@resp
def update_whitelist(id, ip, desc):
    row = WhiteList.query.filter_by(id=id).first()
    if not row:
        return RET.NO_DATA_ERR, '未发现数据'
    if ip and row.ip != ip:
        row.ip = ip
    if row.desc != desc:
        row.desc = desc
    db.session.add(row)
    db.session.commit()
    return RET.OK, 'OK'


@resp
def del_whtelist(id):
    row = WhiteList.query.filter_by(id=id).first()
    if not row:
        return RET.NO_DATA_ERR, '未发现数据'
    db.session.delete(row)
    db.session.commit()
    return RET.OK, 'OK'

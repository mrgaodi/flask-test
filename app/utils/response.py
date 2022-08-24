from flask import jsonify
from functools import wraps
from enum import Enum
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import db
import traceback
import re


class RET(Enum):
    OK = 2000
    PARAMS_ERR = 4001
    SERVER_ERR = 5000
    DB_ERR = 5100
    EXIST_ERR = 5101
    NO_DATA_ERR = 5102
    SQL_ERR = 5103


def resp(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        try:
            code, msg = func(*args, **kwargs)
            if code == RET.OK:
                return jsonify(code=code.value, data=msg)
            return jsonify(code=code.value, msg=msg)
        except IntegrityError as e:
            traceback.print_exc()
            db.session.rollback()
            pattern = re.compile(r'.*\((\d+),.*')
            m = pattern.match(e.args[0])
            err_code = int(m.group(1))
            if err_code == 1062:
                return jsonify(code=RET.EXIST_ERR.value, msg='数据已存在')
            return jsonify(code=RET.SQL_ERR.value, msg='sql错误')
        except SQLAlchemyError:
            traceback.print_exc()
            db.session.rollback()
            return jsonify(code=RET.DB_ERR.value, msg='数据库错误')
        except Exception:
            traceback.print_exc()
            return jsonify(code=RET.SERVER_ERR.value, msg='服务器错误')
    return _wrapper

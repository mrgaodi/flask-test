from . import db


class WhiteList(db.Model):
    __tablename__ = 'tbl_whitelist'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ip = db.Column(db.String(30), nullable=True, unique=True)
    desc = db.Column(db.String(200))

    def json(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'desc': self.desc,
        }

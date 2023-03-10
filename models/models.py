from app import db
from datetime import datetime

class Matches(db.Model):
    __tablename__ = "matches"
    code = db.Column(db.Integer, primary_key=True)
    players = db.Column(db.Integer)
    data_match = db.Column(db.DateTime)
    winner = db.Column(db.String(25))
    turns = db.Column(db.Integer)
    is_done = db.Column(db.Boolean)


    def __repr__(self):
        return f"Matches(code: {self.code})"


class Player(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    score = db.Column(db.Integer)
    match_code = db.Column(db.Integer, db.ForeignKey("matches.code"), nullable = False)

    def __repr__(self):
        return f"Player(code: {self.id} , name: {self.name})"


class Rounds(db.Model):
    __tablename__ = "rounds"
    id = db.Column(db.Integer, primary_key=True)
    score_one = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable = False)
    match_code = db.Column(db.Integer, db.ForeignKey("matches.code"), nullable = False)
    def __repr__(self):
        return f"Rounds(code: {self.id})"


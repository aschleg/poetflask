from app import db


class Poet(db.Model):
    __table_args__ = {"schema": "poetry"}
    __tablename__ = 'poets'

    id = db.Column(db.INT, primary_key=True)
    date_of_birth = db.Column(db.VARCHAR(255))
    date_of_death = db.Column(db.VARCHAR(255))
    description = db.Column(db.TEXT)
    educated_at = db.Column(db.VARCHAR(255))
    gender = db.Column(db.VARCHAR(10))
    occupation = db.Column(db.VARCHAR(255))
    place_of_birth = db.Column(db.VARCHAR(255))
    place_of_burial = db.Column(db.VARCHAR(255))
    place_of_death = db.Column(db.VARCHAR(255))
    year_of_birth = db.Column(db.INT)
    year_of_death = db.Column(db.INT)
    month_of_birth = db.Column(db.INT)
    month_of_death = db.Column(db.INT)
    day_of_birth = db.Column(db.INT)
    day_of_death = db.Column(db.INT)
    first_name = db.Column(db.VARCHAR(255))
    last_name = db.Column(db.VARCHAR(255))
    name = db.Column(db.VARCHAR(255))
    image_location = db.Column(db.VARCHAR(255))


class Poems(db.Model):
    __table_args__ = {"schema": "poetry"}
    __tablename__ = 'poems'

    id = db.Column(db.INT, primary_key=True)
    author = db.Column(db.VARCHAR(255))
    linecount = db.Column(db.INT)
    lines = db.Column(db.TEXT, unique=True)
    title = db.Column(db.TEXT, unique=True)


class PoetOfTheDay(db.Model):
    __table_args__ = {"schema": "poetry"}
    __tablename__ = 'poet_of_the_day'

    id = db.Column(db.INT, primary_key=True)
    author = db.Column(db.VARCHAR(255))
    date = db.Column(db.VARCHAR(255), unique=True)

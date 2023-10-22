import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Numeric, func
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class User(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    registration_date = Column(Date, nullable=False)
    rating_count = Column(Integer, default=0)

    visits = relationship('Visit', backref='user', lazy=True)


class Visit(Model):
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    food = Column(String(100), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    rating = relationship('Rating', uselist=False, back_populates='visit')
    chef_rating = relationship('ChefRating', uselist=False, back_populates='visit')


class Rating(Model):
    id = Column(Integer, primary_key=True)
    stars = Column(Integer, nullable=False)
    comment = Column(String(500))

    visit_id = Column(Integer, ForeignKey('visit.id'), nullable=False)
    visit = relationship('Visit', back_populates='rating')
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)


class ChefRating(Model):
    id = Column(Integer, primary_key=True)
    stars = Column(Integer, nullable=False)
    comment = Column(String(500))

    visit_id = Column(Integer, ForeignKey('visit.id'), nullable=False)
    visit = relationship('Visit', back_populates='chef_rating')
    chef_id = Column(Integer, ForeignKey('chef.id'), nullable=False)
    chef = relationship('Chef', back_populates='chef_ratings')


class Restaurant(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    opening_year = Column(Integer)
    average_rating = Column(Numeric, default=0.0, onupdate=func.coalesce(func.avg(Rating.stars), 0))
    chefs = relationship('Chef', backref='restaurant', lazy=True)
    photo = Column(String(200))
    website = Column(String(100))
    ico = Column(String(15))
    phone = Column(String(20))
    opening_hours = Column(String(100))

    ratings = relationship('Rating', backref='restaurant', lazy=True)
    chefs = relationship('Chef', backref='working_restaurant', lazy=True)


class Chef(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    photo = Column(String(200))
    contact = Column(String(100))

    working_restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', back_populates='chefs')
    chef_ratings = relationship('ChefRating', back_populates='chef')
    average_rating = Column(Numeric, default=0.0, onupdate=func.coalesce(func.avg(ChefRating.stars), 0))
    favorite_foods = relationship('FavoriteFood', back_populates='chef')


class FavoriteFood(Model):
    id = Column(Integer, primary_key=True)
    food_name = Column(String(100), nullable=False)
    chef_id = Column(Integer, ForeignKey('chef.id'), nullable=False)
    chef = relationship('Chef', back_populates='favorite_foods')







class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Vyrobce(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20))
    personal_celphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey("gender.id"), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)

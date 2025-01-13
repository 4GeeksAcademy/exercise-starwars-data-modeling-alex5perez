import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    subscription_date = Column(Date, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    favorites = relationship("Favorite", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "subscription_date": str(self.subscription_date),
            "firstname": self.firstname,
            "lastname": self.lastname
        }

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(50), nullable=True)
    mass = Column(String(50), nullable=True)
    hair_color = Column(String(50), nullable=True)
    skin_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    birth_year = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    films = relationship("CharacterFilm", back_populates="character")
    vehicles = relationship("CharacterVehicle", back_populates="character")
    starships = relationship("CharacterStarship", back_populates="character")
    homeworld = relationship("Planet")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            "homeworld_id": self.homeworld_id,
            "films": self.films,
            "starships": self.starships,
            "vehicles": self.vehicles
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(50), nullable=True)
    rotation_period = Column(String(50), nullable=True)
    orbital_period = Column(String(50), nullable=True)
    gravity = Column(String(50), nullable=True)
    population = Column(String(50), nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(String(50), nullable=True)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited
        }

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=True)
    designation = Column(String(250), nullable=True)
    average_height = Column(String(50), nullable=True)
    average_lifespan = Column(String(50), nullable=True)
    language = Column(String(250), nullable=True)
    homeworld_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    homeworld = relationship("Planet")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
            "language": self.language,
            "homeworld_id": self.homeworld_id,
            "created": self.created,
            "edited": self.edited
        }

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(String(50), nullable=True)
    length = Column(String(50), nullable=True)
    max_atmosphering_speed = Column(String(50), nullable=True)
    crew = Column(String(50), nullable=True)
    passengers = Column(String(50), nullable=True)
    cargo_capacity = Column(String(50), nullable=True)
    consumables = Column(String(250), nullable=True)
    hyperdrive_rating = Column(String(50), nullable=True)
    MGLT = Column(String(50), nullable=True)
    starship_class = Column(String(250), nullable=True)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    characters = relationship("CharacterStarship", back_populates="starship")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
            "created": self.created,
            "edited": self.edited
        }

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(String(50), nullable=True)
    length = Column(String(50), nullable=True)
    max_atmosphering_speed = Column(String(50), nullable=True)
    crew = Column(String(50), nullable=True)
    passengers = Column(String(50), nullable=True)
    cargo_capacity = Column(String(50), nullable=True)
    consumables = Column(String(250), nullable=True)
    vehicle_class = Column(String(250), nullable=True)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    characters = relationship("CharacterVehicle", back_populates="vehicle")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_class": self.vehicle_class,
            "created": self.created,
            "edited": self.edited
        }

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    director = Column(String(250), nullable=True)
    producer = Column(String(250), nullable=True)
    release_date = Column(String(50), nullable=True)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    characters = relationship("CharacterFilm", back_populates="film")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "producer": self.producer,
            "release_date": self.release_date,
            "created": self.created,
            "edited": self.edited
        }

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=True)
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")
    starship = relationship("Starship")
    vehicle = relationship("Vehicle")
    film = relationship("Film")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "starship_id": self.starship_id,
            "vehicle_id": self.vehicle_id,
            "film_id": self.film_id
        }

class CharacterFilm(Base):
    __tablename__ = 'characterfilm'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)
    character = relationship("Character", back_populates="films")
    film = relationship("Film", back_populates="characters")

class CharacterVehicle(Base):
    __tablename__ = 'charactervehicle'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    character = relationship("Character", back_populates="vehicles")
    vehicle = relationship("Vehicle", back_populates="characters")

class CharacterStarship(Base):
    __tablename__ = 'characterstarship'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=False)
    character = relationship("Character", back_populates="starships")
    starship = relationship("Starship", back_populates="characters")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

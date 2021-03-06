import numpy as np
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import mongo_fns


# Create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return'home'


@app.route('/<position>/<stat>')
def pos_stat():

    data = []
    return jsonify(data)


@app.route('/x')
def x():
    data = []
    return jsonify(data)


@app.route('/x')
def x():
    data = []
    return jsonify(data)


@app.route('/x')
def x():
    data = []
    return jsonify(data)


@app.route('/x')
def x():
    data = []
    return jsonify(data)


#################################################
# Database Setup
#################################################


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/precipitation<br/>"
#         f"/api/v1.0/stations<br/>"
#         f"/api/v1.0/tobs<br/>"
#         f"/api/v1.0/start<br/>"
#         f"/api/v1.0/start/end"
#     )
#
#
# @app.route("/api/v1.0/precipitation")
# def precip():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)
#
#     """Return a list of all passenger names"""
#     # Query all passengers
#
#     results = session.query(Measurement.prcp).order_by(Measurement.date.desc()).all()
#
#     session.close()
#     precip = list(np.ravel(results))
#     return jsonify(precip)
#
#
# @app.route("/api/v1.0/stations")
# def stations():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)
#
#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Station.name).all()
#
#     session.close()
#
#     return jsonify(results)
#
#
# @app.route("/api/v1.0/tobs")
# def tobs():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)
#     highest_station_id = 'USC00519281'
#
#     results = session.query(Measurement.tobs).filter(Measurement.station == highest_station_id).all()
#     session.close()
#
#     # Convert list of tuples into normal list
#     output = list(np.ravel(results))
#
#     return jsonify(results)
#
#
# @app.route("/api/v1.0/<start>")
# def just_start(start):
#     # year-month-day
#     cleaned_start = start.replace(" ", "").lower()
#
#     session = Session(engine)
#
#     results = session.query(Measurement.tobs).order_by(Measurement.date.desc()).filter(
#         Measurement.date >= cleaned_start).all()
#
#     session.close()
#     return jsonify(results)
#
#
# @app.route("/api/v1.0/<start>/<end>")
# def start_n_end(start, end):
#     # year-month-day
#     cleaned_start = start.replace(" ", "").lower()
#     cleaned_end = end.replace(" ", "").lower()
#
#     session = Session(engine)
#
#     results = session.query(Measurement.tobs).order_by(Measurement.date.desc()).filter(
#         (Measurement.date.between(cleaned_start, cleaned_end))).all()
#
#     session.close()
#     return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

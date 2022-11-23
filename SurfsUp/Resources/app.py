#importing dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#Database Setup

#create engine
engine =  create_engine('sqlite:///hawaii.sqlite')

#reflect and existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#save reference to the table 

# Save reference to the table
measurement = Base.classes.measurement

# Save reference to the table
ststion = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #session
    precipitation_m = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= '2016-08-23')\
    .filter(Measurement.date<='2017-08-24').order_by(Measurement.date).all()
    return jsonify(precipitation_m)

@app.route("/api/v1.0/stations")
def stations():
    #session
    active = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    return jsonify(active)
    
@app.route("/api/v1.0/tobs")
def tobs():
    #session
    tobs = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs))\
    .filter(Measurement.station=='USC00519281').all()
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def tobs():
    #session
    results=session.query(Measurement.tobs).filter(Measurement.station=='USC00519281')\
    .filter(Measurement.date>='2016-08-23').all()
    return jsonify(results)

@app.route("/api/v1.0/<start>/<end>")
def tobs():
    #session
    start_andend = results=session.query(Measurement.tobs).filter(Measurement.station=='USC00519281')\
    .filter(Measurement.date>='2016-08-23').all()
    return jsonify(start_andend)

if __name__ == '__main__':
    app.run(debug=True)

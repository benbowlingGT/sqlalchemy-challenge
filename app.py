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
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation"""
    # Query all stations
    results = session.query(precipitation.name).all()

    session.close()

    # Convert list of tuples into normal list
    name =list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.close()

    """Return a list of """
    # Query all tobs
    results = session.query(tobs).all()

    session.close()

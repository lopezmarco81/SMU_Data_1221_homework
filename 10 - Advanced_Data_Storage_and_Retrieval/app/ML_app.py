import numpy as np
import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# database setup
path = "sqlite:///Resources/hawaii.sqlite"
engine = create_engine(path)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"""
        <ul>
            <li><a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a></li>
             <li><a href='/api/v1.0/2016-06-01/2016-08-31'>/api/v1.0/2016-06-01/2016-08-31</a></li>
        </ul
        """
    )

@app.route("/api/v1.0/precipitation")
def getPrcp():
    conn = engine.connect()
    query = """
        SELECT
            date,
            station,
            prcp
        FROM
            measurement
        ORDER BY
            date asc,
            station asc
        """

    df = pd.read_sql(query, conn)
    conn.close()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def getTempRanges(start, end):
    conn = engine.connect()
    query = f"""
        SELECT
            min(tobs) as tmin,
            max(tobs) as tmax,
            avg(tobs) as tavg
        FROM
            measurement
        WHERE
            date >= '{start}'
            and date <= '{end}'
        """

    df = pd.read_sql(query, conn)
    conn.close()
    data = df.to_dict(orient="records")
    return(jsonify(data))

if __name__ == '__main__':
    app.run(debug=True)

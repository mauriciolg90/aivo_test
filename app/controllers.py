# For queries and response
from db_setup import Session
from app.models import Indicators
from flask import Flask, request, jsonify

# Application for routing
application = Flask(__name__)

"""
    Returns a list of countries filtering by:
        INDICATOR: SW_LIFS (Life satisfaction)
        INEQUALITY: TOT (Total)
        VALUE: greater than the input index
    --------------------------------------
    Parameters:
        index: min threshold for filtering
"""
@application.route('/countries/sw_lifs_gt/<float:index>', methods=['GET'])
def countries_sw_lifs_gt(index):
    if index > 0.0:
        session = Session()
        # Query on the database according to the filters
        countries = session.query(Indicators.location, Indicators.country).filter(
            Indicators.indicator_code == 'SW_LIFS',
            Indicators.inequality_code == 'TOT',
            Indicators.value > index
        ).all()
        # Return the results
        return jsonify(countries)
    else:
        message = {
            'status': 400,
            'message': 'Bad Request: The index is invalid! Please, select a value greater than 0',
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp

"""
    Returns a custom message for 404 error
    --------------------------------------
    Parameters:
        None so far
"""
@application.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
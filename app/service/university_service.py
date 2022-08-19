import logging
import os

import requests
from flask import request
from flask_caching import Cache

from app import app
from app.config import CacheConfig

app.config.from_object(CacheConfig)
cache = Cache(app)


@cache.cached(timeout=10, query_string=True)
def get_university(university):
    API_URL = os.environ.get('UNIVERSITY_API_URL')

    logging.debug('university url: ' + API_URL)
    logging.info('university url: ' + API_URL)
    logging.warning('university url: ' + API_URL)
    logging.error('university url: ' + API_URL)
    logging.critical('university url: ' + API_URL)

    search = request.args.get('country')
    response = requests.get(f'{API_URL}{search}')
    return response

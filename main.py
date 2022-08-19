#!venv/bin/python
import os

from app import app

PORT = os.environ.get('PORT', 8081)
DEBUG_MODE = os.environ.get('DEBUG_MODE', False)
app.run(debug=DEBUG_MODE, host='0.0.0.0', port=PORT)
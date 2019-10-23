from app import app
from flask import render_template, jsonify
from ..routes.routes_utils import refresh_token

app_config = app.config

@app.route('/')
def index():
  return render_template('viewer.html', version="1.0")

@app.route('/model', methods=['POST'])
def model():
  token = refresh_token()
  return jsonify({
    'documentId': 'urn:{}'.format('[MODEL_URN]'),
    'accessToken': '{}'.format(token)
  })

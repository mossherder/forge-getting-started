from app import app
from flask import render_template, jsonify
from ..routes.routes_utils import refresh_token

app_config = app.config

MarkSampleWallrvt = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6YmFtY29yZV9pbnN0YWxsYXRpb25fbW9kZWxzLTEvbW9kZWxfNS5ydnQ'
starr1rvt = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6YmFtY29yZV9pbnN0YWxsYXRpb25fbW9kZWxzLTEvbW9kZWxfNi5ydnQ'
starrWithPallets = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6YmFtY29yZV9pbnN0YWxsYXRpb25fbW9kZWxzLTEvbW9kZWxfNy5ydnQ'
starrPalletsAndAnnotation = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6YmFtY29yZV9pbnN0YWxsYXRpb25fbW9kZWxzLTEvbW9kZWxfOS5ydnQ'

@app.route('/')
def index():
  return render_template('viewer.html', version="2.5")

@app.route('/model', methods=['POST'])
def model():
  token = refresh_token()
  return jsonify({
    'documentId': 'urn:{}'.format(starrPalletsAndAnnotation),
    'accessToken': '{}'.format(token)
  })

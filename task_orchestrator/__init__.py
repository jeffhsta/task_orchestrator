from flask import Flask, jsonify, request

from task_orchestrator import docker_adaptor

import json


app = Flask(__name__)


def parse_container(container):
  return {
    'id': container.id,
    'image': container.attrs['Config']['Image'],
    'command': ' '.join(container.attrs['Config']['Cmd']),
    'entrypoint': container.attrs['Config']['Entrypoint'],
    'created_at': container.attrs['Created'],
    'status': container.status
  }


@app.route("/", methods = ['GET'])
def hello():
  return jsonify({'status': 'working'}), 200


@app.route("/tasks", methods = ['GET'])
def list_tasks():
  status = request.args.get('status') or 'all'
  containers = docker_adaptor.list_containers()
  containers = [parse_container(c) for c in containers if status == 'all' or c.status == status]

  return jsonify({'data': containers}), 200

@app.route("/tasks", methods = ['POST'])
def run_task():
  body = request.json

  if not body['task'] in docker_adaptor.AVAILABLE_TASKS:
    return jsonify({
        'message': 'Bad request',
        'details': 'Invalid tasks',
        'available_tasks': docker_adaptor.AVAILABLE_TASKS
      }), 400

  container = docker_adaptor.run_task(body['task'])
  return jsonify({'data': parse_container(container)}), 201


@app.route("/tasks/<task_id>", methods = ['DELETE'])
def remove_task(task_id):
  docker_adaptor.stop_task(task_id)

  if request.args.get('remove'):
    docker_adaptor.remove_task(task_id)

  return jsonify({}), 204


@app.route("/tasks/<task_id>/logs", methods = ['GET'])
def fetch_logs(task_id):
  logs = docker_adaptor.fetch_logs(task_id)
  return jsonify({'data': logs.decode('utf-8')}), 200

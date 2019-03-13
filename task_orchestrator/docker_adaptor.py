from docker import DockerClient


DOCKER_SOCKET = 'http+unix://var/run/docker.sock'
AVAILABLE_TASKS = ['test']


def list_containers():
  client = DockerClient(base_url = DOCKER_SOCKET)
  return client.containers.list(all=True)


def run_task(task):
  if not task in AVAILABLE_TASKS:
    raise Exception('Invalid task')
  
  client = DockerClient(base_url = DOCKER_SOCKET)
  return client.containers.run('alpine', 'echo this is a test', detach=True)


def fetch_logs(container_id):
  client = DockerClient(base_url = DOCKER_SOCKET)
  [container] = [c for c in client.containers.list(all=True) if c.id == container_id]
  return container.logs()


def stop_task(container_id):
  client = DockerClient(base_url = DOCKER_SOCKET)
  [container] = [c for c in client.containers.list(all=True) if c.id == container_id]
  container.stop()


def remove_task(container_id):
  client = DockerClient(base_url = DOCKER_SOCKET)
  [container] = [c for c in client.containers.list(all=True) if c.id == container_id]
  container.remove()

def parse_container(container):
  return {
    'id': container.id,
    'image': container.attrs['Config']['Image'],
    'command': ' '.join(container.attrs['Config']['Cmd']),
    'entrypoint': container.attrs['Config']['Entrypoint'],
    'created_at': container.attrs['Created'],
    'status': container.status
  }

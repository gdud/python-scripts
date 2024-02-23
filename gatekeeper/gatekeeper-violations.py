#!/usr/bin/python3

import subprocess
import json
import os

input_namespace = os.getenv('GTKV_NAMESPACE', 'default')
input_ignore_string = os.getenv('GTKV_IGNORE_STRING', '')

OUTPUT_DIR = 'output'

def prepare_output_directory(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass

    for f in os.listdir(OUTPUT_DIR):
        file_path = os.path.join(directory, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

command = ['kubectl', 'get', 'constraints', '-o', 'json']
result = subprocess.run(command, capture_output=True, check=True)

prepare_output_directory(OUTPUT_DIR)

data = json.loads(result.stdout)


for item in data['items']:

  kind = item['kind']
  name = item['metadata']['name']
  total_violations = int(item['status']['totalViolations'])
  
  output = []

  if total_violations > 0:
    for v in item['status']['violations']:
      if v['namespace'] == input_namespace and (len(input_ignore_string) == 0 or str(v['message']).find(input_ignore_string) == -1):
        output.append(v)
        
  if len(output) > 0:
    filename = f'{name}.json'
    with open(f'{OUTPUT_DIR}/{filename}', 'w') as file: 
      file.write(json.dumps(output, indent=2))

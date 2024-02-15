import subprocess, json
from KubernetesContext import *

def exec_kubectl(cmd: str) -> str:
  cmd_l = ['kubectl']
  cmd_l.extend(cmd.split(' '))
  result = subprocess.run(cmd_l, capture_output=True, check=True, text=True)
  return result.stdout

def get_contexts():
  kout = exec_kubectl('config view -o json')
  output = json.loads(kout)
  contexts = []

  current_context = get_current_context()

  for ctx in output['contexts']:
    contexts.append(KubernetesContext(ctx['name'], ctx['name'] == current_context))

  return contexts

def get_current_context() -> str:
  kout = exec_kubectl('config current-context')
  return kout.strip()

def use_context(new_context: KubernetesContext):
  exec_kubectl(f'config use-context {new_context.name}')
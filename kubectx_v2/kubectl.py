import subprocess

def exec_kubectl(cmd: str) -> str:
  cmd_l = ['kubectl']
  cmd_l.extend(cmd.split(' '))
  result = subprocess.run(cmd_l, capture_output=True, check=True, text=True)
  return result.stdout

def use_context(new_context):
  exec_kubectl(f"config use-context {new_context['name']}")
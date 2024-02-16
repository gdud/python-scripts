#!/usr/bin/python3

from typing import List
from kubectl import *


from kubernetes import config

def print_contexts(contexts, current_context) -> None:
  for i, ctx in enumerate(contexts, start=1):
    indicator = ' *' if current_context['name'] == ctx['name'] else ''
    print(f"{i}) {ctx['name']}{indicator}")

def get_user_input() -> int:
  print_contexts(all_contexts, current_context)
  ctx_number = input('?> ')
  
  if len(ctx_number) == 0 or not ctx_number.isdigit():
    return 0
  else:
    return int(ctx_number)

all_contexts, current_context = config.list_kube_config_contexts()

while True:
  ctx_number = get_user_input()
  if ctx_number > 0 and ctx_number <= len(all_contexts):
    break

new_context = all_contexts[ctx_number - 1]
use_context(new_context)
print(f"Switched to context \"{new_context['name']}\".")
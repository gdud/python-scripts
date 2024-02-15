import json
from typing import List
from kubectl import *
from KubernetesContext import *


def print_contexts(contexts: List[KubernetesContext]) -> None:
  for i, ctx in enumerate(contexts, start=1):
    current = ' *' if ctx.is_current else ''
    print(f'{i}) {ctx.name}{current}')

def get_user_input() -> int:
  print_contexts(contexts)
  ctx_number = input('?> ')
  
  if len(ctx_number) == 0 or not ctx_number.isdigit():
    return 0
  else:
    return int(ctx_number)

contexts = get_contexts()

while True:
  ctx_number = get_user_input()
  if ctx_number > 0 and ctx_number <= len(contexts):
    break

new_context = contexts[ctx_number - 1]
use_context(new_context)
print(f'Switched to context "{new_context.name}".')
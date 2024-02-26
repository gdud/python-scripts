from typing import Union

from fastapi import FastAPI, Response

import platform
import psutil

app = FastAPI()


@app.get("/")
def home():
    message = 'Hello World!'
    return Response(content=message, media_type="text/html")

@app.get("/systeminfo")
def system_info():
    
    memory = psutil.virtual_memory()

    system_info = {
        "system": platform.system(),
        "node": platform.node(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "cpu": {
          "count" : f'{psutil.cpu_count()}',
          "percent": f'{psutil.cpu_percent()}'
        },
        "memory": {
          "total": format_memory(memory.total),
          "available": format_memory(memory.available),
          "used": format_memory(memory.used),
          "percent": f'{memory.percent}%'
        }
    }

    return system_info

def format_memory(mem: float) -> str:
    value = round(mem/1024/1024/1024, 1)
    return f'{value}G'
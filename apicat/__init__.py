from fastapi import FastAPI
import importlib
from apicat import config
app = FastAPI()

cfg = config.read("config.toml")
plugin_list = cfg["plugins"]

for plugin_name in plugin_list:
    plugin = importlib.import_module("apicat_"+plugin_name)
    if plugin.metadata.type == "api" or plugin.metadata.type == "API" or plugin.metadata.type == "Api":
        app.include_router(
            plugin.router,
            prefix="/api"+plugin.metadata.path,
            tags=[plugin.metadata.tag]
        )
    elif plugin.metadata.type == "admin" or plugin.metadata.type == "Admin" or plugin.metadata.type == "ADMIN":
        app.include_router(
            plugin.router,
            prefix="/admin"+plugin.metadata.path,
            tags=[plugin.metadata.tag]
        )
@app.get("/")
def root_path():
    return_message = {
        "code": 200,
        "message": "successes",
        "plugin": "apicat_home",
        "info": {
            "message": "Welcome"
        }
    }
    return return_message

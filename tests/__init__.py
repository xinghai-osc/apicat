from fastapi import FastAPI
import importlib
from apicat import config
app = FastAPI()

cfg = config.read("config.toml")
plugin_list = "plugins"

for plugin_name in plugin_list:
    plugin = importlib.import_module("apicat_"+plugin_name)
    app.include_router(
        plugin.router,
        prefix=plugin.metadata.path,
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
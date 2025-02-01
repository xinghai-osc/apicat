from fastapi import FastAPI
from starlette.responses import RedirectResponse
import importlib
from apicat import config
app = FastAPI()

cfg = config.read("config.toml")
plugin_list = cfg["plugins"]

for plugin_name in plugin_list:
    plugin = importlib.import_module("apicat_"+plugin_name)
    if plugin.metadata.type == "admin" or plugin.metadata.type == "Admin" or plugin.metadata.type == "ADMIN":
        app.include_router(
            plugin.router,
            prefix="/admin"+plugin.metadata.path,
            tags=[plugin.metadata.tag]
        )
    else:
        app.include_router(
            plugin.router,
            prefix="/api"+plugin.metadata.path,
            tags=[plugin.metadata.tag]
        )

@app.get("/")
def root_path():
    url = app.url_path_for("docs")
    resp = RedirectResponse(url=url)
    return resp

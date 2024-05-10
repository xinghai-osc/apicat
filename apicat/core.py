import importlib
from flask import Flask
def register_plugins(plugin_names,app):
    for plugin_name in plugin_names:
        try:
            plugin_module = importlib.import_module(str(plugin_name))
            blueprint = getattr(plugin_module, 'blueprint', None)
            if blueprint:
                blueprint.name = plugin_name
                app.register_blueprint(blueprint)
            else:
                print(f"{plugin_name} 不是一个有效的apicat插件。")
        except ImportError:
            print(f"找不到插件 {plugin_name}。")
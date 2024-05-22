import importlib
import yaml
import xhlog as log
from flask import Flask
def register_plugins(app: Flask):
    """
    ApiCat-接口猫 插件注册
    参数：
    app:flask实例
    返回：无
    """
    
    with open('plugins.yaml', encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    plugin_list = list(data.keys())
    for plugin_name in plugin_list:
        try:
            plugin_module = importlib.import_module(str(plugin_name))
            blueprint = getattr(plugin_module, 'blueprint', None)
            if blueprint:
                blueprint.name = plugin_name
                app.register_blueprint(blueprint)
            else:
                log.warning(f"{plugin_name} 不是一个有效的apicat插件。")
        except ImportError:
            log.error(f"找不到插件 {plugin_name}。")
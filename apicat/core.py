import importlib
from flask import Flask
def register_plugins(plugin_names,app):
    """
    ApiCat-接口猫 插件注册
    参数：
    plugin_names:插件名列表
    app:flask实例
    返回：无
    """
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
from flask import Flask, render_template_string
from importlib import import_module
from . import core, config
import xhlog as log

app = Flask("ApiCat")

@app.route('/')
def docs():
    plugin_docs = {}
    for blueprint_name in app.blueprints:
        module_name = blueprint_name.replace('-', '_')  # 转换为模块导入格式
        try:
            module = import_module(module_name)
            plugin_docs[blueprint_name] = module.docs
        except (ImportError, AttributeError):
            # 如果找不到模块或模块中没有docs，则跳过或记录错误
            log.error(f"插件 {blueprint_name} 没有文档。")

    combined_html = '<h1>欢迎使用 ApiCat 🎉</h1>'
    for plugin_name, docs_func in plugin_docs.items():
        docs_str = docs_func() if callable(docs_func) else str(docs_func)
        combined_html += f'<div><h2>{plugin_name}</h2><p>{docs_str}</p></div>'
    return render_template_string(combined_html)

def start(plugin_list: list):
    log.info("欢迎使用 ApiCat🎉")
    log.info("开发团队: 星海码队")
    log.info("项目地址: https://github.com/xinghai-osc/apicat")
    core.register_plugins(plugin_list, app)
    app.run(port=config.get_port(), host=config.get_host())
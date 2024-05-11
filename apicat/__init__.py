from flask import Flask, render_template_string
from . import core,config
import xhlog as log

app = Flask("ApiCat")

@app.route('/')
def docs():
    plugin_docs = {}
    for blueprint_name in app.blueprints:
        if blueprint_name.startswith('plugin'):
            blueprint = app.blueprints[blueprint_name]
            plugin_docs[blueprint_name] = blueprint.get('docs', '')
    
    combined_html = ''
    for plugin_name, docs_content in plugin_docs.items():
        combined_html += f'<h1>欢迎使用 ApiCat 🎉</h1><div>{plugin_name}\n{docs_content}</div>'
    return render_template_string(combined_html)

def start(plugin_list: list):
    log.info("欢迎使用 ApiCat🎉")
    log.info("开发团队: 星海码队")
    log.info("项目地址: https://github.com/xinghai-osc/apicat")
    core.register_plugins(plugin_list,app)
    app.run(port=config.get_port(),host=config.get_host())
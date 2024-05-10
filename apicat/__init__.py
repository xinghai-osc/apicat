from flask import Flask, render_template_string
from . import core
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
        combined_html += f'<h1>API {plugin_name}</h1><div>{docs_content}</div>'
    return render_template_string(combined_html)

def start(plugin_list: list):
    core.register_plugins(plugin_list,app)
    app.run()
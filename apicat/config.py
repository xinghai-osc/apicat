import toml
def get_port():
    path = "./config.toml"
    if toml.load(path)['server']['port'] == None:
        return 80
    else:
        return toml.load(path)['server']['port']
    
def get_host():
    path = "./config.toml"
    if toml.load(path)['server']['host'] == None:
        return "0.0.0.0"
    else:
        return toml.load(path)['server']['host']
    
def get_plugin_cfg(name,type,default=None):
    path = "./config.toml"
    if toml.load(path)[name][type] == None:
        return default
    else:
        return toml.load(path)['server']['host']
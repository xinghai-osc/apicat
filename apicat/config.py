import toml

path = "config.toml"
def get_port():
    if toml.load(path)['website']['port'] == None:
        return 80
    else:
        return toml.load(path)['website']['port']
    
def get_host():
    if toml.load(path)['website']['host'] == None:
        return "0.0.0.0"
    else:
        return toml.load(path)['website']['host']
    
def get_website_name():
    if toml.load(path)['website']['name'] == None:
        return "ApiCat"
    else:
        return toml.load(path)['website']['name']
    
def get_website_url():
    if toml.load(path)['website']['url'] == None:
        return "0.0.0.0"
    else:
        return toml.load(path)['website']['url']
    
def get_plugin_cfg(name,type,default=None):
    if toml.load(path)[name][type] == None:
        return default
    else:
        return toml.load(path)[name][type]
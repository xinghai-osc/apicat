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
        return 80
    else:
        return toml.load(path)['server']['host']
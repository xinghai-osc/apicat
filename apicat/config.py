import toml

path = "config.toml"

def get_port():
    """获取端口，若不存在则返回80"""
    try:
        config = toml.load(path)
        return config['website']['port']
    except KeyError:
        return 80

def get_host():
    """获取主机地址，若不存在则返回'0.0.0.0'"""
    try:
        config = toml.load(path)
        return config['website']['host']
    except KeyError:
        return "0.0.0.0"

def get_website_name():
    """获取网站名称，若不存在则返回'ApiCat'"""
    try:
        config = toml.load(path)
        return config['website']['name']
    except KeyError:
        return "ApiCat"

def get_website_url():
    """获取网站URL，若不存在则返回'0.0.0.0'"""
    try:
        config = toml.load(path)
        return config['website']['url']
    except KeyError:
        return "0.0.0.0"

def get_plugin_cfg(name, type, default=None):
    """获取插件配置，若不存在则返回默认值"""
    try:
        config = toml.load(path)
        return config[name][type]
    except KeyError:
        return default
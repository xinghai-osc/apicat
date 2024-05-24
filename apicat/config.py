import toml
import yaml
import os
import xhlog as log
path = os.getcwd() + "\\config.toml"

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
        if config['website']['url'] == "ApiCat":
            log.warning(f"网站名称未设置！默认为 ApiCat，请前往配置文件修改。")
        return config['website']['url']
    except KeyError:
        return "ApiCat"

def get_website_url():
    """获取网站URL，若不存在则返回'http://localhost'"""
    try:
        config = toml.load(path)
        return config['website']['url']
    except KeyError:
        return "http://localhost"

def get_plugin_cfg(name, type, default=None):
    """获取插件配置，若不存在则返回默认值"""
    with open(path, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return_message =  result[name][type]
    if return_message == None:
        return default
    else:
        return return_message
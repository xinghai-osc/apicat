import sys
import subprocess
import importlib
import xhlog as log

def index():
    help = R"""ApiCat-接口猫
使用：
apicat [命令]
        
命令：
help    显示帮助信息
init    初始化项目
install 安装apicat插件
start   启动项目"""
    try:
        if sys.argv[1] == "help":
            print(help)
        if sys.argv[1] == "init":
            init()
        elif sys.argv[1] == "start":
            start()
    except IndexError:
        print(help)

def init():
    with open("__init__.py","w",encoding="utf-8") as f:
        run_code = R"""from apicat import app,core,config
import xhlog as log
log.info("欢迎使用 ApiCat🎉")
log.info("开发团队: 星海码队")
log.info("项目地址: https://github.com/xinghai-osc/apicat")
core.register_plugins(app)
app.run(port=config.get_port(), host=config.get_host())
        """
        log.info("项目初始化-运行入口")
        f.write(run_code)
    with open("config.toml","w",encoding="utf-8") as f:
        default_config = R"""[website]
name = "ApiCat"
port = 80
host = "0.0.0.0"
url = "http://localhost"
        """
        log.info("项目初始化-默认配置")
        f.write(default_config)
    with open("plugins.yaml","w",encoding="utf-8") as f:
        log.info("项目初始化-插件配置文件")
        f.write("")
        log.info("项目初始化成功！")

def install(pkg_name):
    """安装插件"""
    subprocess.call(f"pip install {pkg_name}", shell=True)
    pkg_import = importlib.import_module(pkg_name)
    with open("plugins.yaml","a",encoding="utf-8") as f:
        f.write(f"{pkg_import.install()}\n")
    log.info(f"插件 {pkg_name} 安装成功！")

def start():
    """启动API"""
    subprocess.call("python __init__.py", shell=True)

if __name__ == '__main__':
    index()
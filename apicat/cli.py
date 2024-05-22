import sys
import subprocess

def index():
    if sys.argv[1] == "help":
        help = R"""
        ApiCat-接口猫
        使用：
        apicat [命令]
        
        命令：
        help    显示帮助信息
        init    初始化项目
        start   启动项目
        """
        print(help)
    if sys.argv[1] == "init":
        init()
    elif sys.argv[1] == "start":
        start()

def init():
    with open("__init__.py","w") as f:
        run_code = R"""from apicat import app
    log.info("欢迎使用 ApiCat🎉")
    log.info("开发团队: 星海码队")
    log.info("项目地址: https://github.com/xinghai-osc/apicat")
    core.register_plugins(app)
    if config.get_website_name() == "ApiCat":
        log.warning(f"网站名称未设置！默认为 ApiCat，请前往配置文件修改。")
    app.run(port=config.get_port(), host=config.get_host())
        """
        f.write(run_code)
    with open("config.toml","w") as f:
        default_config = R"""[website]
name = "ApiCat"
port = 80
host = "0.0.0.0"
url = "http://localhost"
        """
        f.write(default_config)
def start():
    """启动API"""
    subprocess.call("__init__.py", shell=True)

if __name__ == '__main__':
    index()
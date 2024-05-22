from apicat import app,core,config
import xhlog as log
log.info("欢迎使用 ApiCat🎉")
log.info("开发团队: 星海码队")
log.info("项目地址: https://github.com/xinghai-osc/apicat")
core.register_plugins(app)
if config.get_website_name() == "ApiCat":
    log.warning(f"网站名称未设置！默认为 ApiCat，请前往配置文件修改。")
app.run(port=config.get_port(), host=config.get_host())
        
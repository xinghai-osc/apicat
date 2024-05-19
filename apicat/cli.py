import argparse,os,shutil

def cli():
    parser = argparse.ArgumentParser(description='APICAT CLI')
    subparsers = parser.add_subparsers(metavar='CLI命令')

    # 添加子命令，演示没有参数
    one_parser = subparsers.add_parser('init', help='初始化API')
    one_parser.set_defaults(handle=init)

    # 添加子命令，演示有参数
    two_parser = subparsers.add_parser('start', help='启动API')
    two_parser.set_defaults(handle=start)

    # 解析命令
    args = parser.parse_args()
    # 1.第一个命令会解析成handle，使用args.handle()就能够调用
    if hasattr(args, 'handle'):
        # 1.1.其他参数会被解析成args的属性，以命令全称为属性名
        args.handle(args)
    # 2.如果没有handle属性，则表示未输入子命令
    else:
        parser.print_help()

def init(args):
    """初始化API"""
    current_folder = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_local = current_dir + "\\config.toml"
    config = current_folder + "\\config.toml"
    plugin = current_folder + "\\plugin"
    if not os.path.exists(config):
        shutil.copyfile(config_local, config)
    if not os.path.exists(plugin):
        os.makedirs(plugin)
    
def start(args):
    """启动API"""
    
if __name__ == '__main__':
    cli()
# author: LAnHeNG-
# bilibili: https://space.bilibili.com/2119952581
# blog: https://lanhengawa.top

import os
import sys
import time
import subprocess
import json
import shutil
import webbrowser

try:
    import urllib.request  # 需下载
    import requests  # 需下载
    from datetime import datetime
except ImportError:
    os.system('pip install requests')
    os.system('pip install urllib3')
    os.system('pip install datetime')
    import urllib.request  # 需下载
    import requests  # 需下载
    from datetime import datetime


now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d")

if 'logs' not in os.listdir():
    os.mkdir('.\\logs')

log = open('logs\\' + formatted_time + '.log', 'a', encoding='utf-8')

def download(url, file_path):
    urllib.request.urlretrieve(url, file_path)
    print("文件下载完成")


def check_environment(w):
    out_status = os.popen(w).read()
    if w == 'git':
        if 'usage: git' in out_status:
            return False
        else:
            return True
    elif w == 'npm':
        if 'Usage:' in out_status:
            return False
        else:
            return True


def config_change(tag, status):
    # 1. 读取 JSON 文件
    with open('auto_blog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 修改数据
    data[tag] = status

    # 3. 写回文件
    with open('auto_blog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def logs(words):
    log.write('[' + str(datetime.now())[:-7] + '] ' + words + '\n')


def load_blog_config():
    configmts1 = input('请输入config.mts 或 blog-theme.ts的路径(多个文件用";"隔开): ')
    for configmts in configmts1.split(';'):
        if 'config.mts' in configmts:
            with open('auto_blog.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            os.remove(os.getcwd() + '\\' + data['blog_name'] + '\\docs\\.vitepress\\config.mts')
            shutil.copy(configmts, os.getcwd() + '\\' + data['blog_name'] + '\\docs\\.vitepress\\config.mts')
            logs('替换blog内config.mts文件')
        elif 'blog-theme.ts' in configmts:
            with open('auto_blog.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            os.remove(os.getcwd() + '\\' + data['blog_name'] + '\\docs\\.vitepress\\blog-theme.ts')
            shutil.copy(configmts, os.getcwd() + '\\' + data['blog_name'] + '\\docs\\.vitepress\\blog-theme.ts')
            logs('替换blog内blog-theme.ts文件')


def build_blog():
    with open('auto_blog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    os.chdir('.\\' + data['blog_name'])
    os.system('npm run build')
    os.chdir('.\\docs\\.vitepress')
    shutil.make_archive(
        base_name='dist',  # 去掉扩展名
        format='zip',  # 压缩格式
        root_dir='dist'  # 要压缩的文件夹
    )


def print_log(words):
    print(words)
    logs(words)


logs('你当前正运行Ver2.0自动部署Blog 作者:LAnHeNG-')
logs('bilibili: https://space.bilibili.com/2119952581')
logs('blog: https://lanhengawa.top')

git_url = 'https://registry.npmmirror.com/-/binary/git-for-windows/v2.49.0.windows.1/Git-2.49.0-64-bit.exe'
node_url = 'https://cdn.npmmirror.com/binaries/node/v24.0.2/node-v24.0.2-x64.msi'

config_json = {
    'pnpm': 'False',
    'blog_is_created': 'False',
    'custom_blog_name': 'False',
    'blog_name': 'my-blog',
    'backup_location': '',
    'backup_status': "False",
}

if 'auto_blog.json' not in os.listdir():
    # 写入 JSON 文件
    with open('auto_blog.json', 'w', encoding='utf-8') as f:
        json.dump(config_json, f, ensure_ascii=False, indent=4)

with open('auto_blog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
if data['backup_status'] == "False":
    drives = [f"{d}:\\" for d in 'DEFGHIJKLMNOPQRSTUVWXYZABC' if os.path.exists(f"{d}:")]
    config_change('backup_location', drives[0] + 'files_backup\\')
    try:
        os.mkdir(drives[0] + 'files_backup\\')
    except FileExistsError:
        # logs('[Error]在创建备份文件夹时失败')
        # logs('[Error]原因:在创建目录时已经存在该文件夹 导致无法创建')
        # log.write('\n')
        # log.close()
        # sys.exit()
        pass
    config_change('backup_status', 'True')


# only for Windows on version 2.0 #
if sys.platform.startswith('win32'):
    print_log('您当前使用Windows运行自动部署 感谢您使用自动部署')
else:
    print_log('No!目前版本仅支持Windows系统 您可以尝试前往作者blog以寻找更新版本获得Linux/Macos的自动部署!')
    sys.exit()

# Git
if check_environment('git'):
    print_log('检测到git未下载 开始下载...')
    print_log('安装程序下载完毕后会自动打开 请跟随安装程序进行安装')
    download(git_url, 'git_download_program.exe')
    subprocess.run('git_download_program.exe')
    print_log('git安装完毕!')

print_log('git检测完毕')

# Node.js
if check_environment('npm'):
    print_log('检测到Node.js未下载 开始下载...')
    print_log('安装程序下载完毕后会自动打开 请跟随安装程序进行安装')
    download(node_url, 'node_download_program.msi')
    msi_path = "node_download_program.msi"  # 确保路径正确
    subprocess.run(["msiexec", "/i", msi_path])  # 显示安装界面
    print_log('Node.js安装完毕!')

print_log('Node.js检测完毕')

# os - auto_blog.json
if 'changed 1 package' in os.popen('npm install -g pnpm').read():
    # 1. 读取 JSON 文件
    with open('auto_blog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 修改数据
    data['pnpm'] = "True"

    # 3. 写回文件
    with open('auto_blog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
elif 'added 1 package' in os.popen('npm install -g pnpm').read():
    # 1. 读取 JSON 文件
    with open('auto_blog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 修改数据
    data['pnpm'] = "True"

    # 3. 写回文件
    with open('auto_blog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# create blog
with open('auto_blog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if data['blog_name'] not in os.listdir():
    mode = input('您是否想要快速创建blog(即默认项目名为my-blog)或自定义项目名? 是则输入"1" 否则输入"0": ')
    logs('检测到暂未创建blog 开始快速创建')
    if mode == '1':
        logs('用户选择快速创建')
        os.system('npm create @sugarat/theme@latest')
        os.chdir('.\\my-blog')
        commands = [
            'npm install'
        ]

        for cmd in commands:
            subprocess.run(cmd, shell=True)
        os.chdir('..\\')
        config_change('blog_is_created', 'True')
        logs('创建完成')
    else:
        logs('用户选择自定义创建')
        custom_name = input('您选择了自定义项目名! 请输入您的自定义项目名(避免中文字符): ')
        os.system('npm create @sugarat/theme@latest ' + custom_name)
        os.chdir('.\\my-blog')
        commands = [
            'npm install'
        ]

        for cmd in commands:
            subprocess.run(cmd, shell=True)
        os.chdir('..\\')
        config_change('blog_is_created', 'True')
        config_change('custom_blog_name', 'True')
        config_change('blog_name', custom_name)
        logs('创建完成')
else:
    print_log('blog已存在')

while True:
    ctrl = input(
        '请输入操作代码(0为退出 1为替换blog配置文件 2为预览目前编写好的网站 3为构建当前写好的网站生成为zip压缩包): ')
    if ctrl == '0':
        break
    elif ctrl == '1':
        logs('加载配置文件')
        load_blog_config()
    elif ctrl == '2':
        logs('开始预览网站(dev)')
        with open('auto_blog.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        os.chdir('.\\' + data['blog_name'])
        os.system('start npm run dev')
        time.sleep(7)
        webbrowser.open('http://localhost:5173/')
        os.chdir('..\\')
    elif ctrl == '3':
        logs('开始构建网站')
        build_blog()
        logs('网站构建完毕 dist.zip文件位于: ' + os.getcwd())
        os.chdir('..\\')
        os.chdir('..\\')
        os.chdir('..\\')

    # 关闭日志文件
    try:
        drives = [f"{d}:\\" for d in 'ABDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{d}:")]
        os.mkdir(drives[0] + 'files_backup\\' + formatted_time)
    except FileExistsError:
        pass
drives = [f"{d}:\\" for d in 'ABDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{d}:")]
try:
    shutil.copytree(os.getcwd()+'\\my-blog\\docs\\sop', drives[0] + 'files_backup\\' + formatted_time + '\\sop')
except FileExistsError:
    shutil.rmtree(drives[0] + 'files_backup\\' + formatted_time + '\\sop')
    shutil.copytree(os.getcwd() + '\\my-blog\\docs\\sop', drives[0] + 'files_backup\\' + formatted_time + '\\sop')

logs('运行结束 程序正常退出')
log.write('\n')
log.close()

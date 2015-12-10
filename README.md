# wechatrobot
## 环境搭建
1. 首先安装pip 官网http://pypi.python.org
	sudo apt-get install pip
2. 利用pip来安装werobot
	pip install werobot
3. 安装Nginx [Nginx| http://nginx.com/ ]是轻量级、性能强、占用资源少，能很好的处理高并发的反向代理软件。
	sudo apt-get install nginx
	* 配置Nginx，Ubuntu 上配置 Nginx 也是很简单，不要去改动默认的 nginx.conf 只需要将
	/ext/nginx/sites-available/default
替换掉。新建一个default文件：
	server {
    server_name example.com;
    listen 80;

    location / {
        proxy_pass_header Server;
        proxy_redirect off;
        proxy_pass http://127.0.0.1:12233;
    	}
	}
更改配置还需要记得重启一下nginx:	
	sudo service nginx restart
4. 安装 Supervisor
[Supervisor| http://supervisord.org/configuration.html ]可以同时启动多个应用，最重要的是，当某个应用Crash的时候，他可以自动重启该应用，保证可用性。
	sudo apt-get install supervisor
Supervisor 的全局的配置文件位置在：
	/etc/supervisor/supervisor.conf
正常情况下我们并不需要去对其作出任何的改动，只需要添加一个新的`*.conf` 文件放在
	/etc/supervisor/conf.d/
下就可以，那么我们就新建立一个用于启动 my_flask 项目的 uwsgi 的 supervisor 配置 (命名为：my_flask_supervisor.conf)：
	[program:wechat_robot]
	command = python /home/whtsky/robot.py
	user = whtsky
	redirect_stderr = true
	stdout_logfile = /home/whtsky/logs/robot.log
启动服务
	sudo service supervisor start
终止服务
	sudo service supervisor stop

## 
微信机器人WALLE

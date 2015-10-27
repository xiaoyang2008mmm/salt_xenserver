#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.httpserver, os 
import tornado.ioloop 
import tornado.web,redis
import salt.client
from handlers.handlers import HANDLERS , STATIC_PATH , TEMPLATE_PATH

from tornado.options import define, options, parse_command_line

define("port", default=800, help="run on the given port", type=int)
define("redis_host", default="localhost", help="redis server host")
define("redis_db", default="0", help="redis server db")
define("redis_port", default="6386", help="redis server port")
define("redis_password", default="", help="redis server password")


def get_push_vm_list():
    r=redis.Redis(host='localhost', port=6386)
    local = salt.client.LocalClient()
    result_json = local.cmd('push_xenserver', 'cmd.run', ['xe vm-list'],expr_form='nodegroup')
    for key in result_json:
	r.hset("push_xenserver", key, ((result_json[key]).replace(' ',"")).replace('\n\n',""))
    print result_json

class Application(tornado.web.Application):
    def __init__(self):
	handlers=HANDLERS
	settings = {                                                        
       	    "static_path": STATIC_PATH ,
     	    "template_path": TEMPLATE_PATH,
            "debug": True,                                                      
     	    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",                          
	    #"xsrf_cookies":True,                                                  
	}                                                                   
                                                                    

     	tornado.web.Application.__init__(self, handlers, **settings)
	try:
	     pool = redis.ConnectionPool(
	     		host =options.redis_host, port=options.redis_port,
                 	db =options.redis_db,     password=options.redis_password )

             self.db = redis.Redis(connection_pool=pool)                                               
	     if  self.db:
	         print "redis database has connect already ,Please use !"
	except:
	     print  "redis数据库连接不上"
	    	

def main():
    parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.PeriodicCallback(get_push_vm_list, 60000).start()  #1分钟
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

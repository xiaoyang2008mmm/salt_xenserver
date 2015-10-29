#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
import salt.client
import redis
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db
class Index_Handler(BaseHandler):
    def get(self):
	r=redis.Redis(host='localhost', port=6386)
	Xen_Data = r.hgetall("push_xenserver")
        self.render('index.html', Xen_Data= Xen_Data) 






#xe vm-start   vm=1c12db36-7ec3-52ba-6360-5b60c0418534
#xe vm-shutdown  vm=1c12db36-7ec3-52ba-6360-5b60c0418534
#xe vm-reboot   vm=1c12db36-7ec3-52ba-6360-5b60c0418534

class Xen_operation_Handler(BaseHandler):
    '''
    获取xen的uuid和IP
    '''
    def post(self):
        uuid = self.get_argument("uuid")
        xen_ip = self.get_argument("xen_ip")
        action = self.get_argument("action")
        print self.request.arguments
        local = salt.client.LocalClient()
        #result_json = local.cmd_async(xen_ip , 'cmd.run', ['xe vm-%s   vm=%s'%(action,uuid)])
        self.write('%s成功'%action)

#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
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

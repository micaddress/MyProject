# -*- coding: utf-8 -*-

import os
import sae
import web

from weixin import WeixinInterface

urls = (
'/weixin','WeixinInterface'
)
ap_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.renderself(templates_root)

app = web.application(urls,globals()).wsgifunc()
application = sae.create_wsgi_app(app)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
import os
import re
import uuid

import tornado
import tornado.options
from tornado.log import app_log
from tornado.web import RequestHandler

from tornado import gen, web
from tornado import ioloop

def main():

    tornado.options.define('base_path', default='/user/',
            help="Base path for the uptempo service"
    )
    tornado.options.define('port', default=8888,
        help="Port for the main server to listen on"
    )
    tornado.options.define('ip', default=None,
        help="IP for the main server to listen on [default: all interfaces]"
    )

    tornado.options.parse_command_line()
    opts = tornado.options.options

    ioloop = tornado.ioloop.IOLoop().instance()

    static_path = os.path.join(os.path.dirname(__file__), "static")

    settings = dict(
        static_path=static_path,
        cookie_secret=uuid.uuid4(),
        xsrf_cookies=True,
        debug=True,
        autoescape=None,
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        base_path=opts.base_path,
    )

    handlers = [
    ]

    app_log.info("Listening on {}:{}".format(opts.ip or '*', opts.port))
    application = tornado.web.Application(handlers, **settings)
    application.listen(opts.port, opts.ip)
    ioloop.start()

if __name__ == "__main__":
    main()


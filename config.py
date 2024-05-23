#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7169852715:AAH7cj08TU0zRiSE-5mhtWPJpL72mPwQuLY")
    API_ID = int(os.environ.get("API_ID", "24537816"))
    API_HASH = os.environ.get("API_HASH", "d88c4e65689faa570fbc5949468b5c61")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1368753935")

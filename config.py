# Copyright ©️ 2023 Sanila Ranatunga. All Rights Reserved

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 21254911))
    API_HASH = os.environ.get("API_HASH","95e927b3c48ac0af4ebb1c3ffeb0069b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7083760794:AAF_TNGEfpnwxkkKCDoOOj0bLarMMCf8sWo")

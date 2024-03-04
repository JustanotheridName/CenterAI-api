from os import urandom
from base64 import b64encode
import re
import os

class UrlConversionHelper:

    @staticmethod
    def generateRandomUrl(generated_length=int(os.getenv('CONVERTED_LINK_LEN'))):
        random_bytes = b64encode(urandom(64)).decode('utf-8')
        return re.sub(r'\W+', '', random_bytes)[0:min(64, generated_length)]

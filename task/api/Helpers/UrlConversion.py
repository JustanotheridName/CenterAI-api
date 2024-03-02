from os import urandom
from base64 import b64encode
import re

class UrlConversionHelper:

    @staticmethod
    def generateRandomUrl(generated_length=5):
        random_bytes = b64encode(urandom(64)).decode('utf-8')
        return re.sub(r'\W+', '', random_bytes)[0:min(64, generated_length)]

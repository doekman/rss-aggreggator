import logging
import os
import re

import requests

from core.Config import AppConfig


class FetcherUtil:

    @staticmethod
    def fetch(url: str) -> str:
        if AppConfig.is_running_in_gae():
            logging.info(f'Fetching from url {url}')
            result = requests.get(url)
            if result.status_code > 299:
                raise Exception(f'unable to fetch data from {url} - {result.status_code}')
            return result.content
        else:
            logging.warning(f'Retrieving stubbed data locally for {url}')
            if re.match('.*spotgroningen.*', url):
                with open('test/samples/spot/Programma - Spot Groningen.html') as f:
                    return ''.join(f.readlines())
            raise Exception(f'No support for stubbed url {url}')
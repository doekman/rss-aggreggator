import logging
import re

import requests

from app.core.app_config import AppConfig
from app.core.data_fixer import DataFixer


class FetcherUtil:

    @staticmethod
    def fetch(url: str) -> str:
        if AppConfig.is_running_in_gae():
            result = requests.get(url)
            if result.status_code > 299:
                raise Exception(f'unable to fetch data from {url} - {result.status_code}')
            return result.content
        else:
            data_fixer = DataFixer()
            logging.warning(f'Retrieving stubbed data locally for {url}')
            if re.match('.*spotgroningen.*', url):
                with open('tests/samples/spot/Programma - Spot Groningen.html') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*vera-groningen.*page=1.*', url):
                with open('tests/samples/vera-groningen/raw-fetch-0.html') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*vera-groningen.*page=2.*', url):
                with open('tests/samples/vera-groningen/raw-fetch-1.html') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*simplon.nl.*', url):
                with open('tests/samples/simplon-groningen/Simplon.html') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*komoost.nl.*', url):
                with open('tests/samples/oost-groningen/komoost.html') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*tivolivredenburg.nl.*page=1.*', url):
                with open('tests/samples/tivoli-utrecht/ajax-1.js') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*tivolivredenburg.nl.*page=2.*', url):
                with open('tests/samples/tivoli-utrecht/ajax-2.js') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*paradiso.nl.*page=1.*', url):
                with open('tests/samples/paradiso-amsterdam/ajax-1.js') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('.*paradiso.nl.*page=2.*', url):
                with open('tests/samples/paradiso-amsterdam/ajax-2.js') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            elif re.match('https://www.melkweg.nl/.*', url):
                with open('tests/samples/melkweg-amsterdam/small-sample.json') as f:
                    return ''.join([data_fixer.fix(line) for line in f.readlines()])
            raise Exception(f'No support for stubbed url {url}')

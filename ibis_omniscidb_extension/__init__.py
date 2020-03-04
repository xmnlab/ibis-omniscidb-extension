"""Top-level package for Ibis OmniSciDB extension."""

__author__ = """Ivan Ogasawara"""
__email__ = 'ivan.ogasawara@gmail.com'
__version__ = '0.0.1'


from importlib import import_module
import importlib.util
import os
import sys


# force import client package
def setup():
    import pymapd

    ibis_omniscidb_api_path = os.path.join(
        os.path.dirname(pymapd.__path__[0]),
        'ibis', 
        'omniscidb', 
        'api.py'
    )
    
    has_api_client = True
    import_str = '\nfrom ibis.omniscidb import client  # noqa: F401\n'
    file_content = ''

    with open(ibis_omniscidb_api_path, 'r') as f:
        file_content = f.read()
        if not file_content.startswith(import_str):
            has_api_client = False
            file_content = import_str + file_content

    if not has_api_client:
        with open(ibis_omniscidb_api_path, 'w') as f:
            f.write(file_content)

# prepare the environment
setup()

# import here all the extensions
from ibis_omniscidb_extension import ddl

# register here all the extensions
print('registering ddl ...')
ddl.register()

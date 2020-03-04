import os
import pytest

# setup
os.system('python -m ibis_omniscidb_extension')


@pytest.fixture(scope='function')
def db_conf():
    return dict(
        host='localhost',
        port='6274',
        user='admin',
        password='HyperInteractive',
        database='ibis_testing'
    )


@pytest.fixture(scope='function')
def con(db_conf):
    import sys
    # clean environment of any ibis module loaded
    for k in list(sys.modules.keys()):
        if k.startswith('ibis'):
            sys.modules.pop(k)
    # import ibis and return a connection
    import ibis
    return ibis.omniscidb.connect(**db_conf)

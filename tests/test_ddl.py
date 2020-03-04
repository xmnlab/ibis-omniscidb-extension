"""Tests for `ibis_omniscidb_extension` package."""

import pytest


def test_hello(con):
    with pytest.raises(AttributeError):
        con.hello()

    import ibis_omniscidb_extension
    assert con.hello() == 'hello'


def test_bye(con):
    with pytest.raises(AttributeError):
        con.bye()

    import ibis_omniscidb_extension
    assert con.bye() == 'bye'

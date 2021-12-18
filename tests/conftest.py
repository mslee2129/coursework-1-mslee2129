import pytest
from datetime import date
from user import User


@pytest.fixture(scope='module')
def date_of_birth():
    dob = date(year=1997, month=2, day=9)
    yield dob


@pytest.fixture(scope='module')
def password():
    pw = 'password123'
    yield pw

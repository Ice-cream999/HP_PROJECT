import pytest

@pytest.fixture()
def set_up():
    print('\n\nSTART TEST')
    yield
    print('\n\nFINISH TEST')
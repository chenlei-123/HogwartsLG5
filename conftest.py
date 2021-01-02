import pytest


@pytest.fixture(scope="module")
def print_message():
    print("\n【开始计算】")
    yield
    print("\n【计算结束】")

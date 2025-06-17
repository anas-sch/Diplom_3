import time
import pytest

@pytest.fixture
def test_email():
    timestamp = int(time.time())
    return f"test_{timestamp}@example.com"
import pytest

from utils import generate_x_user_data, extract_auth_params

def test_generate_x_user_data():
    result = generate_x_user_data("x_user_data123", "123", "sig", "hash123")
    assert "x_user_data123" in result
    assert "auth_date=123" in result
    assert "signature=sig" in result
    assert "hash=hash123" in result

def test_extract_auth_params():
    url = "auth_date=123&signature=sig&hash=hash123"
    auth_date, signature, hash_value = extract_auth_params(url)
    assert auth_date == "123"
    assert signature == "sig"
    assert hash_value == "hash123"

def test_extract_auth_params_missing_values():
    url = "somethingelse=value"
    auth_date, signature, hash_value = extract_auth_params(url)
    assert auth_date is None
    assert signature is None
    assert hash_value is None

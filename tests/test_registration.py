import pytest
from registration.registration import add_user, initialize_users


def test_add_new_user():
    users = initialize_users()
    result = add_user(users, "new_user", "new_password")
    assert result == "Yeni kullanıcı new_user başarıyla eklendi."
    assert users["new_user"] == "new_password"

def test_add_existing_user():
    users = initialize_users()
    add_user(users, "existing_user", "password")
    result = add_user(users, "existing_user", "new_password")
    assert result == "Kullanıcı zaten mevcut."
    assert users["existing_user"] == "password"
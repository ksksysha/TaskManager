import pytest

from user_manager import UserManager


def test_register_and_authenticate_success() -> None:
    manager = UserManager()
    manager.register_user("student@example.com", "strong123")
    assert manager.authenticate("student@example.com", "strong123")


def test_authenticate_returns_false_for_wrong_password() -> None:
    manager = UserManager()
    manager.register_user("student@example.com", "strong123")
    assert not manager.authenticate("student@example.com", "wrong-pass")


def test_register_user_validates_min_password_length() -> None:
    manager = UserManager()
    with pytest.raises(ValueError):
        manager.register_user("student@example.com", "123")

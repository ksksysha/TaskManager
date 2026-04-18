"""User management and authentication logic."""


class UserManager:
    """Stores users and validates credentials in memory."""

    def __init__(self) -> None:
        self._users: dict[str, str] = {}

    def register_user(self, email: str, password: str) -> None:
        normalized_email = email.strip().lower()
        if not normalized_email:
            raise ValueError("Email must not be empty")
        if len(password) < 6:
            raise ValueError("Password must contain at least 6 characters")
        if normalized_email in self._users:
            raise ValueError("User already exists")
        self._users[normalized_email] = password

    def authenticate(self, email: str, password: str) -> bool:
        normalized_email = email.strip().lower()
        return self._users.get(normalized_email) == password

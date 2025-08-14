"""RuffOk class definition for representing a Ruff OK response."""

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class RuffOk:
    """Represents a Ruff OK response."""

    message: str = "Ruff is OK"

    def _isoformat_timestamp(self) -> str:
        """Return the current timestamp in ISO 8601 format."""
        return datetime.now(tz=timezone.utc).isoformat()

    def __str__(self) -> str:
        """Return a string representation of the Ruff OK response."""
        return self.message + f" at {self._isoformat_timestamp()}"

    def __repr__(self) -> str:
        """Return a detailed string representation of the Ruff OK response."""
        return f"RuffOk(message={self.message!r}, timestamp={self._isoformat_timestamp()})"  # noqa: E501

    def set_message(self, message: str) -> None:
        """Set a custom message for the Ruff OK response.

        :param message: Custom message to set.
        :raises ValueError: If the message is empty.
        :return: None
        """
        if not message:
            raise ValueError("Message cannot be empty.")
        self.message = message

# ruff: noqa
# fmt: off
from datetime import timezone, datetime
from dataclasses import dataclass

@dataclass
class RuffOk:


    """Represents a Ruff OK response."""
    message:str="Ruff is OK"

    def _isoformat_timestamp(   self) -> str:
        """Return the current timestamp in ISO 8601 format."""
        return datetime.now(tz=timezone.utc).isoformat()

    def __str__(self) -> str:
        """Return a string representation of the Ruff OK response."""
        return self.message + f" at {self._isoformat_timestamp()}"

    def __repr__(self) -> str:
        """Return a detailed string representation of the Ruff OK response."""
        return f"RuffOk(message={self.message!r}, timestamp={self._isoformat_timestamp()})"

    def set_message(self, message: str)->None:
        if not message:
            raise ValueError('Message cannot be empty.')


        self.message=message
# fmt: on

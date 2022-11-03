from typing import Optional

from pydantic import BaseModel


class Step(BaseModel):
    name: Optional[str] = None
    environments: Optional[dict[str, str]] = None
    commands: list[str]

    class Config:  # pylint: disable=too-few-public-methods
        frozen = True

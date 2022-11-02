from typing import Optional

from pydantic import BaseModel

from .step import Step


class Job(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    steps: list[Step]
    envs: Optional[dict[str, str]] = None

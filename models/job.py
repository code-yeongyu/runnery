from typing import Optional

from pydantic import BaseModel

from .step import Step


class Job(BaseModel):
    name: Optional[str] = None
    runs_on: Optional[str] = 'local'
    steps: list[Step]
    envs: Optional[dict[str, str]] = None

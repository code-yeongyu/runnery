from typing import Optional

from pydantic import BaseModel, validator

from .step import Step


class Job(BaseModel):
    name: Optional[str] = None
    runs_on: Optional[str] = 'local'
    steps: list[Step]
    envs: Optional[dict[str, str]] = {}

    class Config: # pylint: disable=too-few-public-methods
        frozen = True

    @validator('runs_on')
    @classmethod
    def validate_runs_on(cls, runs_on: str) -> str:
        runs_on = runs_on or 'local'
        if runs_on == 'local':
            return runs_on

        if runs_on.startswith('docker[') and runs_on.endswith(']'):
            return runs_on

        raise ValueError('`runs_on` must be in format `docker[python:3.9]` or `docker[python:3.9-alpine]` or `local`')

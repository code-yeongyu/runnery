from typing import Optional

from pydantic import BaseModel

from .step import Step


class Job(BaseModel):
    name: Optional[str] = None
    docker_image_name: Optional[str] = None
    steps: list[Step]
    envs: Optional[dict[str, str]] = {}

    class Config: # pylint: disable=too-few-public-methods
        frozen = True

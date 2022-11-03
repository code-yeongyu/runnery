from pydantic import BaseModel

from .job import Job


class Workflow(BaseModel):
    jobs: list[Job]

    class Config: # pylint: disable=too-few-public-methods
        frozen = True

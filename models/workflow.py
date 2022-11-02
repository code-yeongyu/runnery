from pydantic import BaseModel

from .job import Job


class Workflow(BaseModel):
    jobs: list[Job]

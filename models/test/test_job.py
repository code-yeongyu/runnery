from typing import Optional

import pytest
from models import Job


class TestJob: # pylint: disable=too-few-public-methods
    class TestRunsOnValidator:
        @pytest.mark.parametrize(
            'allowed_value', ['local', 'docker[python:3.9]', 'docker[python:3.9-alpine]', '', None]
        )
        def test_allow_formatted_text(self, allowed_value: Optional[str]) -> None:
            # when
            job = Job(runs_on=allowed_value, steps = [])

            # then
            assert job.runs_on == allowed_value if allowed_value else 'local'

        @pytest.mark.parametrize(
            'runs_on', ['loc', 'docker[python:3.9', 'doc', 'docker[python:3.9-alpine', 'wrong', 'nothing']
        )
        def test_not_allow_wrong_text(self, runs_on: str) -> None:
            # when & then
            with pytest.raises(ValueError):
                Job(runs_on=runs_on, steps = [])

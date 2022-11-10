import pytest

from models import Job, Step
from runners import LocalJobRunner
from runners.local_job_runner import CommandExecutionError


class TestLocalJobRunner: # pylint: disable=too-few-public-methods
    def test_step_name_matches_result_name(self) -> None:
        # given
        command = 'echo "hello world"'
        step_name = 'echo hello_world'
        job = Job(
            steps=[
                Step(
                    name=step_name,
                    commands=[
                        command,
                    ],
                ),
            ],
        )

        # when
        runner = LocalJobRunner(job)
        result = runner.run()

        # then
        assert result[step_name] == ['hello world\n']

    def test_command_matches_result_name_when_no_step_name(self) -> None:
        # given
        command = 'echo "hello world"'
        job = Job(
            steps=[
                Step(
                    commands=[
                        command,
                    ],
                ),
            ],
        )

        # when
        runner = LocalJobRunner(job)
        result = runner.run()

        # then
        assert result[command] == ['hello world\n']

    def test_wrong_syntax_of_command_should_raise_exception(self) -> None:
        # given
        wrong_command = 'echo "hello world' # closing double-quote not exists
        job = Job(
            steps=[
                Step(
                    commands=[
                        wrong_command,
                    ],
                ),
            ],
        )

        # when & then
        with pytest.raises(CommandExecutionError):
            LocalJobRunner(job).run()

    def test_envs_setted_correctly(self) -> None:
        # given
        command = 'echo "$TEST_ENV"'
        job = Job(
            envs={
                'TEST_ENV': 'the env works',
            },
            steps=[
                Step(
                    commands=[
                        command,
                    ],
                ),
            ],
        )

        # when
        runner = LocalJobRunner(job)
        result = runner.run()

        # then
        assert job.envs is not None
        assert result[command] == [job.envs['TEST_ENV'] + '\n']

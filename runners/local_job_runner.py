import os
import subprocess

from models import Job, Step


class CommandExecutionError(Exception):
    command: str
    stderr: str
    return_code: int


    def __init__(self, command: str, stderr: str, return_code: int):
        self.command = command
        self.stderr = stderr
        self.return_code = return_code

class LocalJobRunner:
    job: Job
    is_done = True

    def __init__(self, job: Job):
        self.job = job

    def run(self) -> dict[str, list[str]]:
        self._set_environment_variables()

        steps_result: dict[str, list[str]] = {}
        for step in self.job.steps:
            result = self._run_step(step)
            step_name = step.name or ''.join(step.commands)
            steps_result[step_name] = result

        return steps_result

    def _set_environment_variables(self) -> None:
        envs = self.job.envs or {}
        for name, value in envs.items():
            os.environ[name] = value

    def _run_step(self, step: Step) -> list[str]:
        return [self._run_command(command) for command in step.commands]

    def _run_command(self, command: str) -> str:
        try:
            proc = subprocess.run(command, shell=True, check=True, capture_output=True)
            return proc.stdout.decode('utf-8')
        except subprocess.CalledProcessError as exception:
            stderr = exception.stderr.decode('utf-8')
            return_code = exception.returncode
            raise CommandExecutionError(command, stderr, return_code) from exception

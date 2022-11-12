from models import Job


class TestJob: # pylint: disable=too-few-public-methods
    class TestIsDocker:
        def test_is_docker_true__when_docker_image_name_is_not_none(self) -> None:
            # when
            job = Job(docker_image_name='test', steps=[])

            # then
            assert job.is_docker is True

        def test_is_docker_false__when_docker_image_name_is_none(self) -> None:
            # when
            job = Job(docker_image_name=None, steps=[])

            # then
            assert job.is_docker is False

        def test_is_docker_false__when_docker_image_name_is_not_given(self) -> None:
            # when
            job = Job(steps=[])

            # then
            assert job.is_docker is False

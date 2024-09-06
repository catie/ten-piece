import os
from typing import Optional
from pydantic import BaseModel


class ServiceEnvironment(BaseModel):
    stage: str
    aws_account_id: str
    aws_region: str

    @staticmethod
    def _load_or_nothing_(env_var: str) -> Optional[str]:
        return os.environ.get(env_var, None)

    def load_or_nothing(self, env_var: str) -> Optional[str]:
        return self._load_or_nothing_(env_var=env_var)

    @staticmethod
    def _load_or_die_(env_var: str) -> str:
        value = os.environ.get(env_var, None)
        if value is None:
            raise ValueError(f"Unable to load environment variable {env_var}")
        return value

    def load_or_die(self, env_var: str) -> str:
        return self._load_or_die_(env_var=env_var)

    @classmethod
    def load(cls) -> "ServiceEnvironment":
        return ServiceEnvironment(
            stage=cls._load_or_die_("STAGE"),
            aws_account_id=cls._load_or_die_("AWS_ACCOUNT_ID"),
            aws_region=cls._load_or_die_("AWS_REGION"),
        )


# Acts as a singleton object
_SERVICE_ENVIRONMENT = ServiceEnvironment.load()


def get_service_environment() -> ServiceEnvironment:
    return _SERVICE_ENVIRONMENT

import os
from typing import Final

from dotenv import load_dotenv

from src.utils.exceptions.configurate_exceptions import EnvDependNotFound

load_dotenv()


def get_env_var(var_name: str) -> str:
    """
    :raise EnvDependNotFound if value in None
    :param var_name: Env var name
    :return: Var value by name
    """
    value: str | None = os.getenv(var_name)
    if value is None:
        raise EnvDependNotFound(var_name)
    else:
        return value

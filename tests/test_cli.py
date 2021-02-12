import sys
import pytest
from .helpers import config_dict, clear_config


def test_override_cli(cli_args, config_dict):
    set_sys_argv(cli_args)
    from fig import Config as C

    assert False


@pytest.fixture()
def cli_args():
    return ["--fruit_apples=[4,5,6]"]


def set_sys_argv(argvs):
    for argv in argvs:
        sys.argv.append(argv)

import pytest
from .helpers import config_dict, defaults_file_path, clear_config


def test_defaults(defaults_file_path, config_dict):
    """Test that defaults load both from the standard defaults_file_path and a custom
    file path using the patch."""
    import os, shutil

    shutil.copyfile(defaults_file_path, "defaults.yaml")

    from fig import Config as C

    assert hasattr(C, "fruit_apples")
    assert hasattr(C, "fruit_orange_colour")
    assert hasattr(C, "fruit_orange_quantity")
    assert hasattr(C, "msg")
    assert C.msg == config_dict["msg"]
    assert C.fruit_apples == config_dict["fruit"]["apples"]
    os.remove("defaults.yaml")
    clear_config(C, config_dict)

    C.load_defaults_from(defaults_file_path)
    assert hasattr(C, "fruit_apples")
    assert hasattr(C, "fruit_orange_colour")
    assert hasattr(C, "fruit_orange_quantity")
    assert hasattr(C, "msg")
    assert C.msg == config_dict["msg"]
    assert C.fruit_apples == config_dict["fruit"]["apples"]
    clear_config(C, config_dict)


def test_default_override(
    defaults_file_path, override_yaml_file_path, override_config_dict
):
    """Test that the load_yaml factory function overrides the default configuration
    where there is overlap.
    """
    from fig import Config as C

    C.load_defaults_from(defaults_file_path)
    C.load_yaml(override_yaml_file_path)

    assert hasattr(C, "fruit_pears")
    assert C.fruit_pears == override_config_dict["fruit"]["pears"]
    clear_config(C, override_config_dict)


@pytest.fixture()
def override_config_dict():
    return {
        "fruit": {"pears": [2, 3, 4], "orange": {"colour": "orange", "quantity": 2}},
        "msg": "jet fuel can't burn steel beams",
    }


@pytest.fixture()
def override_yaml_file_path(tmpdir_factory, override_config_dict):
    import yaml

    fn = tmpdir_factory.mktemp("data").join("config.yaml")
    with open(str(fn), "w") as f:
        f.write(yaml.dump(override_config_dict))

    return fn

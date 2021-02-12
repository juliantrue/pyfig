import pytest
from .helpers import config_dict, clear_config


def test_e2e_yaml(yaml_file_path, config_dict):
    """Test that loading a yaml file does whats expected"""
    from fig import Config as C

    C.load_yaml(yaml_file_path)

    assert hasattr(C, "fruit_apples")
    assert hasattr(C, "fruit_orange_colour")
    assert hasattr(C, "fruit_orange_quantity")
    assert hasattr(C, "msg")
    assert C.msg == config_dict["msg"]
    assert C.fruit_apples == config_dict["fruit"]["apples"]


@pytest.fixture()
def yaml_file_path(tmpdir_factory, config_dict):
    import yaml

    fn = tmpdir_factory.mktemp("data").join("config.yaml")
    with open(str(fn), "w") as f:
        f.write(yaml.dump(config_dict))

    return fn


def test_e2e_yaml_elsewhere(config_dict):
    """Test that the loaded yaml file from above persists the config across
    multiple import statements. If this is called out of order, it will fail."""
    from fig import Config as C

    assert hasattr(C, "fruit_apples")
    assert hasattr(C, "fruit_orange_colour")
    assert hasattr(C, "fruit_orange_quantity")
    assert hasattr(C, "msg")
    assert C.msg == config_dict["msg"]
    assert C.fruit_apples == config_dict["fruit"]["apples"]
    clear_config(C, config_dict)


def test_e2e_toml(toml_file_path):
    """Test that loading a toml file does whats expected"""
    from fig import Config as C

    C.load_toml(toml_file_path)
    assert hasattr(C, "fruit_apples")
    assert hasattr(C, "fruit_orange_colour")
    assert hasattr(C, "fruit_orange_quantity")
    assert hasattr(C, "msg")
    assert C.msg == config_dict["msg"]
    assert C.fruit_apples == config_dict["fruit"]["apples"]
    clear_config(C, config_dict)


@pytest.fixture()
def toml_file_path(tmpdir_factory, config_dict):
    import toml

    fn = tmpdir_factory.mktemp("data").join("config.yaml")
    with open(str(fn), "w") as f:
        f.write(toml.dumps(config_dict))

    return fn

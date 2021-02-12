import pytest


@pytest.fixture()
def config_dict():
    return {
        "fruit": {"apples": [1, 2, 3], "orange": {"colour": "orange", "quantity": 2}},
        "msg": "jet fuel can't burn steel beams",
    }


@pytest.fixture()
def defaults_file_path(tmpdir_factory, config_dict):
    import yaml

    fn = tmpdir_factory.mktemp("data").join("defaults.yaml")
    with open(str(fn), "w") as f:
        f.write(yaml.dump(config_dict))

    return fn


def clear_config(C, config_dict):
    flat_dict = C._flatten_dict(config_dict)
    for k in flat_dict:
        delattr(C, k)

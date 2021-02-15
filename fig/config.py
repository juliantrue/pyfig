import os
import json
import yaml


class Config(object):
    _loaded_config = {}

    @classmethod
    def _load_defaults(cls):
        cls.load_defaults_from("defaults.yaml")

    @classmethod
    def load_defaults_from(cls, path_to_yaml_file):
        """If there is a defaults.yaml file, load it."""
        if os.path.exists(path_to_yaml_file):
            cls.load_yaml(path_to_yaml_file)
        else:
            print("no defaults.yaml found")

    @classmethod
    def load_yaml(cls, path_to_yaml_file):
        if not os.path.exists(path_to_yaml_file):
            raise FileExistsError(f"Cannot find file {path_to_yaml_file}")

        with open(path_to_yaml_file, "rb") as f:
            override_config_dict = yaml.safe_load(f)

        cls._flatten_dict_and_setattr(override_config_dict)
        cls._loaded_config.update(override_config_dict)

    @classmethod
    def load_toml(cls, path_to_toml_file):
        raise NotImplementedError("TODO")

    @classmethod
    def _flatten_dict_and_setattr(cls, dictionary):
        flattened_dict = cls._flatten_dict(dictionary)
        for k, v in flattened_dict.items():
            setattr(cls, k, v)

    @classmethod
    def _flatten_dict(cls, dd, separator="_", prefix=""):
        return (
            {
                prefix + separator + k if prefix else k: v
                for kk, vv in dd.items()
                for k, v in cls._flatten_dict(vv, separator, kk).items()
            }
            if isinstance(dd, dict)
            else {prefix: dd}
        )

    @classmethod
    def _load_env_vars(cls):
        raise NotImplementedError("TODO")

    @classmethod
    def _load_cli_args(cls):
        raise NotImplementedError("TODO")

    @classmethod
    def as_dict(cls):
        return cls._loaded_config

    @classmethod
    def as_json(cls, **kwargs):
        return json.dumps(cls._loaded_config, **kwargs)

    @classmethod
    def show(cls):
        print(cls.as_json(sort_keys=False, indent=4))

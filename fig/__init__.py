from .config import Config


# Perform setup steps according to precedence
Config._load_defaults()
# Config._load_env_vars()
# Config._parse_cli_args()

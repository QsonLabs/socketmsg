"""config.py: config object for socketmsg"""
import os
import yaml


class Config(object):
    """socketmsg config"""
    def __init__(self, uri):
        """requires a config URI to support loading configs from multiple sources"""
        self.config = self.load(uri)

    def load():
        """look up a config based on the uri"""
        pass


def default_config():
    """
    Returns the default options rsformat will use
    """
    return {
        "log_level": "DEBUG"
    }


def parse_yaml(confpath):
    """
    Loads yaml from a config file path does not support arbitrary code in yaml
    """
    try:
        filepath = os.path.abspath(confpath)
    except Exception:
        raise TypeError("config not string type required to specify path: %s" % confpath)
    with open(filepath, 'r') as f:
        configs = yaml.safe_load(f)
    return configs

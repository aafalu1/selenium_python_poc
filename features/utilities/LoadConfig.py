import os
from configparser import ConfigParser


class LoadConfig:
    def __init__(self):
        self.directory = "configurator"
        self.file_name = "config.ini"

    def string_property_config(self, section, key):
        filepath = self.get_file_path()
        config = self._get_config_parser(filepath)
        return config.get(section, key)

    def int_property_config(self, section, key):
        filepath = self.get_file_path()
        config = self._get_config_parser(filepath)
        value = config.get(section, key)
        if value.isdigit():
            return int(value)
        else:
            raise Exception(f"The value for section '{section}' and key '{key}' is not a valid integer.")

    def boolean_property_config(self, section, key):
        filepath = self.get_file_path()
        config = self._get_config_parser(filepath)
        return config.getboolean(section, key)

    def get_file_path(self):
        proj_dir = os.getcwd()
        config_dir = os.path.join(proj_dir, self.directory)
        file_path = os.path.join(config_dir, self.file_name)
        return file_path

    def _get_config_parser(self, filepath):
        config = ConfigParser()
        config.read(filepath)
        return config

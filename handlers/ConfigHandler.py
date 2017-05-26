import sys
import os
import yaml


class ConfigHandler:
    # Le o arquivo de configuração na raiz
    config_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../config.yaml")
    config_file_stream = open(config_path, "r")
    config = yaml.load(config_file_stream)

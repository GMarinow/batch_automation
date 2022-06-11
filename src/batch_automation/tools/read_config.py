import os
import sys
import yaml
import json
import csv

class StringConcatinator(yaml.YAMLObject):
    """
    Class used to create custom yaml constructor.
    """
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!join'
    @classmethod
    def from_yaml(cls, loader, node):
        seq = loader.construct_sequence(node)
        return ''.join([str(i) for i in seq])

class Config():
    """
        Class used to read the data from config files.
        Supported extension are yml/json.
    """
    def __init__(self, dir, filename, ext='yml', reader=yaml.safe_load):
        super().__init__()
        self.ext = ext
        self.filename = filename
        self.reader = reader
        self.dir = dir

    def readSettings(self):
        """
            Returns: The content of the provided file.
        """
        for root, dirs, files in os.walk(self.dir):
            if (f'{self.filename}.{self.ext}') in files:
                filepath = (os.path.join(root, f'{self.filename}.{self.ext}'))
                with open(filepath) as SettingsFile:
                    SettingsFile = self.reader(SettingsFile)
                    return SettingsFile
        else:
            sys.exit(f'File {self.filename} does not exist!')
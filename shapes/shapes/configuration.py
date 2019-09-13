import os
import yaml

class config():

    instanceType = ''
    config = ''
    BASE_DIR = ''

    def __init__(self, instance = '/env.yml'):
        self.instanceType = "/var/www/html/shapes" + instance
        self.parseConfiguration()

    def parseConfiguration(self):
        with open(self.instanceType, 'r') as configfile:
            self.config = yaml.load(configfile)
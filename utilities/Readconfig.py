
import pytest
from configparser import ConfigParser



def read_config(category,key):
    config= ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,key)

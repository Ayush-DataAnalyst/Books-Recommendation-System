import yaml
import sys 
from books_recommendation_system.exception.exception_handler import AppException


def read_yaml_file(file_path:str)->dict:
    # Reads a Yaml File
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e
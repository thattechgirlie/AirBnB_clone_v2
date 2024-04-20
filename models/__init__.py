#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

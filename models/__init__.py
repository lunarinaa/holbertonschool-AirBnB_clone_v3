#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from dotenv import load_dotenv

load_dotenv()

DB_TYPE = os.environ['HBNB_TYPE_STORAGE']

if DB_TYPE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
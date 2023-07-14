#!/usr/bin/python3
"""
Magic method initializing the models package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

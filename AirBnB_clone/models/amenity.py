#!/usr/bin/env python3
"""
Module defines State class that inherits BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines the State"""
    name = ""
    def __init__(self):
        """Initialize class"""
        super().__init__()

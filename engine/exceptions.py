"""
Author:     Chris Knowles
File:       exceptions.py
Version:    1.0.0
Notes:      Custom exception classes utilised by other modules
"""
# Imports


# Classes
class InsufficientCardsError(Exception):
    """
    Exception class to indicate an operation has been performed where there are insufficient
    playing cards available to complete this operation - class variables:
        none
    """
    def __init__(self, msg):
        super().__init__(msg)

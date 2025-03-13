"""Manages a history of mathematical operations."""
from typing import List, Optional
from calculator.calculation import OperationRecord

class OperationHistory:
    _history = []  # Store operations as a class attribute

    @classmethod
    def add_record(cls, record):
        cls._history.append(record)

    @classmethod
    def get_all_records(cls):
        return cls._history

    @classmethod
    def clear_records(cls):
        """Clears all stored operation records."""
        cls._history = []

    @classmethod
    def get_last_record(cls):
        """Gets the last operation record."""
        if cls._history:
            return cls._history[-1]
        return None

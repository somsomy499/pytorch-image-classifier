"""Pytest configuration and fixtures."""
import pytest
import tempfile
import os

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def sample_config():
    return {
        "model": "default",
        "version": "1.0.0",
        "debug": False,
        "max_retries": 3,
    }

@pytest.fixture
def sample_data():
    return [
        {"id": 1, "name": "Alice", "score": 0.95},
        {"id": 2, "name": "Bob", "score": 0.87},
        {"id": 3, "name": "Charlie", "score": 0.92},
    ]

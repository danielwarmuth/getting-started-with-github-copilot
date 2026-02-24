import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Example test for root endpoint using AAA pattern

def test_root_endpoint():
    # Arrange
    expected_status = 307  # Redirect
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == expected_status
    assert response.headers["location"].endswith(expected_location)

# Add more tests for other endpoints below, following AAA pattern

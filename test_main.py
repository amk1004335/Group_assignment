# test_main.py
# // MY NAME
import pytest
from main import collatz_sequence

def test_collatz_even_number():
    # Arrange
    number = 12
    expected = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    
    # Act
    result = collatz_sequence(number)
    
    # Assert
    assert result == expected

def test_collatz_odd_number():
    # Arrange
    number = 5
    expected = [5, 16, 8, 4, 2, 1]
    
    # Act
    result = collatz_sequence(number)
    
    # Assert
    assert result == expected

def test_collatz_invalid_input():
    # Arrange
    number = -3
    
    # Act & Assert
    with pytest.raises(ValueError):
        collatz_sequence(number)  # <- no extra parenthesis here

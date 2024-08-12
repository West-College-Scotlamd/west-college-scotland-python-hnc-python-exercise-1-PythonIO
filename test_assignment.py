import io
import pytest

def test_greeting_sarah(monkeypatch, capsys):
    # Use monkeypatch to mock input
    monkeypatch.setattr('builtins.input', lambda _: 'Sarah')
    
    # Import the script to execute it
    import assignment
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check the output
    assert captured.out.strip() == "Hello Sarah"

#!/bin/bash
# Setup script for Python Abstract Obfuscator

echo "Enabling permissions..."
chmod +x abstract_obfuscator.py

echo "Checking Python 3..."
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed."
    echo "Usage: python3 abstract_obfuscator.py"
else
    echo "Error: Python 3 is not installed. Please install it first."
fi

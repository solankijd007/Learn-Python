#!/bin/bash
# Quick Start Script for Load Testing

echo "🚀 FastAPI Load Testing - Quick Start"
echo "======================================"
echo ""

# Check if server is running
if ! curl -s http://localhost:8000/ > /dev/null 2>&1; then
    echo "❌ Error: FastAPI server is not running!"
    echo ""
    echo "Please start the server first:"
    echo "  Terminal 1: source venv/bin/activate && uvicorn main:app --reload"
    echo ""
    exit 1
fi

echo "✓ Server is running"
echo ""

# Activate virtual environment and run test
source venv/bin/activate
python load_test.py

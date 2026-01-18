#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src

echo "🚀 Starting AstraGuard AI Demo..."
echo "Press Ctrl+C to stop."

# Check for .env
if [ ! -f .env ]; then
    echo "⚠️ .env file not found. Copying .env.example..."
    cp .env.example .env
fi

# Run the demo
python3 demo/run_pipeline.py

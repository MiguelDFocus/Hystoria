#!/bin/bash
# AI History Blog - Setup Script
# Helps you get started quickly and securely

set -e

echo "🚀 Welcome to AI History Blog Setup!"
echo "======================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt
echo "✅ Dependencies installed"

# Check if .env exists
if [ ! -f ".env" ]; then
    echo ""
    echo "🔐 Setting up environment configuration..."
    echo "======================================"
    echo "You need to create a .env file with your OpenAI API key."
    echo ""
    echo "📋 Steps:"
    echo "1. Get your API key from: https://platform.openai.com/api-keys"
    echo "2. Copy env.example to .env: cp env.example .env"
    echo "3. Edit .env and add your API key"
    echo ""
else
    echo "✅ .env file already exists"
fi

# Check git status
if [ -d ".git" ]; then
    echo ""
    echo "🔍 Checking git security..."
    if git status --porcelain | grep -q ".env"; then
        echo "❌ WARNING: .env file is tracked by git!"
        echo "   This is a security risk. Please remove it:"
        echo "   git rm --cached .env"
        echo "   git commit -m 'Remove .env from tracking'"
    else
        echo "✅ .env file is properly ignored by git"
    fi
else
    echo "ℹ️  Git repository not initialized yet"
fi

# Create content directory
mkdir -p content
echo "✅ Content directory ready"

echo ""
echo "🎉 Setup completed successfully!"
echo "================================"

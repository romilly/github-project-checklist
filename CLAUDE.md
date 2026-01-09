# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python script that fetches and analyzes GitHub repository metrics (issues, pull requests, stars, forks) via the GitHub API. Based on a project evaluation checklist.

## Commands

```bash
# Activate virtual environment (always do this first)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python src/evaluation.py
```

## Configuration

The script requires a GitHub personal access token in a `.env` file:
```
GITHUB_TOKEN=your_token_here
```

Without a token, API requests are limited to 60/hour. With a token, the limit is 5,000/hour.

## Code Structure

- `src/evaluation.py` - Main script with `get_github_project_info(owner, repo)` function
- `notebooks/spike.ipynb` - Jupyter notebook for testing/experimentation

## Key Dependencies

- `requests` - GitHub API calls
- `pandas` - Date/time calculations for PR metrics
- `python-dotenv` - Loading `.env` configuration

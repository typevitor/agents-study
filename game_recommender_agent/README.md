# Game Recommender Agent

An intelligent AI agent system that asks users a few targeted questions about their gaming preferences, performs deep research to find matching games, and optionally delivers recommendations via email (Mailtrap) through agent handoff.

## Overview

The Game Recommender Agent follows a simple but effective workflow:
1. **Asks a few questions** to understand basic user gaming preferences
2. **Performs deep research** to find games that match the user's answers
3. **Asks if user wants email delivery** of the recommendations
4. **Hands off to email sender agent** if user requests email delivery

## Features

- **Minimal Questioning**: Quick preference gathering with just a few targeted questions
- **Deep Research Engine**: Comprehensive research based on user answers
- **Optional Email Delivery**: Users can choose to receive recommendations via email
- **Agent Handoff**: Seamless transition to specialized email sender agent
- **Research-Driven Results**: Thorough game discovery based on user responses

## Architecture

### Core Components

- **[`deep_research.py`](deep_research.py)**: Main research engine that finds games based on user answers
- **Question System**: Asks a few key questions to gather user preferences
- **Email Sender Agent**: Handles email delivery when requested (located in [`custom_agents/`](custom_agents/))
- **Research Tools**: Tools for comprehensive game research (located in [`tools/`](tools/))

### Directory Structure

```
game_recommender_agent/
├── __init__.py              # Package initialization
├── deep_research.py         # Main research engine
├── README.md               # This documentation
├── custom_agents/          # Specialized AI agents
│   └── [agents_module].py     # Agents Definition
└── tools/                  # Research tools
    └── [tool modules]      # Game search and analysis tools
```

## Installation

1. **Prerequisites**:
   ```bash
   python >= 3.12
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment setup**:
   Create a `.env` file with required API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   # Email service credentials if using email delivery
   MAILTRAP_API_HOST=your_email_service_key
   MAILTRAP_API_USER=host
   MAILTRAP_API_PASS=password
   ```

## Usage

### Basic Workflow

```python
from game_recommender_agent.deep_research import game_recommender

# Initialize and start the session
game_recommender.start_session()
```

### How It Works

1. **Question Phase**: System asks a few key questions
   - Example: "What type of games do you enjoy?"
   - Example: "What platform do you play on?"
   - Example: "Do you prefer single-player or multiplayer?"

2. **Research Phase**: Deep research triggered automatically
   ```python
   # System uses answers to perform comprehensive research
   research_results = deep_research.find_games(user_answers)
   ```

3. **Email Option**: System asks about email delivery
   - "Would you like these recommendations sent to your email?"

4. **Agent Handoff**: If user says yes
   ```python
   # Hand off to email sender agent
   email_agent.send_recommendations(research_results, user_email)
   ```

## Core Functionality

### Question System
The system asks just a few strategic questions to gather:
- **Game preferences** (genres, styles)
- **Platform availability**
- **Gaming preferences** (single/multiplayer, etc.)

### Deep Research Engine
After collecting answers, the system:
- **Analyzes user responses** to understand preferences
- **Performs comprehensive research** to find matching games
- **Generates detailed recommendations** based on research findings

### Email Integration
When users request email delivery:
- **Prompts for email address**
- **Hands off to email sender agent**
- **Delivers formatted recommendations** via email

## Example Session Flow

```
1. System: "What type of games do you enjoy most?"
   User: "RPGs and strategy games"

2. System: "What platform do you play on?"
   User: "PC and Nintendo Switch"

3. System: "Do you prefer single-player or multiplayer?"
   User: "Single-player with good storylines"

4. [System performs deep research based on answers]

5. System: [Presents game recommendations]
   "Based on your preferences, here are some games you might enjoy..."

6. System: "Would you like these recommendations sent to your email?"
   User: "Yes, please"

7. System: "What's your email address?"
   User: "user@example.com"

8. [System hands off to email sender agent]
   Email agent sends formatted recommendations
```
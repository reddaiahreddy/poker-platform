# Multiplayer Texas Hold’em Poker Platform (Real-Time WebSocket Game Engine)

# Project Description
A real-time multiplayer poker platform built using FastAPI, WebSockets, and Python.

This project simulates a Texas Hold’em poker engine where players can:
- Join a table from different locations
- Play real-time poker games
- Place bets, call, fold
- Play synchronized game rounds

The backend is fully event-driven and uses WebSockets for real-time communication.

# TECH STACK
- Python
- FastAPI
- WebSockets
- Object-Oriented Design
- Real-time Event System


# ARCHITECTURE
Frontend (HTML/JS)
        ↓
WebSocket Layer (FastAPI)
        ↓
Game Service Layer
        ↓
Poker Engine (Table, Player, Deck)
        ↓
Game State Broadcast

# Features Implemented
- Real-time WebSocket communication
- Multiplayer join system
- Poker deck & shuffle system
- Player model with chips & cards
- Betting system (bet, call, fold)
- Turn-based system
- Game state management
- Round progression (pre-flop, flop, turn, river)

# How To Run
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
open frontend/test.html using Live Server

# Sample Actions
- join game
- start game
- bet 50
- call
- fold

# Future Improvements
- Hand ranking system (winner detection)
- Authentication system
- Multiple tables support
- Database persistence (PostgreSQL)
- Deployment using Docker + AWS
- UI with React


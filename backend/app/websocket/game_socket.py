from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket.connection_manager import ConnectionManager
from app.services.game_service import GameService
import json

router = APIRouter()
manager = ConnectionManager()
game = GameService()


# -----------------------------
# MAIN WEBSOCKET ENDPOINT
# -----------------------------
@router.websocket("/ws/table")
async def table_socket(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            action = message.get("action")
            user = message.get("user")

            response = None

            # -----------------------------
            # PLAYER JOIN
            # -----------------------------
            if action == "join":
                response = game.add_player(
                    player_id=user,
                    name=user
                )

            # -----------------------------
            # START GAME
            # -----------------------------
            elif action == "start":
                response = game.start_game()

            # -----------------------------
            # BET
            # -----------------------------
            elif action == "bet":
                response = game.table.bet(
                    player_id=user,
                    amount=message.get("amount", 0)
                )
                game.table.advance_if_ready()

            # -----------------------------
            # CALL
            # -----------------------------
            elif action == "call":
                response = game.table.call(player_id=user)
                game.table.advance_if_ready()

            # -----------------------------
            # FOLD
            # -----------------------------
            elif action == "fold":
                response = game.table.fold(player_id=user)
                game.table.advance_if_ready()

            # -----------------------------
            # GET STATE (DEBUG / UI SYNC)
            # -----------------------------
            elif action == "state":
                response = game.get_state()

            # -----------------------------
            # BROADCAST RESPONSE
            # -----------------------------
            if response:
                await manager.broadcast(response)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast({
            "event": "player_left"
        })
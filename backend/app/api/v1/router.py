from fastapi import APIRouter
from app.api.v1.endpoints import health
from app.websocket.game_socket import router as game_socket_router

router = APIRouter()

router.include_router(health.router)
router.include_router(game_socket_router)

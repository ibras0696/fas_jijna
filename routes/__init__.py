#  Основной роутер для подключение других роутеров
from fastapi import APIRouter

from .items import router as items_router
from .users import router as user_router

router = APIRouter()

# Можно подключить другие роутеры
router.include_router(items_router, prefix="/items", tags=["items"])
router.include_router(user_router, prefix="/users", tags=["users"])

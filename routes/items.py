from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()


templates = Jinja2Templates(directory="templates")


items = {
    1: {"name": " Первое значение", "description": "Это первое значение."},
    2: {"name": "Второе значение", "description": "Это второе значение."},
    3: {"name": "Третье значение", "description": "Это третье значение."},
    4: {"name": "Четвертое значение", "description": "Это четвертое значение."},
    5: {"name": "Пятое значение", "description": "Это пятое значение."},
    6: {"name": "Шестое значение", "description": "Это шестое значение."},
    7: {"name": "Седьмое значение", "description": "Это седьмое значение."},
    8: {"name": "Восьмое значение", "description": "Это восьмое значение."},
    9: {"name": "Девятое значение", "description": "Это девятое значение."},
    10: {"name": "Десятое значение", "description": "Это десятое значение."},
}


# Роутер для подгрузки данных из шаблона
@router.get("/{item_id}")
def read_item(request: Request, item_id: int):
    item = items.get(item_id)
    if item:
        return templates.TemplateResponse("item.html", {"request": request, "item": item})
    return {"error": "Item not found"}

# Подобие подгрузки циклом карточек товаров 
@router.get("/")
def read_items(request: Request):
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI, APIRouter, Request
from random import random, randrange, randint
service_router = APIRouter()


templates = Jinja2Templates(directory="templates")
@service_router.get("/light_on",response_class=HTMLResponse)
async def light_on(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Свет включен"})


@service_router.get("/light_off",response_class=HTMLResponse)
async def light_off(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Свет выключен"})


@service_router.get("/near_battery_station",response_class=HTMLResponse)
async def near_battery_station(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Ближайшая зарядкная станция расположена: ул Адоратского 79"})


@service_router.get("/open_door",response_class=HTMLResponse)
async def open_door(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Открыть двери"})


@service_router.get("/close_door",response_class=HTMLResponse)
async def close_door(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Закрыть двери"})


@service_router.get("/get_location_car",response_class=HTMLResponse)
async def get_location_car(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Ваша машина находится в Казани"})


@service_router.get("/get_charge",response_class=HTMLResponse)
async def get_charge(request: Request):
    charge = random.randint(1, 100)
    return templates.TemplateResponse("home.html", {"request": request, "text": f"Уровень зарядки: {charge}"})


@service_router.get("/on_near_light",response_class=HTMLResponse)
async def on_near_light(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Ближний свет включен"})


@service_router.get("/off_near_light",response_class=HTMLResponse)
async def off_near_light(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Ближний свет выключен"})


@service_router.get("/on_far_light",response_class=HTMLResponse)
async def on_far_light(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Дальний свет включен"})


@service_router.get("/off_far_light",response_class=HTMLResponse)
async def off_far_light(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Дальний свет выключен"})


@service_router.get("/open_trunk",response_class=HTMLResponse)
async def open_trunk(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Багажник открыт"})


@service_router.get("/close_trunk",response_class=HTMLResponse)
async def close_trunk(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Багажник закрыт"})


@service_router.get("/on_conditioner",response_class=HTMLResponse)
async def on_conditioner(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Кондиционер включен"})


@service_router.get("/off_conditioner",response_class=HTMLResponse)
async def off_conditioner(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Кондиционер выключен"})


@service_router.get("/open_hood",response_class=HTMLResponse)
async def open_hood(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Капот открыт"})


@service_router.get("/close_hood",response_class=HTMLResponse)
async def close_hood(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "text": "Капот закрыт"})

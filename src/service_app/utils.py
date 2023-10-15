from fastapi import APIRouter

service_router = APIRouter()


@service_router.get("/light_on")
async def light_on():
    return "Свет включен"


@service_router.get("/light_off")
async def light_off():
    return "Свет выключен"


@service_router.get("/near_battery_station")
async def near_battery_station():
    return "Ближайшая зарядкная станция расположена: "


@service_router.get("/open_door")
async def open_door():
    return "Открыть двери"


@service_router.get("/close_door")
async def close_door():
    return "Закрыть двери"


@service_router.get("/get_location_car")
async def get_location_car():
    return "Ваша машина находится: "


@service_router.get("/get_charge")
async def get_charge():
    return "Уровень зарядки: "


@service_router.get("/on_near_light")
async def on_near_light():
    return "Ближний свет включен"


@service_router.get("/off_near_light")
async def off_near_light():
    return "Ближний свет выключен"


@service_router.get("/on_far_light")
async def on_far_light():
    return "Дальний свет включен"


@service_router.get("/off_far_light")
async def off_far_light():
    return "Дальний свет выключен"


@service_router.get("/open_trunk")
async def open_trunk():
    return "Багажник открыт"


@service_router.get("/close_trunk")
async def close_trunk():
    return "Багажник закрыт"


@service_router.get("/on_conditioner")
async def on_conditioner():
    return "Кондиционер включен"


@service_router.get("/off_conditioner")
async def off_conditioner():
    return "Кондиционер выключен"


@service_router.get("/open_hood")
async def open_hood():
    return "Капот открыт"


@service_router.get("/close_hood")
async def close_hood():
    return "Капот закрыт"

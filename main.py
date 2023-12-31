import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from SpeechRecognize import Recognizer
from SpeechValidators import ValidatorZoneAndCommand as vzac, CommandValidator as cv
from SpeechValidators import ZoneValidator as zv
from SpeechValidators import CommandsInfo as ci
from Helpers import GetZone, GetDistance, ConverterStringToCoords
from fastapi.templating import Jinja2Templates

from service_app.utils import service_router

app = FastAPI(
    title="AtomApp"
)

main_router = APIRouter()
main_router.include_router(service_router, prefix="/service", tags=["command"])
app.include_router(main_router)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/speak", response_class=HTMLResponse)
def speakmicro(request: Request):
    rec = Recognizer.Recognizer()
    text = rec.get_text()
    user_location = "40.7128 74.00601"
    return templates.TemplateResponse("RightCommandOrNot.html", {"request": request,
                                                                 "text": text, "user_location": user_location})


@app.get("/recieve_command{command}&{location_user}", response_class=HTMLResponse)
def send_command(request: Request, command: str, location_user: str):
    command = command[9:]
    location_user = location_user[14:]
    print(location_user)
    user_location = ConverterStringToCoords.ConverterSTringToCoords(location_user)
    print(command)
    car_location = (40.7128, 74.00600)
    distance = GetDistance.get_distance(user_location, car_location)
    print(distance)
    current_zone = GetZone.get_zone(distance)
    print(current_zone)
    if not cv.CommandValidator(ci.comms).find_command(command):
        return templates.TemplateResponse("WrongCommand.html", {"request": request})
    if not zv.ZoneValidator(ci.zones).check_zone(current_zone, command):
        return templates.TemplateResponse("WrongZone.html", {"request": request})
    print(ci.dict_command_path[command])
    path_request = "/service/" + ci.dict_command_path[command]
    print(path_request)
    return RedirectResponse(path_request)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)

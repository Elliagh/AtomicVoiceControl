import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from SpeechRecognize import Recognizer
from SpeechValidators import ValidatorZoneAndCommand as vzac, CommandValidator as cv
from SpeechValidators import ZoneValidator as zv
from SpeechValidators import CommandsInfo as ci
from Helpers import GetZone, GetDistance, ConverterStringToCoords
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="AtomApp"
)

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("init.html", {"request": request})


@app.get("/speak", response_class=HTMLResponse)
def speakmicro(request: Request):
    rec = Recognizer.Recognizer()
    try:
        text = rec.get_text()
    except:
        return RedirectResponse("/")
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
    path_request = ci.dict_command_path[command]
    return RedirectResponse(path_request)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)


def light_on():
    pass


def light_off():
    pass


def near_battery_station():
    pass

def open_door():
    pass

def close_door():
    pass

def get_location_car():
    pass

def get_charge():
    pass

def on_near_light():
    pass

def off_near_light():
    pass

def on_far_light():
    pass

def off_far_light():
    pass

def build_route(point):
    pass

def open_trunk():
    pass

def close_trunk():
    pass

def on_conditioner():
    pass

def off_conditioner():
    pass

def open_hood():
    pass

def close_hood():
    pass


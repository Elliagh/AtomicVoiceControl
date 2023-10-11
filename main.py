from fastapi.responses import HTMLResponse
from SpeechRecognize import Recognizer
from SpeechValidators import ValidatorZoneAndCommand as vzac, CommandValidator as cv
from SpeechValidators import ZoneValidator as zv
from SpeechValidators import CommandsInfo as ci
from Helpers import GetZone, GetDistance, ConverterStringToCoords
from fastapi import FastAPI

app = FastAPI(
    title="AtomApp"
)

html = """<!DOCTYPE html>
<html style="font-size: 16px;"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="Voice Manager Car, Нажмите на кнопку и говорите в течении 5 секунд"><meta name="description" content="">
    <title></title>
    <link rel="stylesheet" href="/nicepage.css" media="screen">
    <script class="u-script" type="text/javascript" src="np://app.desktop.nicepage.com/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="np://app.desktop.nicepage.com/nicepage.js" defer=""></script>
<meta name="generator" content="Nicepage 5.19.3, nicepage.com"></head>
<body class="u-body u-overlap u-xl-mode" data-style="blank" data-posts="" data-global-section-properties="{&quot;colorings&quot;:{&quot;light&quot;:[&quot;clean&quot;],&quot;colored&quot;:[&quot;clean&quot;],&quot;dark&quot;:[&quot;dark&quot;]}}" data-source="blank" data-lang="ru" data-page-sections-style="[{&quot;name&quot;:&quot;blank&quot;}]" data-page-coloring-types="{&quot;light&quot;:[&quot;clean&quot;],&quot;colored&quot;:[&quot;clean&quot;],&quot;dark&quot;:[&quot;dark&quot;]}" data-page-category="&quot;Basic&quot;"><section class="u-clearfix u-block-6981-1" custom-posts-hash="[]" data-style="blank" data-section-properties="{&quot;margin&quot;:&quot;none&quot;,&quot;stretch&quot;:true}" id="sec-34c5" data-id="6981">
  <div class="u-clearfix u-sheet u-block-6981-2"><h1 class="u-text u-text-default-xs u-block-6981-6">Voice Manager Car</h1><a href="/speak" class="u-active-palette-2-dark-1 u-border-none u-btn u-button-style u-hover-palette-3-base u-palette-1-base u-block-6981-3">Где деньги Лебовски</a><h1 class="u-text u-block-6981-5">Нажмите на кнопку и говорите в течении 5 секунд</h1></div>
<style data-mode="XL" data-visited="true">@media (min-width: 1200px) {
  .u-block-6981-2 {
    min-height: 1105px;
  }
  .u-block-6981-6 {
    margin-top: 284px;
    margin-right: -194px;
    margin-bottom: 0;
    margin-left: 218px;
  }
  .u-block-6981-3 {
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 82px;
    margin-right: auto;
    margin-bottom: 0;
    margin-left: 267px;
    padding-top: 59px;
    padding-right: 186px;
    padding-bottom: 59px;
    padding-left: 185px;
  }
  .u-block-6981-5 {
    width: 779px;
    margin-top: 61px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 60px;
  }
}</style><style data-mode="LG" data-visited="true">@media (max-width: 1199px) and (min-width: 992px) {
  .u-block-6981-2 {
    min-height: 1105px;
  }
  .u-block-6981-6 {
    width: auto;
    margin-top: 275px;
    margin-right: -237px;
    margin-bottom: 0;
    margin-left: 261px;
  }
  .u-block-6981-3 {
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 87px;
    margin-right: auto;
    margin-bottom: 0;
    margin-left: 131px;
    padding-top: 59px;
    padding-right: 186px;
    padding-bottom: 59px;
    padding-left: 185px;
  }
  .u-block-6981-5 {
    width: auto;
    margin-top: 67px;
    margin-right: 174px;
    margin-bottom: 60px;
    margin-left: 87px;
  }
}</style><style data-mode="MD" data-visited="true">@media (max-width: 991px) and (min-width: 768px) {
  .u-block-6981-2 {
    min-height: 1105px;
  }
  .u-block-6981-6 {
    width: auto;
    margin-top: 206px;
    margin-right: -19px;
    margin-bottom: 0;
    margin-left: 43px;
  }
  .u-block-6981-3 {
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 38px;
    margin-right: auto;
    margin-bottom: 0;
    margin-left: 118px;
    padding-top: 59px;
    padding-right: 186px;
    padding-bottom: 59px;
    padding-left: 185px;
  }
  .u-block-6981-5 {
    width: 527px;
    margin-top: 152px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 60px;
  }
}</style><style data-mode="SM" data-visited="true">@media (max-width: 767px) and (min-width: 576px) {
  .u-block-6981-2 {
    min-height: 1105px;
  }
  .u-block-6981-6 {
    width: auto;
    margin-top: 317px;
    margin-right: 0;
    margin-bottom: 0;
    margin-left: 24px;
  }
  .u-block-6981-3 {
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 135px;
    margin-right: auto;
    margin-bottom: 0;
    margin-left: 64px;
    padding-top: 59px;
    padding-right: 186px;
    padding-bottom: 59px;
    padding-left: 185px;
  }
  .u-block-6981-5 {
    width: auto;
    margin-top: 71px;
    margin-right: auto;
    margin-bottom: 60px;
    margin-left: 13px;
  }
}</style><style data-mode="XS" data-visited="true">@media (max-width: 575px) {
  .u-block-6981-2 {
    min-height: 678px;
  }
  .u-block-6981-6 {
    width: auto;
    margin-top: 107px;
    margin-left: 18px;
    margin-right: 18px;
    margin-bottom: 0;
  }
  .u-block-6981-3 {
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 107px;
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    padding-top: 59px;
    padding-right: 132px;
    padding-bottom: 59px;
    padding-left: 132px;
  }
  .u-block-6981-5 {
    width: auto;
    margin-top: 43px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 60px;
  }
}</style></section>
</body></html>"""

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get("/speak", response_class=HTMLResponse)
def speakmicro():
    rec = Recognizer.Recognizer()
    text = rec.get_text()
    user_location = "40.7128 74.00601"
    return f"""<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Кнопка</title>
    </head>
    <div>
    Команда : {text}
    </div>
    <body>
     <form action="/recieve_command&command='{text}'&location_user='{user_location}'" target="_blank">
    <button>Нажми если это то что ты говорил</button>
    </form>
    </body>
    <body>
     <form action="/" target="_blank">
    <button>Нажми если это не то что ты говорил</button>
    </form>
    </body>
    </html>
    """

@app.get("/recieve_command{command}&{location_user}", response_class=HTMLResponse)
def send_command(command : str, location_user : str):
    command = command[10:-1]
    location_user = location_user[15:-1]
    print(location_user)
    user_location = ConverterStringToCoords.ConverterSTringToCoords(location_user)
    print(command)
    car_location = (40.7128, 74.00600)
    distance = GetDistance.get_distance(user_location, car_location)
    print(distance)
    current_zone = GetZone.get_zone(distance)
    print(current_zone)
    if not cv.CommandValidator(ci.comms).find_command(command):
            return f"""<!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>Кнопка</title>
            </head>
            <div>
            "Command does not exist"
            </div>
            <body>
            <form action="/" target="_blank">
            <button>Нажми чтобы вернуться обратно (спасите)</button>
            </form>
            </body>
            </html>
            """
    if not zv.ZoneValidator(ci.zones).check_zone(current_zone, command):
            return f"""<!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>Кнопка</title>
            </head>
            <div>
            "Command not available in this zone"
            </div>
            <body>
            <form action="/" target="_blank">
            <button>Нажми чтобы вернуться обратно (спасите)</button>
            </form>
            </body>
            </html>
            """
    return "success"

import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Python.api.schema import Request, Response
from starlette.requests import Request as StarletteRequest

from Python.simple_python.src import remove_null, reverse_substrings

TITLE = "Sina"
DESCRIPTION = "Flexible API to make you write english correctly!"

app = FastAPI(title=TITLE, description=DESCRIPTION)


# @ the root we show title, description and link to docs
@app.get("/", response_class=HTMLResponse, status_code=200)
def index(request: StarletteRequest) -> str:
    return f"""
        <html>
            <head>
                <title>{TITLE}</title>
            </head>

            <body>
                <h1>{DESCRIPTION}</h1>
                <p>Find documentation  
                    <a href="{os.path.join(request.url.__str__(), "docs")}"> here </a>
                </p>
            </body>
        </html>
    """


@app.post("/clean_string", response_model=Response, status_code=200)
async def clean_string(request: Request) -> Response:
    return Response.parse_obj(
        {"processed_string": reverse_substrings(remove_null(request.string))}
    )

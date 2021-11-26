from pydantic import BaseModel, Field


class Request(BaseModel):
    string: str = Field(
        default="2076,3B,19C,138D,NULL,NULL",
        description="string that contains sub strings separated by a common",
    )


class Response(BaseModel):
    processed_string: str = Field(
        default="138D,19C,3B,2076",
        description="a processed string ex. input= 2076,3B,19C,138D,NULL,NULL output=138D,"
        "19C,3B,2076",
    )

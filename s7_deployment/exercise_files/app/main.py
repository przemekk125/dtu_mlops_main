import re
from enum import Enum
from http import HTTPStatus

#import cv2
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    """Health check."""
    return {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }

class ItemEnum(Enum):  # noqa: D101
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

#@app.get("/restric_items/{item_id}")
#def read_item(item_id: ItemEnum):  # noqa: D103
#    return {"item_id": item_id}  # noqa: ERA001

@app.get("/query_items")
def read_item(item_id: int): # noqa: D103
    return {"item_id": item_id}

database = {"username": [ ], "password": [ ]}

@app.post("/login/")
def login(username: str, password: str):  # noqa: D103
    username_db = database["username"]
    password_db = database["password"]
    if username not in username_db and password not in password_db:
        with open("database.csv", "a") as file:
            file.write(f"{username}, {password} \n")
        username_db.append(username)
        password_db.append(password)
    return "login saved"




class Mail(BaseModel):
    email: str
    domain_match: str


@app.post("/text_model/")
def contains_email(data: Mail):  # noqa: D103
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # noqa: Q000
    mail = data.email
    domain = data.domain_match
    if domain == mail.split('@')[-1]:
        response = {
            "input": data,
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "is_email": re.fullmatch(regex, mail) is not None # type: ignore
        }
    else:
        response = {
            "input": data,
            "message": HTTPStatus.BAD_REQUEST.phrase,
            "status-code": HTTPStatus.BAD_REQUEST,
            "is_email": False
        }
    return response

"""from fastapi import UploadFile, File
from typing import Optional
from fastapi.responses import FileResponse
import cv2

@app.post("/cv_model/")
async def cv_model(data: UploadFile = File(...), h: int = 224, w: int = 224):  # noqa: D103
    with open('image.jpg', 'wb') as image:
        content = await data.read()
        image.write(content)
        image.close()
    img = cv2.imread("image.jpg")
    res = cv2.resize(img, (h, w))
    cv2.imwrite("resized_image.jpg", res)
    return FileResponse('resized_image.jpg')
    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response"""
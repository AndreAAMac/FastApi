#Descobrir o endereço local
#>>> import socket
#>>> s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#>>> s.connect(("8.8.8.8", 80))
#>>> s.getsockname()[0]
#'192.168.0.100'

from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/users/', response_model=UserPublic)
def create_user(user: UserSchema):
    return user

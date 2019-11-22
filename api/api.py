from flask import Blueprint, Response, request, jsonify
from .service import Musicas
import requests
import json


Lista = Blueprint(
    "artista", __name__, url_prefix="/v1/musicas"
)

@Lista.route("/artista/<nome>", methods=["GET"])
def artista(nome):
    a = Musicas.process(nome)
    b = json.dumps(a)

    return b



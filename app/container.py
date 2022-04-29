from dependency_injector import containers, providers
from dependency_injector.ext import flask as flask_ext
from flask import Flask

from app.api import get_prediction
from app.services import PredictionService


class Container(containers.DeclarativeContainer):
    app = flask_ext.Application(Flask, __name__)

    prediction_service = providers.Singleton(
        PredictionService
    )

    get_prediction = flask_ext.View(
        get_prediction,
        prediction_service=prediction_service
    )

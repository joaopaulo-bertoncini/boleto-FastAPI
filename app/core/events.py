from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core.settings.app import AppSettings

def create_start_app_handler(app: FastAPI,settings: AppSettings,) -> Callable:  # type: ignore
    return


def create_stop_app_handler(app: FastAPI) -> Callable:
    return
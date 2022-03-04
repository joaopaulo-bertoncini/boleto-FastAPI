#!/bin/bash

source venv/bin/active
uvicorn app.main:app --reload
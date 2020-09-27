@echo off
title ErdemMusic
color a
pip install -U -r requirements.txt
cls
:a
py bot.py
goto a
"""
Script de build para o YT Downloader usando py2app.

Este script empacota o aplicativo em um bundle .app autocontido,
incluindo o interpretador Python, as bibliotecas necessárias e os
executáveis yt-dlp e ffmpeg.
"""
from setuptools import setup
import os

# --- Configurações Principais ---
APP_NAME = "YT Downloader"
APP_SCRIPT = "YT Downloader.app/Contents/MacOS/yt_downloader_gui.py"
APP_VERSION = "1.2.0"

# --- Caminhos para os Binários ---
# Localiza os executáveis no PATH do Homebrew
YT_DLP_PATH = "/opt/homebrew/bin/yt-dlp"
FFMPEG_PATH = "/opt/homebrew/bin/ffmpeg"

# --- Ícone do Aplicativo ---
# ICON_PATH = "YT Downloader.app/Icon"

# --- Opções do py2app ---
OPTIONS = {
    "argv_emulation": True,
    # "iconfile": ICON_PATH,
    "packages": ["tkinter"],
    # Inclui os binários na pasta Contents/Resources do app
    "resources": [YT_DLP_PATH, FFMPEG_PATH],
    "plist": {
        "CFBundleName": APP_NAME,
        "CFBundleDisplayName": APP_NAME,
        "CFBundleGetInfoString": "Baixador de vídeos do YouTube",
        "CFBundleIdentifier": "com.vagner.ytdownloader",
        "CFBundleVersion": APP_VERSION,
        "CFBundleShortVersionString": APP_VERSION,
        "NSHumanReadableCopyright": "Copyright © 2025, Vagner Santos de Araujo. Todos os direitos reservados."
    }
}

# --- Execução do setup ---
setup(
    app=[APP_SCRIPT],
    name=APP_NAME,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)

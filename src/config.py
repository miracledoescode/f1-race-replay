import os

# --- Resource Paths ---
# Base directories
IMAGES_DIR = "images"
RESOURCES_DIR = "resources"
CACHE_DIR = ".fastf1-cache"
COMPUTED_DATA_DIR = "computed_data"

# Image subdirectories
CONTROLS_ICONS_DIR = os.path.join(IMAGES_DIR, "controls")
WEATHER_ICONS_DIR = os.path.join(IMAGES_DIR, "weather")
TYRE_ICONS_DIR = os.path.join(IMAGES_DIR, "tyres")

# Background images
BACKGROUND_IMAGE_PATH = os.path.join(RESOURCES_DIR, "background.png")

# --- Screen Settings ---
DEFAULT_SCREEN_WIDTH = 1920
DEFAULT_SCREEN_HEIGHT = 1200
DEFAULT_SCREEN_TITLE = "F1 Race Replay"

# --- Telemetry Settings ---
FPS = 25
DT = 1 / FPS

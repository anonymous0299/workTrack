import os

# API configuration
BACKEND_URL = "https://worktrack-w8jx.onrender.com/api/tracking/ping"
PING_INTERVAL = 5  # seconds
IDLE_THRESHOLD = 300  # seconds (5 minutes)

# Config location for local caching and tokens
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SQLITE_DB = os.path.join(CONFIG_DIR, "offline_buffer.db")

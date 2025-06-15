from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import MemoryCacheHandler
import getpass
import time


try:
    client_id = input("Enter your client ID: ")
    client_secret = getpass.getpass("Enter your client secret: ")
    redirect_uri = input("Enter your redirect URI: ")
    
   
    cache = MemoryCacheHandler()
    SpotifyOAuth(cache_handler=cache, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri).get_access_token(as_dict=False)
    refresh_token = cache.get_cached_token().get("refresh_token")

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print(f"\n{MAGENTA}{'='*60}{RESET}")
    print(f"{GREEN}🎵 {BOLD}Your Spotify Refresh Token:{RESET}\n")
    print(f"{YELLOW}{BOLD}{refresh_token}{RESET}")
    print(f"\n{MAGENTA}{'='*60}{RESET}")

    print(f"\n{CYAN}🔐 COPY the refresh token above and add it as a GitHub Actions secret.{RESET}")
    print("👉 Go to your repository → Settings → Secrets → Actions → 'New repository secret'")
    print(f"Name it: {BOLD}SPOTIPY_REFRESH_TOKEN{RESET}")
    print("And paste the token as the value.\n")

    print(f"{MAGENTA}{'='*60}{RESET}")
    input()
except Exception as e:
    print(f"Error: {e}")
    time.sleep(5)

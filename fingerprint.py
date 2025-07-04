import requests
import uuid
import random
import json
import base64

def make_super_properties():
    props = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": "en-GB",
        "has_client_mods": False,
        "browser_user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) "
            "Gecko/20100101 Firefox/140.0"
        ),
        "browser_version": "140.0",
        "os_version": "10",
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": random.randint(400_000, 500_000),
        "client_event_source": None,
        "client_launch_id": str(uuid.uuid4()),
        "client_app_state": "unfocused"
    }
    compact = json.dumps(props, separators=(",", ":")).encode("utf-8")
    return base64.b64encode(compact).decode("utf-8")

def fetch_and_print():
    url = "https://discord.com/api/v9/experiments?with_guild_experiments=true"
    super_props = make_super_properties()
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "discord.com",
        "Referer": "https://discord.com/register",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "X-Context-Properties": "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "en-GB",
        "X-Discord-Timezone": "Europe/Amsterdam",
        "X-Super-Properties": super_props
    }
    resp = requests.get(url, headers=headers, timeout=10)
    print(resp.json().get("fingerprint", ""))
    print(super_props)

if __name__ == "__main__":
    fetch_and_print()

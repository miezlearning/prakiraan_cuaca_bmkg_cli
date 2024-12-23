
import requests
import logging

logger = logging.getLogger(__name__)

def fetch_prakiraan_cuaca(adm_level_code, kode):
    """
    Mengambil data prakiraan cuaca dari API BMKG.
    """
    url = f'https://api.bmkg.go.id/publik/prakiraan-cuaca?{adm_level_code}={kode}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        logger.error(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.ConnectionError as errc:
        logger.error(f"Error Connecting: {errc}")
        return None
    except requests.exceptions.Timeout as errt:
        logger.error(f"Timeout Error: {errt}")
        return None
    except requests.exceptions.RequestException as err:
        logger.error(f"OOPS: Something Else: {err}")
        return None

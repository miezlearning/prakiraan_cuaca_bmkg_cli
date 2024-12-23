import os
"""
Imports:
- os: Modul ini menyediakan fungsi untuk berinteraksi dengan sistem operasi, seperti membersihkan layar terminal.
- requests: Modul ini digunakan untuk melakukan HTTP requests, seperti mengambil data prakiraan cuaca dari API.
- logging: Modul ini digunakan untuk mencatat log atau pesan kesalahan selama program berjalan.
- csv: Modul ini digunakan untuk membaca dan menulis file CSV.
- collections.defaultdict, collections.Counter: Digunakan untuk membuat dictionary dengan nilai default dan menghitung frekuensi elemen.
- datetime: Modul ini digunakan untuk memanipulasi tanggal dan waktu.
- tabulate: Modul ini digunakan untuk membuat tabel yang rapi dari data yang diberikan.
- rich.console.Console, rich.prompt.Prompt, rich.prompt.Confirm: Digunakan untuk membuat tampilan terminal yang lebih interaktif dan berwarna.
"""
import requests
import logging
import csv
from collections import defaultdict, Counter
from datetime import datetime
from tabulate import tabulate
from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
wilayah_hierarchy = {}
adm_levels = {
    1: {'code': 'adm1', 'name': 'Provinsi'},
    2: {'code': 'adm2', 'name': 'Kabupaten/Kota'},
    3: {'code': 'adm3', 'name': 'Kecamatan'},
    4: {'code': 'adm4', 'name': 'Kelurahan/Desa'}
}

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def load_wilayah_from_csv(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            first_row = next(reader)
            if first_row[0].lower().startswith('adm'):
                pass
            else:
                csvfile.seek(0)
                reader = csv.reader(csvfile)
            
            current_adm1 = None
            current_adm2 = None
            current_adm3 = None

            for row in reader:
                if not row or len(row) < 2:
                    continue

                adm_code = row[0].strip()
                adm_name = row[1].strip()
                parts = adm_code.split('.')
                level = len(parts)

                if level == 1:
                    if adm_code not in wilayah_hierarchy:
                        wilayah_hierarchy[adm_code] = {
                            'name': adm_name,
                            'children': {}
                        }
                    current_adm1 = adm_code
                    current_adm2 = None
                    current_adm3 = None

                elif level == 2:
                    if current_adm1 is None:
                        logger.warning(f"adm2 {adm_code} tanpa adm1.")
                        continue
                    if adm_code not in wilayah_hierarchy[current_adm1]['children']:
                        wilayah_hierarchy[current_adm1]['children'][adm_code] = {
                            'name': adm_name,
                            'children': {}
                        }
                    current_adm2 = adm_code
                    current_adm3 = None

                elif level == 3:
                    if current_adm2 is None:
                        logger.warning(f"adm3 {adm_code} tanpa adm2.")
                        continue
                    if adm_code not in wilayah_hierarchy[current_adm1]['children'][current_adm2]['children']:
                        wilayah_hierarchy[current_adm1]['children'][current_adm2]['children'][adm_code] = {
                            'name': adm_name,
                            'children': {}
                        }
                    current_adm3 = adm_code

                elif level == 4:
                    if current_adm3 is None:
                        logger.warning(f"adm4 {adm_code} tanpa adm3.")
                        continue
                    wilayah_hierarchy[current_adm1]['children'][current_adm2]['children'][current_adm3]['children'][adm_code] = adm_name

                else:
                    logger.warning(f"Kode adm yang tidak dikenali: {adm_code}")
    except FileNotFoundError:
        logger.error(f"File {filename} tidak ditemukan.")
        console.print(f"[bold red]File {filename} tidak ditemukan.[/bold red]")
        exit()
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat membaca {filename}: {e}")
        console.print(f"[bold red]Terjadi kesalahan saat membaca {filename}: {e}[/bold red]")
        exit()

def display_menu(options, adm_level_name):
    console.print(f"\n[bold cyan]Pilih {adm_level_name}:[/bold cyan]")
    for idx, (code, name) in enumerate(options, start=1):
        console.print(f"[yellow]{idx}.[/yellow] {name}")

    while True:
        try:
            pilihan = Prompt.ask(f"Masukkan pilihan {adm_level_name} (1-{len(options)})", default="1")
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(options):
                selected_code = options[pilihan - 1][0]
                selected_name = options[pilihan - 1][1]
                return selected_code, selected_name
            else:
                console.print(f"[bold red]Input tidak valid. Harap masukkan angka antara 1 dan {len(options)}.[/bold red]")
        except ValueError:
            console.print("[bold red]Input tidak valid. Harap masukkan angka yang sesuai.[/bold red]")

def pilih_wilayah_dinamis():
    current_level = wilayah_hierarchy
    tingkat = 1
    max_tingkat = 4
    selected_codes = {}
    selected_names = {}

    while tingkat <= max_tingkat:
        bersihkan_layar()
        if tingkat < 4:
            options = [(code, info['name']) for code, info in current_level.items()]
        else:
            options = [(code, name) for code, name in current_level.items()]

        if not options:
            console.print(f"[bold red]Tidak ada opsi yang tersedia untuk {adm_levels[tingkat]['name']}.[/bold red]")
            break

        adm_level_name = adm_levels[tingkat]['name']
        selected_code, selected_name = display_menu(options, adm_level_name)
        selected_codes[adm_levels[tingkat]['code']] = selected_code
        selected_names[adm_levels[tingkat]['code']] = selected_name
        console.print(f"\nData Untuk {adm_level_name} dipilih: [bold magenta]{selected_name}[/bold magenta]")
        fetch_and_display_weather(adm_levels[tingkat]['code'], selected_code, tingkat)

        if tingkat < max_tingkat:
            lanjut = Confirm.ask(f"Apakah kamu ingin melanjutkan cek {adm_levels[tingkat +1]['name']}?")
            if lanjut:
                temp_level = wilayah_hierarchy
                for t in range(1, tingkat +1):
                    adm = adm_levels[t]['code']
                    code = selected_codes[adm]
                    if adm != 'adm4':
                        temp_level = temp_level[code]['children']
                current_level = temp_level
                tingkat +=1
            else:
                console.print("[bold green]Terima kasih telah menggunakan program cek cuaca.[/bold green]")
                break
        else:
            console.print("[bold green]Yeayy kamu telah mencapai tingkat wilayah terakhir.😁[/bold green]")
            break

def fetch_and_display_weather(adm_level_code, kode, tingkat):
    data_cuaca = fetch_prakiraan_cuaca(adm_level_code, kode)
    tampilkan_prakiraan(data_cuaca, tingkat)

def fetch_prakiraan_cuaca(adm_level_code, kode):
    url = f'https://api.bmkg.go.id/publik/prakiraan-cuaca?{adm_level_code}={kode}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        logger.error(f"HTTP Error: {errh}")
        console.print(f"[bold red]HTTP Error: {errh}[/bold red]")
    except requests.exceptions.ConnectionError as errc:
        logger.error(f"Error Connecting: {errc}")
        console.print(f"[bold red]Error Connecting: {errc}[/bold red]")
    except requests.exceptions.Timeout as errt:
        logger.error(f"Timeout Error: {errt}")
        console.print(f"[bold red]Timeout Error: {errt}[/bold red]")
    except requests.exceptions.RequestException as err:
        logger.error(f"OOPS: Something Else: {err}")
        console.print(f"[bold red]OOPS: Something Else: {err}[/bold red]")
    return None

def tampilkan_prakiraan(data, tingkat):
    if not data:
        console.print("[bold red]Tidak ada data prakiraan cuaca yang tersedia.[/bold red]")
        return

    if isinstance(data, dict):
        entries = data.get('data', [])
    elif isinstance(data, list):
        entries = data
    else:
        logger.error("Struktur data tidak dikenali.")
        console.print("[bold red]Struktur data tidak dikenali.[/bold red]")
        return

    if not entries:
        console.print("[bold red]Tidak ada data prakiraan cuaca yang tersedia.[/bold red]")
        return

    lokasi_info = entries[0].get('lokasi', {})
    provinsi = lokasi_info.get('provinsi', 'N/A')
    kotkab = lokasi_info.get('kotkab', 'N/A')
    kecamatan = lokasi_info.get('kecamatan', 'N/A')
    desa = lokasi_info.get('desa', 'N/A')

    if tingkat == 1:
        kotkab = 'N/A'
        kecamatan = 'N/A'
        desa = 'N/A'
    elif tingkat == 2:
        kecamatan = 'N/A'
        desa = 'N/A'
    elif tingkat == 3:
        desa = 'N/A'
    elif tingkat == 4:
        pass

    console.print("\n[bold blue]===== Prakiraan Cuaca =====[/bold blue]")
    console.print(f"[bold green]Provinsi           :[/bold green] {provinsi}")
    console.print(f"[bold green]Kabupaten/Kota     :[/bold green] {kotkab}")
    console.print(f"[bold green]Kecamatan          :[/bold green] {kecamatan}")
    console.print(f"[bold green]Kelurahan/Desa     :[/bold green] {desa}")
    console.print("[bold blue]==========================[/bold blue]\n")

    prakiraan_harian = defaultdict(lambda: {
        'suhu_min': float('inf'),
        'suhu_max': float('-inf'),
        'kelembaban_max': 0,
        'angin_total': 0.0,
        'angin_count': 0,
        'wd_freq': Counter(),
        'kondisi_freq': Counter()
    })

    for entry in entries:
        cuaca_list = entry.get('cuaca', [])
        for cuaca_group in cuaca_list:
            for forecast in cuaca_group:
                local_datetime_str = forecast.get('local_datetime')
                if not local_datetime_str:
                    continue

                try:
                    local_datetime = datetime.strptime(local_datetime_str, '%Y-%m-%d %H:%M:%S')
                    tanggal = local_datetime.date().isoformat()
                except ValueError:
                    logger.error(f"Format tanggal tidak valid: {local_datetime_str}")
                    console.print(f"[bold red]Format tanggal tidak valid: {local_datetime_str}[/bold red]")
                    continue

                suhu = forecast.get('t')
                kelembaban = forecast.get('hu')
                angin_speed = forecast.get('ws')
                angin_dir = forecast.get('wd')
                kondisi = forecast.get('weather_desc')

                if suhu is None or kelembaban is None or angin_speed is None or angin_dir is None or kondisi is None:
                    continue

                prakiraan = prakiraan_harian[tanggal]

                if suhu < prakiraan['suhu_min']:
                    prakiraan['suhu_min'] = suhu
                if suhu > prakiraan['suhu_max']:
                    prakiraan['suhu_max'] = suhu

                if kelembaban > prakiraan['kelembaban_max']:
                    prakiraan['kelembaban_max'] = kelembaban

                prakiraan['angin_total'] += angin_speed
                prakiraan['angin_count'] += 1
                prakiraan['wd_freq'][angin_dir] += 1
                prakiraan['kondisi_freq'][kondisi] += 1

    tabel_prakiraan = []
    for tanggal, info in sorted(prakiraan_harian.items()):
        if info['suhu_min'] == float('inf') or info['suhu_max'] == float('-inf'):
            continue

        suhu_min = info['suhu_min']
        suhu_max = info['suhu_max']
        kelembaban_max = info['kelembaban_max']
        angin_avg = info['angin_total'] / info['angin_count'] if info['angin_count'] > 0 else 'N/A'
        angin_dir = info['wd_freq'].most_common(1)[0][0] if info['wd_freq'] else 'N/A'
        kondisi = info['kondisi_freq'].most_common(1)[0][0] if info['kondisi_freq'] else 'N/A'

        tabel_prakiraan.append([
            tanggal,
            f"{suhu_min}°C - {suhu_max}°C",
            f"{kelembaban_max}%",
            f"{angin_avg:.1f} km/jam dari {angin_dir}" if angin_avg != 'N/A' else "N/A",
            kondisi
        ])

    if tabel_prakiraan:
        headers = ["Tanggal", "Suhu", "Kelembaban Maksimal", "Angin", "Kondisi Cuaca"]
        table = tabulate(tabel_prakiraan, headers=headers, tablefmt="rounded_grid")
        console.print("[bold magenta]Prakiraan Cuaca Harian:[/bold magenta]")
        console.print(table)
    else:
        console.print("[bold red]Tidak ada data prakiraan cuaca yang tersedia.[/bold red]")

    console.print("\n")

def main():
    console.print("[bold cyan]Selamat datang di program cek cuaca.[/bold cyan]\n")
    load_wilayah_from_csv('base.csv')
    pilih_wilayah_dinamis()

if __name__ == "__main__":
    main()

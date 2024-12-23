from collections import defaultdict, Counter
from datetime import datetime
from tabulate import tabulate
from rich.console import Console
from rich.prompt import Prompt, Confirm
from utils.display.header import pilih_provinsi_header, pilih_kabupaten_header, pilih_kecamatan_header, pilih_kelurahan_header
import logging

logger = logging.getLogger(__name__)
console = Console()

def display_menu(options, adm_level_name):
    """
    Menampilkan menu pilihan dan mengembalikan kode yang dipilih.
    """
    if adm_level_name == "Provinsi":
        pilih_provinsi_header()
    elif adm_level_name == "Kabupaten/Kota":
        pilih_kabupaten_header()
    elif adm_level_name == "Kecamatan":
        pilih_kecamatan_header()
    elif adm_level_name == "Kelurahan":
        pilih_kelurahan_header()
    for idx, (code, name) in enumerate(options, start=1):
        console.print(f"[yellow]{idx}.[/yellow] {name}")

    while True:
        try:
            pilihan = Prompt.ask(
    f"[bold cyan]🔍 Masukkan pilihan {adm_level_name} (1-{len(options)}) 🔍:[/bold cyan]",
    default="1",
    show_default=True
)
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(options):
                selected_code = options[pilihan - 1][0]
                selected_name = options[pilihan - 1][1]
                return selected_code, selected_name
            else:
                console.print(f"[bold red]Input tidak valid. Harap masukkan angka antara 1 dan {len(options)}.[/bold red]")
        except ValueError:
            console.print("[bold red]Input tidak valid. Harap masukkan angka yang sesuai.[/bold red]")

def tampilkan_prakiraan(data, tingkat, adm_levels):
    """
    Memproses dan menampilkan data prakiraan cuaca dengan format yang lebih rapi.
    Output disesuaikan dengan tingkat administrasi yang dipilih.
    """
    if not data:
        console.print("[bold red]Tidak ada data prakiraan cuaca yang tersedia.[/bold red]")
        return

    # Asumsikan data mengandung list prakiraan di key 'data'
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

    # Ambil informasi lokasi
    lokasi_info = entries[0].get('lokasi', {})
    provinsi = lokasi_info.get('provinsi', 'N/A')
    kotkab = lokasi_info.get('kotkab', 'N/A')
    kecamatan = lokasi_info.get('kecamatan', 'N/A')
    desa = lokasi_info.get('desa', 'N/A')

    # Sesuaikan informasi yang ditampilkan berdasarkan tingkat administrasi
    if tingkat == 1:
        # Provinsi
        kotkab = 'N/A'
        kecamatan = 'N/A'
        desa = 'N/A'
    elif tingkat == 2:
        # Kabupaten/Kota
        kecamatan = 'N/A'
        desa = 'N/A'
    elif tingkat == 3:
        # Kecamatan
        desa = 'N/A'
    elif tingkat == 4:
        # Kelurahan/Desa
        pass  # Semua informasi sudah diisi

    # Tampilkan informasi lokasi dengan warna
    console.print("\n[bold blue]===== Prakiraan Cuaca =====[/bold blue]")
    console.print(f"[bold green]Provinsi           :[/bold green] {provinsi}")
    console.print(f"[bold green]Kabupaten/Kota     :[/bold green] {kotkab}")
    console.print(f"[bold green]Kecamatan          :[/bold green] {kecamatan}")
    console.print(f"[bold green]Kelurahan/Desa     :[/bold green] {desa}")
    console.print("[bold blue]==========================[/bold blue]\n")

    # Menyiapkan struktur data untuk agregasi harian
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
                    continue  # Lewati jika tidak ada waktu lokal

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
                    continue  # Lewati jika data penting tidak ada

                prakiraan = prakiraan_harian[tanggal]

                # Update suhu_min dan suhu_max
                if suhu < prakiraan['suhu_min']:
                    prakiraan['suhu_min'] = suhu
                if suhu > prakiraan['suhu_max']:
                    prakiraan['suhu_max'] = suhu

                # Update kelembaban_max
                if kelembaban > prakiraan['kelembaban_max']:
                    prakiraan['kelembaban_max'] = kelembaban

                # Update angin_total dan angin_count
                prakiraan['angin_total'] += angin_speed
                prakiraan['angin_count'] += 1

                # Update arah angin
                prakiraan['wd_freq'][angin_dir] += 1

                # Update kondisi cuaca
                prakiraan['kondisi_freq'][kondisi] += 1

    # Menyiapkan data untuk tabel
    tabel_prakiraan = []
    for tanggal, info in sorted(prakiraan_harian.items()):
        if info['suhu_min'] == float('inf') or info['suhu_max'] == float('-inf'):
            continue  # Lewati jika tidak ada data suhu

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

    # Buat tabel menggunakan tabulate dengan style 'rounded_grid'
    if tabel_prakiraan:
        headers = ["Tanggal", "Suhu", "Kelembaban Maksimal", "Angin", "Kondisi Cuaca"]
        table = tabulate(tabel_prakiraan, headers=headers, tablefmt="rounded_grid")
        console.print("[bold magenta]Prakiraan Cuaca Harian:[/bold magenta]")
        console.print(table)
    else:
        console.print("[bold red]Tidak ada data prakiraan cuaca yang tersedia.[/bold red]")

    console.print("\n")

# main.py

import logging
from rich.console import Console
from utils.loader.loader import load_wilayah_from_csv
from utils.display.display import tampilkan_prakiraan, display_menu
from utils.display.header import opening_header
from api.fetch_api import fetch_prakiraan_cuaca
from utils.utils import bersihkan_layar, pause
from rich.prompt import Confirm

console = Console()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

adm_levels = {
    1: {'code': 'adm1', 'name': 'Provinsi'},
    2: {'code': 'adm2', 'name': 'Kabupaten/Kota'},
    3: {'code': 'adm3', 'name': 'Kecamatan'},
    4: {'code': 'adm4', 'name': 'Kelurahan/Desa'}
}

def pilih_wilayah_dinamis(wilayah_hierarchy):
    """
    Memulai pemilihan wilayah secara dinamis dari adm1 hingga adm4.
    """
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

        # Tampilkan menu dan dapatkan pilihan
        adm_level_name = adm_levels[tingkat]['name']
        selected_code, selected_name = display_menu(options, adm_level_name)

        # Simpan kode dan nama yang dipilih
        selected_codes[adm_levels[tingkat]['code']] = selected_code
        selected_names[adm_levels[tingkat]['code']] = selected_name

        # Tampilkan data yang dipilih
        console.print(f"\nData Untuk {adm_level_name} dipilih: [bold magenta]{selected_name}[/bold magenta]")

        # Ambil dan tampilkan prakiraan cuaca
        data_cuaca = fetch_prakiraan_cuaca(adm_levels[tingkat]['code'], selected_code)
        tampilkan_prakiraan(data_cuaca, tingkat, adm_levels)

        # Tanyakan apakah ingin melanjutkan ke tingkat berikutnya
        if tingkat < max_tingkat:
            lanjut = Confirm.ask(
    f"[bold magenta]✨ Apakah kamu siap untuk melanjutkan cek {adm_levels[tingkat + 1]['name']}? ✨[/bold magenta]",
    default=True
)
            if lanjut:
                # Set current_level ke children dari yang dipilih
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
            pause()
            start()
            break

def start():
    try:
        wilayah_hierarchy = load_wilayah_from_csv('data/base.csv')
    except Exception:
        console.print("[bold red]Gagal memuat data wilayah. Program dihentikan.[/bold red]")
        return

    # Memulai pemilihan wilayah secara dinamis
    pilih_wilayah_dinamis(wilayah_hierarchy)

def main():
    # Tampilkan pesan selamat datang dengan warna
    # console.print("[bold cyan]Selamat datang di program cek cuaca.[/bold cyan]\n")
    bersihkan_layar()
    opening_header()
    pause()

    # Memuat data wilayah dari base.csv
    start()

if __name__ == "__main__":
    main()

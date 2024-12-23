from rich.console import Console
console = Console()
import os

def bersihkan_layar():
    """
    Membersihkan layar konsol.
    Menggunakan 'cls' untuk Windows dan 'clear' untuk sistem operasi lainnya.
    """
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    try:
        console.print("[bold blue]Tekan [Enter] untuk melanjutkan...[/bold blue]")
        input()
    except KeyboardInterrupt:
        pass
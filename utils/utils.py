
import os

def bersihkan_layar():
    """
    Membersihkan layar konsol.
    Menggunakan 'cls' untuk Windows dan 'clear' untuk sistem operasi lainnya.
    """
    os.system("cls" if os.name == "nt" else "clear")

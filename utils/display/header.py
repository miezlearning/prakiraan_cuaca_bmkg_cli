
from rich.console import Console
console = Console()

def opening_header():
    console.print("""[bold red]
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣶⣄⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀[/bold red] [bold white]
⠀⢠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠈⠿⣿⣿⡿⠋⠈⠻⣿⣿⣿⣿⡿⠟⠁⠀⠙⠿⠿⠛⠁⠙⠻⠿⠿⠟⠁⠀⠀
⠀⠀⠀⠀⣠⡀⠀⠀⢦⡄⠉⠉⣁⠀⠀⠀⠀⠀⠀⠰⡆⠀⠀⢰⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⠇⠀⠀⠈⠀⠀⠀⠛⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠀⢰⡄⠀⠀⣀⠀⠀⠈⠛⠀⠀⢰⣧⠀⠀⠀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣷⠀⠀⠈⠉⠀⠀⢻⡇⠀⠀⠀⡀⠀⠀⠉⠀⠀⠀⢻⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠛⠂⠀⠀⢠⡄⠀⠈⠟⠀⠀⠀⢿⠀⠀⠀⣤⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠃⠀⠀⠀⣀⠀⠀⠘⠃⠀⠀⠉⠀⠀⠀⢰⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠓⠀⠀[/bold white]
          
[bold green]Selamat datang di aplikasi prakiraan cuaca![/bold green]
[bold white]Aplikasi ini akan membantu kamu untuk melihat prakiraan cuaca di[/bold white] [bold red]Indo[bold white]nesia[/bold white][/bold red].
[bold white]Silakan pilih wilayah yang ingin kamu lihat prakiraan cuacanya.[/bold white]
[bold white]Selamat menikmati![/bold white]
                  
[bold yellow]Created by: @miezlipp[/bold yellow]
[bold yellow]API by: [/bold yellow]

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░▒░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓████▓▓▓▒░░░▒▓▓▓░░░░▒▓▓▓░░░██░░░░▒▓▓▓░░░░▒▓████▓▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░███▒▒▒▒██▓░░▓████░░░████▒░▒██░░░▓██▒░░░▒██▓▒░░▒██▓░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██▓░░░▒██▒░░▓████▒░▓█▓██▒░▒██░▓██▒░░░░░██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░█████████▒░░▓██▒█▓░██░██▒░▒██████▓░░░░░██▒░░░█████░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██▓░░░░░██▒░▓██░████▒░██▒░▒██▓░░▓██▒░░░██▓░░░░░▒██░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░███▓▓▓▓███░░▓██░▒███░░██▒░▒██░░░░▒██▓░░░▓██▓▓▓▓███░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░▒▒░░▒▒▒░░▒▒░░░▒▒░░░░░▒▒▒░░░░░▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    

def pilih_provinsi_header():
    console.print("""
[bold red]
██████╗░██╗██╗░░░░░██╗██╗░░██╗  ██████╗░██████╗░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗██╗
██╔══██╗██║██║░░░░░██║██║░░██║  ██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║████╗░██║██╔════╝██║
██████╔╝██║██║░░░░░██║███████║  ██████╔╝██████╔╝██║░░██║╚██╗░██╔╝██║██╔██╗██║╚█████╗░██║[/bold red][bold white]
██╔═══╝░██║██║░░░░░██║██╔══██║  ██╔═══╝░██╔══██╗██║░░██║░╚████╔╝░██║██║╚████║░╚═══██╗██║
██║░░░░░██║███████╗██║██║░░██║  ██║░░░░░██║░░██║╚█████╔╝░░╚██╔╝░░██║██║░╚███║██████╔╝██║
╚═╝░░░░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝
[/bold white]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    
def pilih_kabupaten_header():
    console.print("""
[bold red]
██████╗░██╗██╗░░░░░██╗██╗░░██╗  ██╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░█████╗░████████╗███████╗███╗░░██╗
██╔══██╗██║██║░░░░░██║██║░░██║  ██║░██╔╝██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗░██║
██████╔╝██║██║░░░░░██║███████║  █████═╝░███████║██████╦╝██║░░░██║██████╔╝███████║░░░██║░░░█████╗░░██╔██╗██║[/bold red][bold white]
██╔═══╝░██║██║░░░░░██║██╔══██║  ██╔═██╗░██╔══██║██╔══██╗██║░░░██║██╔═══╝░██╔══██║░░░██║░░░██╔══╝░░██║╚████║
██║░░░░░██║███████╗██║██║░░██║  ██║░╚██╗██║░░██║██████╦╝╚██████╔╝██║░░░░░██║░░██║░░░██║░░░███████╗██║░╚███║
╚═╝░░░░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝
[/bold white]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")   
    
def pilih_kecamatan_header():
    console.print("""
[bold red]
██████╗░██╗██╗░░░░░██╗██╗░░██╗  ██╗░░██╗███████╗░█████╗░░█████╗░███╗░░░███╗░█████╗░████████╗░█████╗░███╗░░██╗
██╔══██╗██║██║░░░░░██║██║░░██║  ██║░██╔╝██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
██████╔╝██║██║░░░░░██║███████║  █████═╝░█████╗░░██║░░╚═╝███████║██╔████╔██║███████║░░░██║░░░███████║██╔██╗██║[/bold red][bold white]
██╔═══╝░██║██║░░░░░██║██╔══██║  ██╔═██╗░██╔══╝░░██║░░██╗██╔══██║██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║██║╚████║
██║░░░░░██║███████╗██║██║░░██║  ██║░╚██╗███████╗╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║██║░╚███║
╚═╝░░░░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
[/bold white]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")   

def pilih_kelurahan_header():
    console.print("""
[bold red]
██████╗░██╗██╗░░░░░██╗██╗░░██╗  ██╗░░██╗███████╗██╗░░░░░██╗░░░██╗██████╗░░█████╗░██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗██║██║░░░░░██║██║░░██║  ██║░██╔╝██╔════╝██║░░░░░██║░░░██║██╔══██╗██╔══██╗██║░░██║██╔══██╗████╗░██║
██████╔╝██║██║░░░░░██║███████║  █████═╝░█████╗░░██║░░░░░██║░░░██║██████╔╝███████║███████║███████║██╔██╗██║[/bold red][bold white]
██╔═══╝░██║██║░░░░░██║██╔══██║  ██╔═██╗░██╔══╝░░██║░░░░░██║░░░██║██╔══██╗██╔══██║██╔══██║██╔══██║██║╚████║
██║░░░░░██║███████╗██║██║░░██║  ██║░╚██╗███████╗███████╗╚██████╔╝██║░░██║██║░░██║██║░░██║██║░░██║██║░╚███║
╚═╝░░░░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
[/bold white]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")   
import os


def clear_screen():
    # Clear command for Windows vs Unix-based systems (Linux, macOS)
    os.system('cls' if os.name == 'nt' else 'clear')

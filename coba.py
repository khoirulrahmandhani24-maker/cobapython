import time
import sys
import os

# Warna teks
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def slow_print(text, delay=0.05):
    """Cetak teks dengan efek mengetik"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animasi lilin berkedip 🎂
cake_frames = [
    f"""
        {YELLOW}     i i i i i
        {YELLOW}    |~~~~~~~~~|
        {MAGENTA}   |  SELAMAT |
        {CYAN}   | ULANG TAHUN |
        {RED}    \_________/
        {RESET}
    """,
    f"""
        {YELLOW}       i i i
        {YELLOW}    |~~~~~~~~~|
        {MAGENTA}   |  SELAMAT |
        {CYAN}   | ULANG TAHUN |
        {RED}    \_________/
        {RESET}
    """,
    f"""
        {YELLOW}     i i i i
        {YELLOW}    |~~~~~~~~~|
        {MAGENTA}   |  SELAMAT |
        {CYAN}   | ULANG TAHUN |
        {RED}    \_________/
        {RESET}
    """
]

def cake_animation():
    for _ in range(6):
        clear()
        print(cake_frames[_ % len(cake_frames)])
        time.sleep(0.5)

def main():
    clear()
    slow_print(f"{CYAN}✨✨✨ Hai, seseorang yang spesial... ✨✨✨{RESET}", 0.07)
    time.sleep(1)
    slow_print(f"{MAGENTA}Hari ini adalah hari yang luar biasa... 🎉{RESET}", 0.07)
    time.sleep(1)
    slow_print(f"{YELLOW}Karena hari ini adalah hari ulang tahunmu! 🥳{RESET}", 0.07)
    time.sleep(1)

    cake_animation()

    slow_print(f"{GREEN}🎂 Semoga panjang umur, sehat selalu, dan bahagia terus ya! 🎂{RESET}", 0.06)
    time.sleep(1)
    slow_print(f"{BLUE}🌟 Jangan lupa bersyukur dan tetap semangat mengejar mimpi! 🌟{RESET}", 0.06)
    time.sleep(1)
    slow_print(f"{MAGENTA}🎈 Selamat Ulang Tahun 🎈{RESET}", 0.1)
    time.sleep(0.5)
    slow_print(f"{CYAN}~ Dari Python dengan cinta 💖 ~{RESET}", 0.08)

if __name__ == "__main__":
    main()

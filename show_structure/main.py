from colorama import Fore, Back, Style, init
from pathlib import Path

def show_dir(path, spaces):
    for item in path.iterdir():
        if item.is_file():
           print(f"{' ' * spaces} {Fore.RED +item.name}")
           item.write_text('')
        if item.is_dir():
           print(f"{' ' * spaces} {Fore.GREEN +item.name}")
           show_dir(item, spaces=spaces+4)


def main():
    spaces = 4
    current = Path('test')

    print(f'\n\n\nYour directory is: {Fore.YELLOW +current.name}\n\n\n')
    print(f'{Fore.YELLOW +current.name}')
    show_dir(current, spaces=spaces)
    

if __name__ == '__main__':
    main()
import sys
from pathlib import Path
from colorama import Fore

def main():
    if len(sys.argv) > 1:
        print(sys.argv)
        directory = Path(sys.argv[1])
        log_level = sys.argv[2]
    else:
        print('No path in the request!')
        return
    
    


if __name__ == "__main__":
    main()

# To start:
# python main.py ./log_file.txt error  
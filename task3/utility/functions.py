from pathlib import Path
current_dir = Path(__file__).parent

def parse_log_line(line: str) -> dict:
    pass

def load_logs(file_path: str) -> list:
    
    path_to_file = Path(file_path)
    if not path_to_file.is_absolute():
        path_to_file = current_dir / path_to_file
    if not path_to_file.exists():
        print(f'The path {path_to_file} does not exist!')
    elif not path_to_file.is_file:
        print(f'The path {path_to_file} does not lead to a file!')
    else:
        print(path_to_file)


    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            logs = [el.rstrip() for el in file.readlines()]
            for log in logs:
                log = log.split()
                logs.append()
    except FileNotFoundError:
        print("Can't gat file with logs.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    pass

def count_logs_by_level(logs: list) -> dict:
    pass

def display_log_counts(counts: dict):
    pass



if __name__ == "__main__":
    pass

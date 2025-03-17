from pathlib import Path
import collections
LEVELS = {'INFO', 'ERROR', 'DEBUG', 'WARNING'}
current_dir = Path(__file__).parent

def parse_log_line(line: str) -> dict:
    log = line.split()
    return {'log_date':log[0],
            'log_time':log[1],
            'log_level':log[2],
            'log_message':' '.join(log[3:])}

def load_logs(file_path: str) -> list:
    path_to_file = Path(file_path)
    if not path_to_file.is_absolute():
        path_to_file = current_dir / path_to_file

    logs_prepr = []
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            logs = [el.rstrip() for el in file]
            for log in logs:                
                logs_prepr.append(parse_log_line(log))
    except FileNotFoundError:
        print("Can't gat the file with logs.")
    except UnicodeDecodeError:
        print("Wrong format of the file with logs.")
    return logs_prepr

def filter_logs_by_level(logs: list, level: str) -> list:
    lev = level.upper()
    if lev in LEVELS:
        filtred_logs = [log for log in logs if lev == log['log_level']]
        print(f"\nLog details for {lev} level:")
        for log in filtred_logs:
            print(f'{log['log_date']} {log['log_time']} - {log['log_message']}')
    else:
        print(f'Level {lev} unknown! You can try INFO, ERROR, DEBUG, WARNING.')

def count_logs_by_level(logs: list) -> dict:
    list_of_levels = [log['log_level'] for log in logs]
    counts = collections.Counter(list_of_levels)
    return counts
    

def display_log_counts(counts: dict):
    print(f"\n{"Logging level":<15}|{"Number":<10}")
    print('-'*15 + '|' + '-'*10)
    for key, value in counts.items():
        print(f"{key:<15}|{value:<10}")


if __name__ == "__main__":
    pass

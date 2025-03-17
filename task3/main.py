import sys
from utility import load_logs, display_log_counts, count_logs_by_level, filter_logs_by_level

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        print('No path in the request!')
        return
    logs = load_logs(directory)
    if logs:     
        display_log_counts(count_logs_by_level(logs))
        if len(sys.argv) > 2:
            log_level = sys.argv[2]
            filter_logs_by_level(logs, log_level)

    
    


if __name__ == "__main__":
    main()

# To start:
# python main.py ./log_file.txt error  
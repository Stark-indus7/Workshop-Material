# This project analyzes logs and provides detailed reports on errors and usage.
# Implement the code here

import re

def analyze_logs(log_file):
    error_count = 0
    error_summary = {}

    with open(log_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                error_count += 1
                error_type = re.search(r'ERROR: (.*?):', line)
                if error_type:
                    error = error_type.group(1)
                    if error in error_summary:
                        error_summary[error] += 1
                    else:
                        error_summary[error] = 1

    print(f'Total Errors: {error_count}')
    print('Error Summary:')
    for error, count in error_summary.items():
        print(f'{error}: {count}')

# Example usage
analyze_logs('application.log')

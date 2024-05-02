#!/usr/bin/python3
'''This a script for parsing HTTP request logs.
'''
import re


def extract_input(input_line):
    '''Extracting sections of a line of an HTTP request log.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = r'{}\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Printing the accumulated statistics of the HTTP request log.
    '''
    print('Total File Size: {:,} bytes'.format(total_file_size), flush=True)
    print('Status Codes Statistics:')
    for status_code, num in sorted(status_codes_stats.items()):
        if num > 0:
            print('{}: {}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updating the metrics from a given HTTP request log.

    Args:
        line (str): Line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    try:
        line_info = extract_input(line)
        status_code = line_info.get('status_code', '0')
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
        total_file_size += line_info['file_size']
    except Exception as e:
        print("Error:", e)
    return total_file_size


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

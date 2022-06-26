#!/usr/bin/python3
import requests
import re

def get_contrib_cal_data(user: str) -> dict[str, int]:
    """Retrieve the GitHub contribution calendar data
    of a user.
    
    Args:
        user (str): The github username contribution data to retrieve from

    Return:
        contrib_cal_data (dict): Contribution calendar data
    """
    
    contrib_url = f"https://github.com/users/{user}/contributions"
    contrib_cal_data: dict[str, int] = {}
    contributions = requests.get(contrib_url).text

    for line in contributions.split('\n'):
        match = re.search('data-count="(\d+)".*data-date="(\d+-\d+-\d+)"', line)

        if not match:
            continue
        if match.group(1) != b'0':
            contrib_cal_data[match.group(2)] = int(match.group(1))

    return contrib_cal_data


def main():
    contribution_data = get_contrib_cal_data('h4r1337')
    print(contribution_data)

if __name__ == "__main__":
    main()

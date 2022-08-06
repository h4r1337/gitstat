#!/usr/bin/env python3
import requests
import re
from pytermgui import tim, terminal, ColorSystem


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
        match = re.search('data-date="(\d+-\d+-\d+)".*data-level="(\d+)"', line)

        if not match:
            continue
        if match.group(1) != b'0':
            contrib_cal_data[match.group(1)] = int(match.group(2))

    return contrib_cal_data

def render_contrib_cal(data: dict) -> None:
    buff = ""
    for y_pos in range(0, 7):
        for x_pos in range(53):
            buff += "[57;211;83]▢"

        buff += "[/]\n"

    system = ColorSystem.TRUE
    terminal.forced_colorsystem = system

    tim.print(buff)

def main():
    contribution_data = get_contrib_cal_data('h4r1337')
    render_contrib_cal(contribution_data)

if __name__ == "__main__":
    main()

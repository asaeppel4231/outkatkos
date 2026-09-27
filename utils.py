#!/usr/bin/env python3
# This file (utils.py) is part of the outkatkos project.
# SPDX-License-Identifier: MIT
# Partial AI generated

import sys

def get_advertising_text(template_path: str) -> str:
    try:
        with open(template_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def get_i(lang: str, is_team: bool) -> str:
    if lang == "de":
        if is_team:
            return "wir"
        else:
            return "ich"
    elif lang == "en":
        if is_team:
            return "we"
        else:
            return "I"
    # Language already checked by main

def get_verb(lang: str, is_team: bool):
    if lang == "de":
        if is_team:
            return "bedauern"
        else:
            return "bedauere"
    elif lang == "en":
        return "regret"

def parse_main_template(template_path: str, recipient: str, i: str,
    verb: str, server_name: str, date_start: str, date_end: str,
    time_start: str, time_end: str, sender: str, advertising: str):
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"[outkatkos] ❌ Error: Template {template_path} is missing!")
        sys.exit(1)

    text = text.replace("${0}", recipient)
    text = text.replace("${1}", i)
    text = text.replace("${2}", verb)
    text = text.replace("${3}", server_name)
    text = text.replace("${4}", date_start)
    text = text.replace("${5}", date_end)
    text = text.replace("${6}", time_start)
    text = text.replace("${7}", time_end)
    text = text.replace("${8}", sender)
    text = text.replace("${9}", advertising)
    
    return text

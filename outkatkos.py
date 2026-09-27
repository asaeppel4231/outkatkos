#!/usr/bin/env python3
#
# Partial AI generated
# 

from i18n import parser_help_texts, error_texts, email_subject, information_texts
import utils

import os
import sys
import json
import argparse
import smtplib

import locale

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CONFIG_PATH = os.environ.get("OUTKATKOS_CONFIG_FILE_PATH", os.path.expanduser("config.json") if os.path.exists("config.json") else "NO_VALID_PATH")

def load_config(loc_str: str):
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(error_texts["config_nf"][loc_str].format(CONFIG_PATH=CONFIG_PATH))
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="outkatkos CLI")
    loc = locale.getlocale()
    loc_str = loc[0] # we don't like to have the charset, too
    loc_str = loc_str[:2] # first 2 characters of the language (e.g. just "de" of "de_DE")

    if loc_str not in ("de", "en"):
        print(f"Unsupported language: {loc[0]}")
        sys.exit(1)
    
    parser.add_argument("--ds", help=parser_help_texts["--ds"][loc_str], required=True)
    parser.add_argument("--de", help=parser_help_texts["--de"][loc_str], required=True)
    parser.add_argument("--ts", help=parser_help_texts["--ts"][loc_str], required=True)
    parser.add_argument("--te", help=parser_help_texts["--te"][loc_str], required=True)
    parser.add_argument("--server", help=parser_help_texts["--server"][loc_str], required=True)
    parser.add_argument("--sender", help=parser_help_texts["--sender"][loc_str], required=True)
    parser.add_argument("--send-now", action="store_true", help=parser_help_texts["--send-now"][loc_str])
    parser.add_argument("--min", action="store_true", help=parser_help_texts["--min"][loc_str])

    args = parser.parse_args()
    config = load_config(loc_str)

    base_dir = os.path.dirname(CONFIG_PATH)
    base_template_file = os.path.join(base_dir, "templates", f"{loc_str}.txt")
    
    recipients_dict = config.get("recipients", {})
    if not recipients_dict:
        print(error_texts["no_recipients"][loc_str].format(CONFIG_PATH=CONFIG_PATH))
        return

    is_team = config.get("team-or-not", 0)
    i: str = utils.get_i(loc_str, is_team)
    verb: str = utils.get_verb(loc_str, is_team)

    advertising = utils.get_advertising_text(os.path.join(base_dir, "templates", f"advertising_{loc_str}.txt"))
    
    if args.send_now:
        provider = config.get("email-provider")
        smtp_server = f"smtp.{provider}"
        smtp_port = 587
        sender_email = f"{config.get('email-name')}@{provider}"
        password = config.get("email-password")

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, password)
        except Exception as e:
            print(error_texts["smtp_error"][loc_str].format(e=e))
        
        print(information_texts["start_sending"][loc_str].format(count_persons=len(recipients_dict)))
        
    for person_name, email_address in recipients_dict.items():
        clean_email = email_address.replace("\\", "").strip()
        body = utils.parse_main_template(base_template_file, person_name, i, verb, args.server, args.ds, args.de, args.ts, args.te, args.sender, advertising)
        msg = MIMEMultipart()
        if args.send_now:
            msg['From'] = sender_email
            msg['To'] = clean_email
            msg['Subject'] = email_subject[loc_str].format(server=args.server)
            msg.attach(MIMEText(body, 'plain'))
            server.sendmail(sender_email, clean_email, msg.as_string())
            print(information_texts["email_sent"][loc_str].format(person_name=person_name, clean_email=clean_email))
        else:
            if not args.min:
                print(f"Recipient: {person_name} ({clean_email})")
                print("")
            print(body)
            if not args.min:
                print("")
            
    if args.send_now:               
        server.quit()
        print(information_texts["all_emails_sent"][loc_str])
        
if __name__ == "__main__":
    main()


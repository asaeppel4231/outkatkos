#!/usr/bin/env python3
# This file (i18n.py) is part of the outkatkos project.
# SPDX-License-Identifier: MIT
# Error and information texts partial generated using AI

parser_help_texts = {
    "--ds": {
        "de": "Datum des Starts des Serverausfalls",
        "en": "Date of the start of the outage of the server"
    },
    "--de": {
        "de": "Enddatum des Serverausfalls",
        "en": "Date of the end of the outage of the server"
    },
    "--ts": {
        "de": "Zeit am Startdatum, wann der Serverausfall beginnt",
        "en": "Time of the start date of the outage of the server begins"
    },
    "--te": {
        "de": "Zeit am Enddatum, wann der Serverausfall vorbei ist",
        "en": "Time of the end date of the outage of the server"
    },
    "--server": {
        "de": "Name des Servers, der ausfällt",
        "en": "Name of the server which has that outage"
    },
    "--sender": {
        "de": "Name der Person, die die Meldung des Serverausfalls verschickt",
        "en": "Name of the person who sends the report of the server-outage"
    },
    "--send-now": {
        "de": "Die Meldung per SMTP (Email) senden statt sie in der Standardausgabe auszugeben",
        "en": "Send the report now by using SMTP (Email) instead of printing it to stdout"
    },
    "--min": {
        "de": "Nur den Nachrichteninhalt ausgeben, wenn die Email nicht gesendet wird",
        "en": "Print only the message content for the first person if no emails should sended"
    }
}

error_texts = {
    "config_nf": {
        "de": "[outkatkos] ❌ Fehler: Konfigurations im Pfad {CONFIG_PATH} wurde nicht gefunden!",
        "en": "[outkatkos] ❌ Error: Configuration under {CONFIG_PATH} not found !"
    },
    "no_recipients": {
        "de": "[outkatkos] ❌ Fehler: Keine Empfänger in der Konfigurationsdatei {CONFIG_PATH} definiert !",
        "en": "[outkatkos] ❌ Error: No recipients in configuration {CONFIG_PATH} !"
    },
    "smtp_error": {
        "de": "[outkatkos] ❌ SMTP-Fehler: {e}",
        "en": "[outkatkos] ❌ SMTP-Error: {e}"
    }
}

email_subject = {
    "de": "Serverausfall von {server}",
    "en": "Outage of {server}"
}

information_texts = {
    "start_sending": {
        "de": "[outkatkos] 🚀 Starte Echt-Versand  an {count_persons} Personen...",
        "en": "[outkatkos] 🚀 Start sending emails to {count_persons} People..."
    },
    "email_sent": {
        "de": "[outkatkos] -> Email erfolgreich an {person_name} ({clean_email}) gesendet.",
        "en": "[outkatkos] -> Email succesfully sent to {person_name} ({clean_email})."
    },
    "all_emails_sent": {
        "de": "[outkatkos] ✨ Alle Benachrichtigungen erfolgreich verschickt!",
        "en": "[outkatkos] ✨ All emails were successfully sent !"
    }
}

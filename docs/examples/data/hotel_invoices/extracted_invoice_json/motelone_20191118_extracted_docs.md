# File Documentation: motelone_20191118_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json/motelone_20191118_extracted.json`
- **Size**: 2,648 bytes (2,638 characters)
- **Lines**: 80
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "Hotel Information": {
            "Name": "Motel One Berlin-Hauptbahnhof",
            "Address": "Invalidenstraße 54, 10557 Berlin"
        },
        "Guest Information": {
            "Name": "APImeiseter Consulting GmbH",
            "Address": "Friedrichstrasse 123, 10117 Berlin, Deutschland"
        },
        "Invoice Information": {
            "Datum": "18.11.2019",
            "Rechnungsnummer": "534717906",
            "Reservierungsnummer": "534629153/1",
            "Zimmer": "1011",
            "Anreise": "18.11.2019",
            "Abreise": "19.11.2019"
        },
        "Charges": [
            {
                "Bezeichnung": "Bestpreis mit Frühstück",
                "MWST-Satz": null,
                "Menge": null,
                "Einzelpreis EUR": "80,50",
                "Gesamtpreis EUR": "80,50"
            },
            {
                "Bezeichnung": "Frühstück",
                "MWST-Satz": "19,00%",
                "Menge": "1",
                "Einzelpreis EUR": "11,50",
                "Gesamtpreis EUR": "11,50"
            },
            {
                "Bezeichnung": "Logis",
                "MWST-Satz": "7,00%",
                "Menge": "1",
                "Einzelpreis EUR": "69,00",
                "Gesamtpreis EUR": "69,00"
            },
            {
                "Bezeichnung": "Saldo Leistungen",
                "MWST-Satz": null,
                "Menge": null,
                "Einzelpreis EUR": null,
                "Gesamtpreis EUR": "80,50"
            }
        ],
        "Payments": [
            {
                "Datum": "18.11.2019",
                "Zahlungsart": "Mastercard",
                "Karten-Nr.": "************5052",
                "Betrag Devisen": null,
                "Zahlung EUR": "-80,50"
            }
        ],
        "Saldo Zahlungen": "-80,50",
        "Rechnungsbetrag": "0,00",
        "Steuerbeträge": [
            {
                "Steuersatz": "19,00 %",
                "Netto EUR": "9,66",
                "Steuer EUR": "1,84",
                "Brutto EUR": "11,50"
            },
            {
                "Steuersatz": "7,00 %",
                "Netto EUR": "64,49",
                "Steuer EUR": "4,51",
                "Brutto EUR": "69,00"
            }
        ],
        "WLAN Information": {
            "AGB bestätigen und lossurfen!": "Einfach AGB bestätigen und lossurfen!",
            "WLAN-Support gewünscht?": "Kostenlose Hotline aus Deutschland: 0800-4357576, Kostenlose Hotline aus anderen Ländern: +49-241-70539605"
        },
        "Front Office Agent": "Daniel Martelock"
    }
]
```

---

## High-Level Overview

This is a configuration/data file.

---

## Detailed Walkthrough

---

## Performance & Security Notes

- Verify that sensitive data is not committed to version control
- Validate configuration values

---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

Refer to the project README for instructions on how to use this file.

---

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json/motelone_20191118_extracted.json`*

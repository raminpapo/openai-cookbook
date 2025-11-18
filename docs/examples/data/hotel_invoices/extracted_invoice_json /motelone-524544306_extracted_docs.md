# File Documentation: motelone-524544306_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /motelone-524544306_extracted.json`
- **Size**: 2,946 bytes (2,937 characters)
- **Lines**: 92
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "Hotel Information": {
            "Name": "Motel One Berlin-Tiergarten",
            "Address": "An der Urania 12/14 - 10787 Berlin"
        },
        "Guest Information": {
            "Name": "Apimeister Consulting GmbH",
            "Address": "Friedrichstrasse 123, 10117 Berlin, Deutschland"
        },
        "Invoice Information": {
            "Datum": "25.02.2019",
            "Rechnungsnummer": "524544306",
            "Reservierungsnummer": "524414809/1",
            "Zimmer": "519",
            "Anreise": "25.02.2019",
            "Abreise": "27.02.2019"
        },
        "Charges": {
            "Gast": "Walter, Jens",
            "Zimmer": "519",
            "Zeitraum": "25.02.2019 bis 27.02.2019",
            "Leistungen": [
                {
                    "Bezeichnung": "Best Public Rate mit Frühstück",
                    "MWST-Satz": null,
                    "Menge": 2,
                    "Einzelpreis EUR": 80.5,
                    "Gesamtpreis EUR": 161.0
                },
                {
                    "Bezeichnung": "Frühstück",
                    "MWST-Satz": "19,00%",
                    "Menge": 2,
                    "Einzelpreis EUR": 11.5,
                    "Gesamtpreis EUR": 23.0
                },
                {
                    "Bezeichnung": "Logis",
                    "MWST-Satz": "7,00%",
                    "Menge": 2,
                    "Einzelpreis EUR": 69.0,
                    "Gesamtpreis EUR": 138.0
                }
            ],
            "Saldo Leistungen": {
                "Währung": "EUR",
                "Betrag": 161.0
            }
        },
        "Payments": {
            "Datum": "25.02.2019",
            "Zahlungsart": "Mastercard",
            "Karten-Nr.": "****2825",
            "Betrag Devisen": null,
            "Zahlung EUR": -161.0
        },
        "Saldo Zahlungen": -161.0,
        "Rechnungsbetrag": 0.0,
        "Steuerbeträge": [
            {
                "Steuersatz": "19,00%",
                "Netto EUR": 19.33,
                "Steuer EUR": 3.67,
                "Brutto EUR": 23.0
            },
            {
                "Steuersatz": "7,00%",
                "Netto EUR": 128.97,
                "Steuer EUR": 9.03,
                "Brutto EUR": 138.0
            }
        ],
        "WLAN-Zugangsdaten": {
            "Einfach AGB bestätigen und lossurfen!": null,
            "WLAN-Support gewünscht?": null,
            "Kostenlose Hotline aus Deutschland": "0800-4357526",
            "Kostenlose Hotline aus anderen Ländern": "+49-241-70530965"
        },
        "Hotel Manager": {
            "Name": "Sebastian Gahm",
            "Title": "Front Office Manager"
        },
        "Additional Information": {
            "Newly Opened": [
                "Motel One Bonn-Beethoven",
                "Motel One Leipzig-Post"
            ]
        }
    },
    {}
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json /motelone-524544306_extracted.json`*

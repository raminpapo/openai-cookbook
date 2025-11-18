# File Documentation: madison_497810_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json/madison_497810_extracted.json`
- **Size**: 3,233 bytes (3,219 characters)
- **Lines**: 101
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "Hotel Information": {
            "Name": "MADISON Hotel GmbH",
            "Address": "Schaarsteinweg 4, 20459 Hamburg",
            "Contact": {
                "Phone": "+49.40.37 666-0",
                "Fax": "+49.40.37 666-137",
                "Email": "info@madisonhotel.de",
                "Website": "madisonhotel.de"
            },
            "Geschäftsführer": "Martens Heald, Thomas Kleinertz",
            "AG": "Hamburg HRB 47881",
            "VAT": "DE118 686 407",
            "Bank": {
                "Name": "HypoVereinsbank",
                "IBAN": "DE48 2003 0000 0003 6027 111",
                "BIC": "HYVEDEMM300"
            }
        },
        "Guest Information": {
            "Company": "APImeiseter Consulting GmbH",
            "Address": "Friedrichstr. 123, 10117 Berlin",
            "Guest Name": "Herr Jens Walter"
        },
        "Invoice Information": {
            "Invoice Number": "497810 /",
            "Date": "26.04.19",
            "Room Number": "403",
            "Arrival Date": "22.04.19",
            "Departure Date": "26.04.19",
            "Page": "1 of 1",
            "User ID": "RIL"
        },
        "Charges": [
            {
                "Datum": "22.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "23.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "24.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "25.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "26.04.19",
                "Beschreibung": "Mastercard IFC",
                "Belastung": null,
                "Entlastung": 440.0
            }
        ],
        "Summary": {
            "Total": {
                "Netto EUR": 411.21,
                "MwSt. EUR": 28.79,
                "Brutto EUR": 440.0
            },
            "Saldo": {
                "Amount": 0.0,
                "Currency": "EUR"
            }
        },
        "Tax Details": {
            "Total inkl. MwSt.": {
                "Netto EUR": 411.21,
                "MwSt. 7%": 28.79,
                "Brutto EUR": 440.0
            }
        },
        "Payment Information": {
            "Finanzamt": "Hamburg Mitte",
            "Steuernummer": "48/741/01228",
            "Kreditkartendetails": {
                "Kartennummer": "XXXXXXXXXXXX2825",
                "Verfallsdatum": "XX/XX",
                "Terminal ID": "6928491"
            },
            "Vorgangsnummer": "164984932",
            "Beleg Nr.": "7635",
            "Transaktionsbetrag": 440.0,
            "Genehmigungsnr.": "626349",
            "Genehmigungscode": "626349"
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json/madison_497810_extracted.json`*

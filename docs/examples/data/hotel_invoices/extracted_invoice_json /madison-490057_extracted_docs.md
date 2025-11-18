# File Documentation: madison-490057_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /madison-490057_extracted.json`
- **Size**: 3,464 bytes (3,447 characters)
- **Lines**: 107
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
                "Phone": "+49.40.37 66 0",
                "Fax": "+49.40.37 66 137",
                "Email": "info@madisonhotel.de",
                "Website": "madisonhotel.de"
            },
            "Geschäftsführer": "Marlies Head, Thomas Kleinertz",
            "Bank": {
                "Name": "HypoVereinsbank",
                "BLZ": "200 300 00",
                "Konto-Nr": "360 27 11",
                "IBAN": "DE40 2003 0000 0036 0271 11",
                "BIC": "HYVEDEMM300"
            },
            "VAT": "DE118 686 407",
            "AG Hamburg HRB": "47881"
        },
        "Guest Information": {
            "Company": "APImeleister Consulting GmbH",
            "Address": "Friedrichstr. 123, 10117 Berlin",
            "Guest Name": "Herr Jens Walter"
        },
        "Invoice Information": {
            "Rechnungs-Nr": "490057 /",
            "Date": "15.02.19",
            "Room": "336",
            "Arrival": "10.02.19",
            "Departure": "15.02.19",
            "Page": "1 of 1",
            "User ID": "SMA"
        },
        "Charges": [
            {
                "Datum": "10.02.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "11.02.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "12.02.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "13.02.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "14.02.19",
                "Beschreibung": "Übernachtung exklusive Frühstück",
                "Belastung": 110.0,
                "Entlastung": null
            },
            {
                "Datum": "15.02.19",
                "Beschreibung": "Mastercard IFC",
                "Belastung": 550.0,
                "Entlastung": null
            }
        ],
        "Summary": {
            "Umsatzsteuer Detail": {
                "Netto EUR": 514.02,
                "MwSt. EUR": 35.98,
                "Brutto EUR": 550.0
            },
            "Total": {
                "Total incl. MwSt.": 550.0,
                "Saldo": 0.0
            }
        },
        "Payment Information": {
            "Finanzamt": "Hamburg Mitte",
            "Steuernummer": "47/471/01228",
            "Kreditkartendetails": {
                "Kartenunternehmen": "Mastercard",
                "Kreditkartennummer": "154498432",
                "Verfallsdatum": "XX/XX",
                "Terminal ID": "69264961",
                "Beleg Nr.": "6692",
                "Transaktionsbetrag": 550.0,
                "Genehmigter Betrag": 550.0,
                "Genehmigungsnr.": "258692"
            }
        }
    },
    {
        "hotel_information": {
            "name": "THE MADISON",
            "location": "HAMBURG"
        }
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json /madison-490057_extracted.json`*

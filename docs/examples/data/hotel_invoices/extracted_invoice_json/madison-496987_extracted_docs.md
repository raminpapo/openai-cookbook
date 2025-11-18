# File Documentation: madison-496987_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json/madison-496987_extracted.json`
- **Size**: 3,740 bytes (3,725 characters)
- **Lines**: 115
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
            "Geschäftsführer": "Marlies Head, Thomas Kleinertz",
            "Register": "AG Hamburg HRB 47881",
            "VAT ID": "DE118 696 407",
            "Bank": {
                "Name": "HypoVereinsbank",
                "IBAN": "DE84 20030000 0003627111",
                "BIC": "HYVEDEMM300"
            }
        },
        "Guest Information": {
            "Company": "APimeister Consulting GmbH",
            "Address": "Friedrichstr. 123, 10117 Berlin",
            "Guest Name": "Herr Jens Walter"
        },
        "Invoice Information": {
            "Invoice Number": "496987 /",
            "Date": "18.04.19",
            "Room Number": "439",
            "Arrival Date": "15.04.19",
            "Departure Date": "18.04.19",
            "Page": "1 of 1",
            "User ID": "LBE"
        },
        "Charges": [
            {
                "Datum": "15.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück*",
                "Belastung": "110.00",
                "Entlastung": null
            },
            {
                "Datum": "16.04.19",
                "Beschreibung": "Frühstück **",
                "Belastung": "20.00",
                "Entlastung": null
            },
            {
                "Datum": "16.04.19",
                "Beschreibung": "CHECK#1000540",
                "Belastung": null,
                "Entlastung": "20.00"
            },
            {
                "Datum": "16.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück*",
                "Belastung": "110.00",
                "Entlastung": null
            },
            {
                "Datum": "17.04.19",
                "Beschreibung": "Übernachtung exklusive Frühstück*",
                "Belastung": "110.00",
                "Entlastung": null
            },
            {
                "Datum": "18.04.19",
                "Beschreibung": "Frühstück **",
                "Belastung": "20.00",
                "Entlastung": null
            },
            {
                "Datum": "18.04.19",
                "Beschreibung": "Mastercard IFC",
                "Belastung": null,
                "Entlastung": "370.00"
            }
        ],
        "Summary": {
            "Umsatzsteuer Detail": [
                {
                    "MwSt. 7%": {
                        "Netto EUR": "308.41",
                        "MwSt. EUR": "21.59",
                        "Brutto EUR": "330.00"
                    }
                },
                {
                    "MwSt. 19%": {
                        "Netto EUR": "33.61",
                        "MwSt. EUR": "6.39",
                        "Brutto EUR": "40.00"
                    }
                }
            ],
            "Total": {
                "Netto EUR": "342.02",
                "MwSt. EUR": "27.98",
                "Brutto EUR": "370.00"
            },
            "Saldo": "0.00 EUR"
        },
        "Payment Information": {
            "Kreditkartennr.": "XXXX XXXX XXXX 2825",
            "Verfallsdatum": "XX/XX",
            "Terminal ID": "6826492",
            "Kreditkarteninstitut": "15649832",
            "Beleg Nr.": "25903",
            "Transaktionsbetrag": "370.00",
            "Genehmigter Betrag": "370.00",
            "Genehmigungscode": "960959"
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json/madison-496987_extracted.json`*

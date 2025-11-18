# File Documentation: madison_folio_g_cp_efolio5976009_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json/madison_folio_g_cp_efolio5976009_extracted.json`
- **Size**: 3,605 bytes (3,588 characters)
- **Lines**: 115
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "MADISON Hotel GmbH",
            "address": "Schaartinsweg 4, 20459 Hamburg, Germany",
            "contact": {
                "phone": "+49.40.37 666-0",
                "fax": "+49.40.37 666-137",
                "email": "info@madisonhotel.de",
                "website": "madisonhotel.de"
            },
            "managing_directors": "Marlies Head, Thomas Kleinertz",
            "registration": {
                "court": "AG Hamburg HRB 47281",
                "VAT_ID": "DE118 696 407"
            },
            "bank_details": {
                "bank_name": "HypoVereinsbank",
                "IBAN": "DE84 2003 0000 0003 6027 11",
                "BIC": "HYVEDEMM300"
            }
        },
        "guest_information": {
            "company": "APMeister Consulting GmbH",
            "address": "Friedrichstr. 123, 10117 Berlin",
            "guest_name": "Herr Jens Walter"
        },
        "invoice_information": {
            "invoice_number": "508189",
            "date": "09.08.19",
            "room_number": "438",
            "check_in": "04.08.19",
            "check_out": "09.08.19",
            "page": "1 of 1",
            "user_id": "WM"
        },
        "charges": [
            {
                "date": "04.08.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "05.08.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "06.08.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "07.08.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "08.08.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "09.08.19",
                "description": "Frühstück **",
                "charge": 20.0,
                "credit": null
            },
            {
                "date": "09.08.19",
                "description": "Mastercard IFC",
                "charge": null,
                "credit": 570.0
            }
        ],
        "summary": {
            "total_netto": 530.83,
            "total_mwst": 39.17,
            "total_brutto": 570.0,
            "saldo": 0.0
        },
        "tax_details": [
            {
                "rate": "7%",
                "netto": 16.81,
                "mwst": 1.18,
                "brutto": 20.0
            },
            {
                "rate": "19%",
                "netto": 514.02,
                "mwst": 35.98,
                "brutto": 550.0
            }
        ],
        "financial_information": {
            "bank": "Finanzamt Hamburg Mitte",
            "tax_number": "48/741/01228"
        },
        "credit_card_details": {
            "contract_number": "154584932",
            "card_number": "XXXXXXXXXXXX5052",
            "terminal_id": "52964893",
            "approval_code": "165942",
            "receipt_number": "93935",
            "transaction_amount": 570.0,
            "approved_amount": 570.0
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json/madison_folio_g_cp_efolio5976009_extracted.json`*

# File Documentation: madison_folio_g_cp_efolio5895707_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json/madison_folio_g_cp_efolio5895707_extracted.json`
- **Size**: 3,156 bytes (3,144 characters)
- **Lines**: 97
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "MADISON Hotel GmbH",
            "address": "Schaartvenweg 4, 20459 Hamburg",
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
            "bank": {
                "name": "HypoVereinsbank",
                "account_number": "360 27 11",
                "IBAN": "DE84 2003 0000 0003 6027 11",
                "BIC": "HYVEDEMM300"
            }
        },
        "guest_information": {
            "company": "APfmeister Consulting GmbH",
            "address": "Friedrichstr. 123, 10117 Berlin",
            "guest_name": "Herr Jens Walter"
        },
        "invoice_information": {
            "invoice_number": "505050 /",
            "date": "04.07.19",
            "room_number": "203",
            "check_in_date": "30.06.19",
            "check_out_date": "04.07.19",
            "page": "1 of 1",
            "user_id": "RIL"
        },
        "charges": [
            {
                "date": "30.06.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "01.07.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "02.07.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "03.07.19",
                "description": "Übernachtung exklusive Frühstück*",
                "charge": 110.0,
                "credit": null
            },
            {
                "date": "04.07.19",
                "description": "Mastercard IFC",
                "charge": null,
                "credit": 440.0
            }
        ],
        "tax_details": {
            "total_net_amount": 411.21,
            "total_vat": 28.79,
            "total_gross_amount": 440.0,
            "vat_7_percent": {
                "net_amount": 411.21,
                "vat_amount": 28.79,
                "gross_amount": 440.0
            }
        },
        "balance": {
            "total": 440.0,
            "paid": 440.0,
            "balance_due": 0.0
        },
        "payment_information": {
            "credit_card_number": "XXXXXXXXXXXX5052",
            "authorization_code": "114540",
            "transaction_number": "440.00",
            "approval_amount": "440.00",
            "terminal_id": "82684691",
            "approval_code": "114540",
            "receipt_number": "8250",
            "verification_number": "XXXXXX",
            "contract_number": "156648932"
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json/madison_folio_g_cp_efolio5895707_extracted.json`*

# File Documentation: hampton_20190411_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /hampton_20190411_extracted.json`
- **Size**: 5,246 bytes (5,210 characters)
- **Lines**: 158
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "Hampton by Hilton Hamburg City Centre",
            "address": "Nordkanalstrasse 18, 20097 Hamburg",
            "phone": "+49(0)40-302372-0",
            "fax": "+49(0)40-302372-100"
        },
        "guest_information": {
            "name": "APIMEISTER CONSULTING GMBH",
            "address": "FRIEDRICHSTR. 123, 10117 BERLIN, GERMANY",
            "guest_name": "JENS WALTER"
        },
        "invoice_information": {
            "invoice_number": "31611",
            "confirmation_number": "92353607",
            "VAT": "DE258969536",
            "folio_no": "126069 A"
        },
        "stay_information": {
            "room_no": "216",
            "arrival_date": "04/11/2019 19:00:00",
            "departure_date": "08/11/2019",
            "adults/children": "1/0",
            "room_rate": "99.00",
            "rate_plan": "2G2",
            "HH #": "null"
        },
        "charges": [
            {
                "date": "04/11/2019",
                "description": "MC *5620",
                "cashier_id": "ANPE",
                "ref_no": "437200",
                "guest_charges": "-476.00",
                "credit": "null",
                "balance": "null"
            },
            {
                "date": "04/11/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "437361",
                "guest_charges": "null",
                "credit": "€94.05",
                "balance": "null"
            },
            {
                "date": "05/11/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "437361",
                "guest_charges": "null",
                "credit": "€4.95",
                "balance": "null"
            },
            {
                "date": "05/11/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "437770",
                "guest_charges": "null",
                "credit": "€134.05",
                "balance": "null"
            },
            {
                "date": "05/11/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "437770",
                "guest_charges": "null",
                "credit": "€4.95",
                "balance": "null"
            },
            {
                "date": "06/11/2019",
                "description": "GUEST ROOM",
                "cashier_id": "ANPE",
                "ref_no": "438200",
                "guest_charges": "null",
                "credit": "€114.05",
                "balance": "null"
            },
            {
                "date": "06/11/2019",
                "description": "BREAKFAST",
                "cashier_id": "ANPE",
                "ref_no": "438200",
                "guest_charges": "null",
                "credit": "€4.95",
                "balance": "null"
            },
            {
                "date": "07/11/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "438616",
                "guest_charges": "null",
                "credit": "€114.05",
                "balance": "null"
            }
        ]
    },
    {
        "hotel_information": {
            "name": "Hampton by Hilton Hamburg City Centre",
            "address": "Nordkanalstrasse 18, 20097 Hamburg",
            "phone": "+49(0)40-302372-0",
            "fax": "+49(0)40-302372-100"
        },
        "guest_information": {
            "name": "APIMEISTER CONSULTING GMBH",
            "address": "FRIEDRICHSTR. 123, 10117 BERLIN, GERMANY",
            "guest_name": "JENS WALTER"
        },
        "invoice_information": {
            "invoice_number": "31611",
            "confirmation_number": "92353607",
            "VAT_number": "DE259985536",
            "folio_number": "126609 A"
        },
        "stay_information": {
            "room_number": "216",
            "arrival_date": "04/11/2019 19:09:00",
            "departure_date": "08/11/2019",
            "adults_children": "1/0",
            "rate_plan": "2G2"
        },
        "charges": [
            {
                "date": "07/11/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "438616",
                "guest_charges": "€4.95",
                "credit": null,
                "balance": "€0.00"
            }
        ],
        "tax_summary": {
            "trade_receivable_net_19%": "€16.64",
            "trade_receivable_net_7%": "€0.00",
            "trade_receivable_net_7.00%": "€426.36",
            "VAT_19%": "€3.16",
            "F&B_VAT_7%": "€0.00",
            "VAT_7%": "€29.84",
            "trade_receivables_incl_VAT": "€476.00"
        },
        "payment_information": {
            "approval_amount": "€476.00",
            "approval_code": "109423",
            "transaction_id": "437200",
            "balance": "-€476.00"
        },
        "signature": "Guest Signature",
        "note": "Debit related verbiage"
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json /hampton_20190411_extracted.json`*

# File Documentation: mercure-37816396_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /mercure-37816396_extracted.json`
- **Size**: 1,930 bytes (1,927 characters)
- **Lines**: 57
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "Mercure Hotel Bochum City",
            "address": "Massenbergstrasse 19-21, 44787 Bochum",
            "contact": {
                "phone": "+49 234 9690",
                "fax": "+49 234 9692222",
                "email": "H0707@accor.com",
                "website": "mercure.com | accorhotels.com"
            }
        },
        "guest_information": {
            "company": "Apimeister Consulting GmbH",
            "address": "Friedrichstrasse 123, 10117 Berlin, Germany",
            "guest_name": "Herrn Jens Walter"
        },
        "invoice_information": {
            "invoice_number": "HA007 - 123123 - 37816396",
            "date": "05.07.19",
            "page": "1 von 1",
            "user_id": "IWINKING",
            "room_number": "1307",
            "arrival_date": "04.07.19",
            "departure_date": "05.07.19"
        },
        "charges": [
            {
                "date": "04.07.19",
                "description": "Übernachtung",
                "charge": 118.0,
                "credit": null
            },
            {
                "date": "05.07.19",
                "description": "Mastercard",
                "charge": null,
                "credit": 118.0
            }
        ],
        "summary": {
            "total_incl_vat": {
                "net_amount": 110.28,
                "vat_amount": 7.72,
                "gross_amount": 118.0
            },
            "vat_7_percent": {
                "net_amount": 110.28,
                "vat_amount": 7.72,
                "gross_amount": 118.0
            },
            "total": 118.0,
            "balance": 0.0
        },
        "message": "Vielen Dank für Ihren Aufenthalt im Mercure Bochum City. Wir wünschen Ihnen eine gute Heimreise und freuen uns schon heute auf einen erneuten Besuch in unserem Hotel. Ihr Mercure Hotel Bochum City."
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json /mercure-37816396_extracted.json`*

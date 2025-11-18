# File Documentation: invoice_schema.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/invoice_schema.json`
- **Size**: 1,644 bytes (1,644 characters)
- **Lines**: 59
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "string",
            "address": {
                "street": "string",
                "city": "string",
                "country": "string",
                "postal_code": "string"
            },
            "contact": {
                "phone": "string",
                "fax": "string",
                "email": "string",
                "website": "string"
            }
        },
        "guest_information": {
            "company": "string",
            "address": "string",
            "guest_name": "string"
        },
        "invoice_information": {
            "invoice_number": "string",
            "reservation_number": "string",
            "date": "YYYY-MM-DD",  
            "room_number": "string",
            "check_in_date": "YYYY-MM-DD",  
            "check_out_date": "YYYY-MM-DD"  
        },
        "charges": [
            {
                "date": "YYYY-MM-DD", 
                "description": "string",
                "charge": "number",
                "credit": "number"
            }
        ],
        "totals_summary": {
            "currency": "string",
            "total_net": "number",
            "total_tax": "number",
            "total_gross": "number",
            "total_charge": "number",
            "total_credit": "number",
            "balance_due": "number"
        },
        "taxes": [
            {
                "tax_type": "string",
                "tax_rate": "string",
                "net_amount": "number",
                "tax_amount": "number",
                "gross_amount": "number"
            }
        ]
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

*Documentation generated for `examples/data/hotel_invoices/invoice_schema.json`*

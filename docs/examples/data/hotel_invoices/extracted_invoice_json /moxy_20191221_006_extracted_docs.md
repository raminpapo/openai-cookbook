# File Documentation: moxy_20191221_006_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /moxy_20191221_006_extracted.json`
- **Size**: 3,290 bytes (3,289 characters)
- **Lines**: 102
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "MOXY Frankfurt Airport",
            "address": "Amelia-Mary-Earhart-Strasse 5, 60549 Frankfurt/Main",
            "phone": "+49 (0) 69 96759119",
            "email": "crew.frankfurtairport@moxyhotels.com",
            "website": "www.moxyfrankfurtairport.com"
        },
        "guest_information": {
            "name": "Jens Walter",
            "company": "API Meister Consulting GmbH",
            "address": "Friedrichstr. 123, 10117 Berlin, Germany",
            "room_no": "305",
            "arrival_date": "30.11.19",
            "departure_date": "01.12.19",
            "folio_no": "227638",
            "confirmation_no": "85111510",
            "cashier_no": "8370",
            "invoice_date": "01.12.19"
        },
        "invoice_information": {
            "date": "01.12.19",
            "description": "INVOICE"
        },
        "charges": [
            {
                "date": "21.11.19",
                "description": "Deposit Tax Transfer",
                "debit_eur": null,
                "credit_eur": "3.14"
            },
            {
                "date": "30.11.19",
                "description": "Accommodation",
                "debit_eur": "48.00",
                "credit_eur": null
            },
            {
                "date": "30.11.19",
                "description": "Deposit Transfer at C/I",
                "debit_eur": null,
                "credit_eur": "44.86"
            }
        ],
        "deposit_information": [
            {
                "date": "21.11.19",
                "deposit_folio_no": "225353",
                "deposit_amount": "48.00",
                "vat": "3.14"
            }
        ],
        "totals": {
            "total": "48.00",
            "balance_to_pay": "0.00"
        },
        "vat_details": {
            "total_incl_vat": {
                "net_eur": "44.86",
                "vat_eur": "3.14",
                "gross_eur": "48.00"
            },
            "vat_7_percent": {
                "net_eur": "44.86",
                "vat_eur": "3.14",
                "gross_eur": "48.00"
            },
            "deposit_7_percent": {
                "net_eur": "44.86",
                "vat_eur": "3.14",
                "gross_eur": "-48.00"
            }
        },
        "credit_card_details": {
            "merchant_no": null,
            "credit_card_no": "XXXXXXXXXXXX5052",
            "expiry_date": "XX/XX",
            "card_entry": null,
            "verification": null,
            "terminal_id": null,
            "receipt_no": null,
            "transaction_amount": "48.00",
            "approval_amount": "48.00",
            "approval_code": "A1848003"
        },
        "signature": {
            "card_holder": null
        },
        "entity_information": {
            "name": "QMHotel Germany GmbH",
            "chamber_of_commerce_number": "HRB 207980",
            "registered_office": "MÜNCHEN",
            "fiscal_number": "143/317/7200",
            "vat_id_number": "UID DE294499203",
            "authorized_representative": "Rune Fring",
            "bank": "NORDEA BANK AB",
            "iban": "DE25 3143 5030 6889 0400 01",
            "swift_code": "NDEADEFF"
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

*Documentation generated for `examples/data/hotel_invoices/extracted_invoice_json /moxy_20191221_006_extracted.json`*

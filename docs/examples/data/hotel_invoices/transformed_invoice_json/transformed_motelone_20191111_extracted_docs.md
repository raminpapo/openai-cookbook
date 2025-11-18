# File Documentation: transformed_motelone_20191111_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_motelone_20191111_extracted.json`
- **Size**: 1,948 bytes (1,947 characters)
- **Lines**: 93
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "hotel_information": {
    "name": "Motel One Stuttgart-Bad Cannstatt",
    "address": {
      "street": "Badstraße 20",
      "city": "Stuttgart",
      "country": "Germany",
      "postal_code": "70372"
    },
    "contact": {
      "phone": null,
      "fax": null,
      "email": null,
      "website": null
    }
  },
  "guest_information": {
    "company": "Apimeister consulting GmbH",
    "address": "Friedrichstrasse 123, 10117 Berlin, Germany",
    "guest_name": null
  },
  "invoice_information": {
    "invoice_number": "548113542",
    "reservation_number": "548098589/1",
    "date": "2019-11-11",
    "room_number": "330",
    "check_in_date": "2019-11-11",
    "check_out_date": "2019-11-12"
  },
  "charges": [
    {
      "date": "2019-11-11",
      "description": "Deposit 548113520/02 from 11.11.19",
      "charge": 0,
      "credit": 90.5
    },
    {
      "date": "2019-11-11",
      "description": "Breakfast",
      "charge": 11.5,
      "credit": 0
    },
    {
      "date": "2019-11-11",
      "description": "Lodging",
      "charge": 79.0,
      "credit": 0
    },
    {
      "date": "2019-11-11",
      "description": "Best Price including Breakfast",
      "charge": 90.5,
      "credit": 0
    },
    {
      "date": "2019-11-11",
      "description": "Breakfast",
      "charge": 11.5,
      "credit": 0
    },
    {
      "date": "2019-11-11",
      "description": "Lodging",
      "charge": 79.0,
      "credit": 0
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": 0,
    "total_tax": 0,
    "total_gross": 0,
    "total_charge": 271.5,
    "total_credit": 90.5,
    "balance_due": 0
  },
  "taxes": [
    {
      "tax_type": "19.00%",
      "tax_rate": "19.00%",
      "net_amount": 0,
      "tax_amount": 0,
      "gross_amount": 0
    },
    {
      "tax_type": "7.00%",
      "tax_rate": "7.00%",
      "net_amount": 0,
      "tax_amount": 0,
      "gross_amount": 0
    }
  ]
}
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_motelone_20191111_extracted.json`*

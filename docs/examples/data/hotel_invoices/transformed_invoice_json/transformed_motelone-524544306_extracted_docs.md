# File Documentation: transformed_motelone-524544306_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_motelone-524544306_extracted.json`
- **Size**: 1,628 bytes (1,628 characters)
- **Lines**: 75
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "hotel_information": {
    "name": "Motel One Berlin-Tiergarten",
    "address": {
      "street": "An der Urania 12/14",
      "city": "Berlin",
      "country": "Germany",
      "postal_code": "10787"
    },
    "contact": {
      "phone": null,
      "fax": null,
      "email": null,
      "website": null
    }
  },
  "guest_information": {
    "company": "Apimeister Consulting GmbH",
    "address": "Friedrichstrasse 123, 10117 Berlin, Germany",
    "guest_name": null
  },
  "invoice_information": {
    "invoice_number": "524544306",
    "reservation_number": "524414809/1",
    "date": "2019-02-25",
    "room_number": "519",
    "check_in_date": "2019-02-25",
    "check_out_date": "2019-02-27"
  },
  "charges": [
    {
      "date": "2019-02-25",
      "description": "Best Public Rate with Breakfast",
      "charge": 161.0,
      "credit": 0.0
    },
    {
      "date": "2019-02-25",
      "description": "Breakfast",
      "charge": 23.0,
      "credit": 0.0
    },
    {
      "date": "2019-02-25",
      "description": "Accommodation",
      "charge": 138.0,
      "credit": 0.0
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": 161.0,
    "total_tax": 12.7,
    "total_gross": 173.7,
    "total_charge": 322.0,
    "total_credit": 161.0,
    "balance_due": 0.0
  },
  "taxes": [
    {
      "tax_type": "19.00%",
      "tax_rate": "19.00%",
      "net_amount": 19.33,
      "tax_amount": 3.67,
      "gross_amount": 23.0
    },
    {
      "tax_type": "7.00%",
      "tax_rate": "7.00%",
      "net_amount": 128.97,
      "tax_amount": 9.03,
      "gross_amount": 138.0
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_motelone-524544306_extracted.json`*

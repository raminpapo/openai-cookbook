# File Documentation: transformed_hampton_20190411_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_hampton_20190411_extracted.json`
- **Size**: 2,233 bytes (2,233 characters)
- **Lines**: 105
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "hotel_information": {
    "name": "Hampton by Hilton Hamburg City Centre",
    "address": {
      "street": "Nordkanalstrasse 18",
      "city": "Hamburg",
      "country": "Germany",
      "postal_code": "20097"
    },
    "contact": {
      "phone": "+49(0)40-302372-0",
      "fax": "+49(0)40-302372-100",
      "email": null,
      "website": null
    }
  },
  "guest_information": {
    "company": "APIMEISTER CONSULTING GMBH",
    "address": "FRIEDRICHSTR. 123, 10117 BERLIN, GERMANY",
    "guest_name": "JENS WALTER"
  },
  "invoice_information": {
    "invoice_number": "31611",
    "reservation_number": "92353607",
    "date": null,
    "room_number": "216",
    "check_in_date": "2019-11-04",
    "check_out_date": "2019-11-08"
  },
  "charges": [
    {
      "date": "2019-11-04",
      "description": "MC *5620",
      "charge": -476.0,
      "credit": null
    },
    {
      "date": "2019-11-04",
      "description": "GUEST ROOM",
      "charge": null,
      "credit": 94.05
    },
    {
      "date": "2019-11-05",
      "description": "BREAKFAST",
      "charge": null,
      "credit": 4.95
    },
    {
      "date": "2019-11-05",
      "description": "GUEST ROOM",
      "charge": null,
      "credit": 134.05
    },
    {
      "date": "2019-11-05",
      "description": "BREAKFAST",
      "charge": null,
      "credit": 4.95
    },
    {
      "date": "2019-11-06",
      "description": "GUEST ROOM",
      "charge": null,
      "credit": 114.05
    },
    {
      "date": "2019-11-06",
      "description": "BREAKFAST",
      "charge": null,
      "credit": 4.95
    },
    {
      "date": "2019-11-07",
      "description": "GUEST ROOM",
      "charge": null,
      "credit": 114.05
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": null,
    "total_tax": null,
    "total_gross": null,
    "total_charge": null,
    "total_credit": null,
    "balance_due": null
  },
  "taxes": [
    {
      "tax_type": "VAT 19%",
      "tax_rate": "19%",
      "net_amount": 16.64,
      "tax_amount": 3.16,
      "gross_amount": 19.8
    },
    {
      "tax_type": "VAT 7%",
      "tax_rate": "7%",
      "net_amount": 426.36,
      "tax_amount": 29.84,
      "gross_amount": 456.2
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_hampton_20190411_extracted.json`*

# File Documentation: transformed_madison-496987_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_madison-496987_extracted.json`
- **Size**: 2,210 bytes (2,210 characters)
- **Lines**: 99
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "hotel_information": {
    "name": "MADISON Hotel GmbH",
    "address": {
      "street": "Schaarsteinweg 4",
      "city": "Hamburg",
      "country": "Germany",
      "postal_code": "20459"
    },
    "contact": {
      "phone": "+49.40.37 666-0",
      "fax": "+49.40.37 666-137",
      "email": "info@madisonhotel.de",
      "website": "madisonhotel.de"
    }
  },
  "guest_information": {
    "company": "APimeister Consulting GmbH",
    "address": "Friedrichstr. 123, 10117 Berlin",
    "guest_name": "Mr. Jens Walter"
  },
  "invoice_information": {
    "invoice_number": "496987 /",
    "reservation_number": null,
    "date": "2019-04-18",
    "room_number": "439",
    "check_in_date": "2019-04-15",
    "check_out_date": "2019-04-18"
  },
  "charges": [
    {
      "date": "2019-04-15",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-16",
      "description": "Breakfast **",
      "charge": 20.0,
      "credit": null
    },
    {
      "date": "2019-04-16",
      "description": "CHECK#1000540",
      "charge": null,
      "credit": 20.0
    },
    {
      "date": "2019-04-16",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-17",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-18",
      "description": "Breakfast **",
      "charge": 20.0,
      "credit": null
    },
    {
      "date": "2019-04-18",
      "description": "Mastercard IFC",
      "charge": null,
      "credit": 370.0
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": 342.02,
    "total_tax": 27.98,
    "total_gross": 370.0,
    "total_charge": 370.0,
    "total_credit": 370.0,
    "balance_due": 0.0
  },
  "taxes": [
    {
      "tax_type": "VAT 7%",
      "tax_rate": "7%",
      "net_amount": 308.41,
      "tax_amount": 21.59,
      "gross_amount": 330.0
    },
    {
      "tax_type": "VAT 19%",
      "tax_rate": "19%",
      "net_amount": 33.61,
      "tax_amount": 6.39,
      "gross_amount": 40.0
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_madison-496987_extracted.json`*

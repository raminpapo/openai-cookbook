# File Documentation: transformed_madison-489347_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_madison-489347_extracted.json`
- **Size**: 1,987 bytes (1,987 characters)
- **Lines**: 86
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "hotel_information": {
    "name": "THE MADISON. HAMBURG",
    "address": {
      "street": "Schaarsteinweg 4",
      "city": "Hamburg",
      "country": "Germany",
      "postal_code": "20459"
    },
    "contact": {
      "phone": "+49-40-37 666-0",
      "fax": "+49-40-37 666-137",
      "email": "info@madisonhotel.de",
      "website": "madisonhotel.de"
    }
  },
  "guest_information": {
    "company": "APImeiser Consulting GmbH",
    "address": "Friedrichstr. 123, 10117 Berlin",
    "guest_name": "Mr. Jens Walter"
  },
  "invoice_information": {
    "invoice_number": "489347 /",
    "reservation_number": null,
    "date": "2019-02-08",
    "room_number": "334",
    "check_in_date": "2019-02-03",
    "check_out_date": "2019-02-08"
  },
  "charges": [
    {
      "date": "2019-02-03",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-02-04",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-02-05",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-02-06",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-02-07",
      "description": "Overnight stay excluding breakfast*",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-02-08",
      "description": "Mastercard IFC",
      "charge": null,
      "credit": 550.0
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": 514.02,
    "total_tax": 35.98,
    "total_gross": 550.0,
    "total_charge": 550.0,
    "total_credit": 550.0,
    "balance_due": 0.0
  },
  "taxes": [
    {
      "tax_type": "VAT",
      "tax_rate": "7%",
      "net_amount": 514.02,
      "tax_amount": 35.98,
      "gross_amount": 550.0
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_madison-489347_extracted.json`*

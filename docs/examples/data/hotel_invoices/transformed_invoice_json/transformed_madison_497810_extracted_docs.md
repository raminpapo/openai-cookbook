# File Documentation: transformed_madison_497810_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_madison_497810_extracted.json`
- **Size**: 1,841 bytes (1,841 characters)
- **Lines**: 80
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
    "company": "APImeiseter Consulting GmbH",
    "address": "Friedrichstr. 123, 10117 Berlin",
    "guest_name": "Mr. Jens Walter"
  },
  "invoice_information": {
    "invoice_number": "497810 /",
    "reservation_number": null,
    "date": "2019-04-26",
    "room_number": "403",
    "check_in_date": "2019-04-22",
    "check_out_date": "2019-04-26"
  },
  "charges": [
    {
      "date": "2019-04-22",
      "description": "Overnight stay excluding breakfast",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-23",
      "description": "Overnight stay excluding breakfast",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-24",
      "description": "Overnight stay excluding breakfast",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-25",
      "description": "Overnight stay excluding breakfast",
      "charge": 110.0,
      "credit": null
    },
    {
      "date": "2019-04-26",
      "description": "Mastercard IFC",
      "charge": null,
      "credit": 440.0
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": 411.21,
    "total_tax": 28.79,
    "total_gross": 440.0,
    "total_charge": 440.0,
    "total_credit": 440.0,
    "balance_due": 0.0
  },
  "taxes": [
    {
      "tax_type": "VAT 7%",
      "tax_rate": "7%",
      "net_amount": 411.21,
      "tax_amount": 28.79,
      "gross_amount": 440.0
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_madison_497810_extracted.json`*

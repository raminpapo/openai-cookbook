# File Documentation: transformed_moxy-20191221_007_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/transformed_invoice_json/transformed_moxy-20191221_007_extracted.json`
- **Size**: 1,568 bytes (1,568 characters)
- **Lines**: 68
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "hotel_information": {
    "name": "MOXY Frankfurt Airport",
    "address": {
      "street": "Amelia-Mary-Earhart-Strasse 5",
      "city": "Frankfurt/Main",
      "country": "Germany",
      "postal_code": "60549"
    },
    "contact": {
      "phone": "+49 69 96759139",
      "fax": "+49 69 96759139",
      "email": "crew.frankfurt@moxyhotels.com",
      "website": "www.moxyfrankfurtairport.com"
    }
  },
  "guest_information": {
    "company": "Pfmeister Consulting GmbH",
    "address": "Friedrichstr. 123, 10117 Berlin, Germany",
    "guest_name": "Maik Walter"
  },
  "invoice_information": {
    "invoice_number": "227639",
    "reservation_number": "85111762",
    "date": "2019-12-01",
    "room_number": "306",
    "check_in_date": "2019-11-30",
    "check_out_date": "2019-12-01"
  },
  "charges": [
    {
      "date": "2019-11-21",
      "description": "Deposit Tax Transfer",
      "charge": null,
      "credit": 3.14
    },
    {
      "date": "2019-11-30",
      "description": "Accommodation",
      "charge": 48.0,
      "credit": null
    },
    {
      "date": "2019-11-30",
      "description": "Deposit Transfer at C/I",
      "charge": null,
      "credit": 44.86
    }
  ],
  "totals_summary": {
    "currency": "EUR",
    "total_net": 44.86,
    "total_tax": 3.14,
    "total_gross": 48.0,
    "total_charge": 48.0,
    "total_credit": 48.0,
    "balance_due": 0.0
  },
  "taxes": [
    {
      "tax_type": "VAT 7%",
      "tax_rate": "7%",
      "net_amount": 44.86,
      "tax_amount": 3.14,
      "gross_amount": 48.0
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

*Documentation generated for `examples/data/hotel_invoices/transformed_invoice_json/transformed_moxy-20191221_007_extracted.json`*

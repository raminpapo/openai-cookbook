# Documentation: moxy-20191221_007_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /moxy-20191221_007_extracted.json`
- **Type**: .json file
- **Size**: 3,460 bytes (3.38 KB)
- **Lines**: 103
- **Words**: 213
- **Characters**: 3,459

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "MOXY Frankfurt Airport",
            "address": "Amelia-Mary-Earhart-Strasse 5, 60549 Frankfurt/Main",
            "contact": {
                "phone": "+49 69 96759139",
                "fax": "+49 69 96759139",
                "email": "crew.frankfurt@moxyhotels.com",
                "website": "www.moxyfrankfurtairport.com"
            }
        },
        "guest_information": {
            "name": "Maik Walter",
            "company": "Pfmeister Consulting GmbH",
            "address": "Friedrichstr. 123, 10117 Berlin, Germany",
            "room_number": "306",
            "arrival_date": "30.11.19",
            "departure_date": "01.12.19",
            "folio_number": "227639",
            "confirmation_number": "85111762",
            "cashier_number": "8370",
            "invoice_date": "01.12.19"
        },
        "invoice_information": {
            "description": [
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
            "deposit_folio": [
                {
                    "date": "21.11.19",
                    "folio_number": "223554",
                    "deposit_amount": "48.00",
                    "vat": "3.14"
                }
            ],
            "total": {
                "debit_eur": "48.00",
                "credit_eur": "48.00",
                "balance_to_pay": "0.00"
            }
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
                "vat_eur": "-3.14",
                "gross_eur": "48.00"
            }
        },
        "credit_card_details": {
            "merchant_number": null,
            "card_number": "XXXXXXXXXXXX5052",
            "expiry_date": "XX/XX",
            "card_entry": null,
            "verification": null,
            "terminal_id": null,
            "receipt_number": null,
            "transaction_amount": "48.00",
            "approval_amount": "48.00",
            "approval_code": "A311243"
        },
        "entity_information": {
            "name": "QMHotel Germany GmbH",
            "chamber_of_commerce_number": "HRB 207980",
            "location": "MÜNCHEN",
            "fiscal_number": "143/179/72007",
            "vat_id_number": "UID DE294499203",
            "authorized_representative": "Rune Firing",
            "bank": {
                "name": "NORDEA BANK A/S",
                "iban": "DE23 6143 0030 6869 0400 01",
                "swift_code": "NDEADEFF"
            }
        }
    }
]
```



## High-Level Overview

JSON data file containing structured configuration or data.

## Detailed Analysis

JSON structure (parsing details unavailable)

## Usage & Examples

See file content for usage details.

## Performance & Security Notes

No specific performance or security concerns identified.

## Related Files

**Same directory**:
- [20190119_002_extracted.json](./20190119_002_extracted.json_docs.md)
- [20190202_THE MADISON HAMBURG_001_extracted.json](./20190202_THE MADISON HAMBURG_001_extracted.json_docs.md)
- [20190202_THE MADISON HAMBURG_extracted.json](./20190202_THE MADISON HAMBURG_extracted.json_docs.md)
- [citadines-20190331_Invoice_extracted.json](./citadines-20190331_Invoice_extracted.json_docs.md)
- [citadines_08372561_extracted.json](./citadines_08372561_extracted.json_docs.md)
- [hampton-25789_extracted.json](./hampton-25789_extracted.json_docs.md)
- [hampton_20190411_extracted.json](./hampton_20190411_extracted.json_docs.md)
- [hampton_24361_extracted.json](./hampton_24361_extracted.json_docs.md)
- [hampton_28646_extracted.json](./hampton_28646_extracted.json_docs.md)
- [madison-489347_extracted.json](./madison-489347_extracted.json_docs.md)

## Testing & Execution

See project documentation for testing procedures.

---
*Generated by Repo Book Generator v1.0.0*

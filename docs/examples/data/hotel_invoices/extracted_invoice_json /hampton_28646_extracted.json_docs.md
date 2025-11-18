# Documentation: hampton_28646_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json /hampton_28646_extracted.json`
- **Type**: .json file
- **Size**: 6,055 bytes (5.91 KB)
- **Lines**: 179
- **Words**: 372
- **Characters**: 5,999

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "Hampton by Hilton Hamburg City Centre",
            "address": "Nordkanalstrasse 18, 20097 Hamburg",
            "contact": {
                "phone": "+49(0)40-302372-0",
                "fax": "+49(0)40-302372-100"
            }
        },
        "guest_information": {
            "company": "APIMEISTER CONSULTING GMBH",
            "address": "FRIEDRICHSTR 123, 10117 BERLIN, GERMANY",
            "guest_name": "JENS WALTER"
        },
        "invoice_information": {
            "vat_invoice": "26846",
            "confirmation_number": "81134041",
            "invoice_date": "23/08/2019 09:20:00",
            "vat_number": "DE259895636",
            "folio_number": "119062 A"
        },
        "stay_information": {
            "room_number": "707 /NUDX",
            "arrival_date": "19/08/2019 17:55:00",
            "departure_date": "23/08/2019",
            "adults_children": "1/0",
            "room_rate": "129.00",
            "rate_plan": "2GQ"
        },
        "charges": [
            {
                "date": "19/08/2019",
                "description": "Advance Deposit MC *5052",
                "cashier_id": "TARO",
                "ref_no": "396235",
                "guest_charges": null,
                "credit": "-€516.00",
                "balance": "-€516.00"
            },
            {
                "date": "19/08/2019",
                "description": "ADVANCED DEPOSIT DEBIT",
                "cashier_id": "TARO",
                "ref_no": "396235",
                "guest_charges": "€516.00",
                "credit": null,
                "balance": "0.00"
            },
            {
                "date": "19/08/2019",
                "description": "ADVANCED DEPOSIT CREDIT",
                "cashier_id": "TARO",
                "ref_no": "396237",
                "guest_charges": null,
                "credit": "-€516.00",
                "balance": "-€516.00"
            },
            {
                "date": "19/08/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "396605",
                "guest_charges": "€124.05",
                "credit": null,
                "balance": "-€391.95"
            },
            {
                "date": "19/08/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "396655",
                "guest_charges": "€4.95",
                "credit": null,
                "balance": "-€387.00"
            },
            {
                "date": "20/08/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "396777",
                "guest_charges": "€134.05",
                "credit": null,
                "balance": "-€252.95"
            },
            {
                "date": "20/08/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "396877",
                "guest_charges": "€4.95",
                "credit": null,
                "balance": "-€248.00"
            },
            {
                "date": "21/08/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "397412",
                "guest_charges": "€124.05",
                "credit": null,
                "balance": "-€123.95"
            },
            {
                "date": "21/08/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "397412",
                "guest_charges": "€4.95",
                "credit": null,
                "balance": "-€119.00"
            },
            {
                "date": "22/08/2019",
                "description": "GUEST ROOM",
                "cashier_id": "MACH",
                "ref_no": "397699",
                "guest_charges": "€114.05",
                "credit": null,
                "balance": "-€4.95"
            }
        ]
    },
    {
        "hotel_information": {
            "name": "Hampton by Hilton Hamburg City Centre",
            "address": "Nordkanalstrasse 18, 20097 Hamburg",
            "phone": "+49(0)40-302372-0",
            "fax": "+49(0)40-302372-100"
        },
        "guest_information": {
            "company": "APMEISTER CONSULTING GMBH",
            "address": "DREIDRICHSTR 123, 10117 BERLIN, GERMANY",
            "guest_name": "JENS WALTER"
        },
        "invoice_information": {
            "vat_invoice": "28646",
            "confirmation_number": "81134041",
            "vat": "DE259895636",
            "folio_no": "119562 A"
        },
        "stay_information": {
            "room_no": "707",
            "arrival_date": "19/08/2019 17:55:00",
            "departure_date": "23/08/2019",
            "adult/child": "1/0",
            "room_rate": "120.00",
            "rate_plan": "2C2",
            "al": "H"
        },
        "charges": [
            {
                "date": "22/08/2019",
                "description": "BREAKFAST",
                "cashier_id": "MACH",
                "ref_no": "3797690",
                "guest_charges": "4.95",
                "credit": null,
                "balance": null
            }
        ],
        "balance": "0.00",
        "tax_summary": {
            "trade_receivable_net_19.00%": "€18.64",
            "trade_receivable_net_7.00%": "€0.00",
            "trade_receivable_net_7.00%_2": "€443.73",
            "vat_at_19%": "€3.16",
            "f&b_vat_7%": "€0.00",
            "vat_at_7%": "€32.47",
            "trade_receivables_incl_vat": "€516.00"
        },
        "approval_amount": "€516.00",
        "transaction_id": "390235",
        "appr_code": "277397",
        "balance_2": "-€516.00",
        "guest_signature": "Debit related webpage",
        "thank_you_note": "THANK YOU FOR STAYING WITH US!"
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
- [madison-489347_extracted.json](./madison-489347_extracted.json_docs.md)
- [madison-490057_extracted.json](./madison-490057_extracted.json_docs.md)

## Testing & Execution

See project documentation for testing procedures.

---
*Generated by Repo Book Generator v1.0.0*

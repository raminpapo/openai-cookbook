# Documentation: motelone_20191111_extracted.json

## File Metadata
- **Path**: `examples/data/hotel_invoices/extracted_invoice_json/motelone_20191111_extracted.json`
- **Type**: .json file
- **Size**: 3,434 bytes (3.35 KB)
- **Lines**: 108
- **Words**: 233
- **Characters**: 3,429

## Original Source

```json
[
    {
        "hotel_information": {
            "name": "Motel One Stuttgart-Bad Cannstatt",
            "address": "Badstraße 20, 70372 Stuttgart"
        },
        "guest_information": {
            "name": "Apimeister consulting GmbH",
            "address": "Friedrichstrasse 123, 10117 Berlin, Germany"
        },
        "invoice_information": {
            "date": "11.11.2019",
            "invoice_number": "548113542",
            "reservation_number": "548098589/1",
            "room": "330",
            "arrival": "11.11.2019",
            "departure": "12.11.2019"
        },
        "charges": [
            {
                "guest": "Apimeister consulting GmbH",
                "service": "Deposit 548113520/02 vom 11.11.19",
                "VAT": null,
                "num": "-1",
                "price_EUR": "90,50",
                "amount_EUR": "-90,50"
            },
            {
                "guest": "Apimeister consulting GmbH",
                "service": "Frühstück",
                "VAT": "19,00%",
                "num": "1",
                "price_EUR": "11,50",
                "amount_EUR": "11,50"
            },
            {
                "guest": "Apimeister consulting GmbH",
                "service": "Lodging",
                "VAT": "7,00%",
                "num": "1",
                "price_EUR": "79,00",
                "amount_EUR": "79,00"
            },
            {
                "guest": "Walter, Jens",
                "room": "330",
                "date_range": "from 11.11.2019 to 12.11.2019",
                "service": "Best Price including Breakfast",
                "VAT": null,
                "num": null,
                "price_EUR": null,
                "amount_EUR": null
            },
            {
                "guest": "Walter, Jens",
                "room": "330",
                "date_range": "from 11.11.2019 to 12.11.2019",
                "service": "Frühstück",
                "VAT": "19,00%",
                "num": "1",
                "price_EUR": "11,50",
                "amount_EUR": "11,50"
            },
            {
                "guest": "Walter, Jens",
                "room": "330",
                "date_range": "from 11.11.2019 to 12.11.2019",
                "service": "Lodging",
                "VAT": "7,00%",
                "num": "1",
                "price_EUR": "79,00",
                "amount_EUR": "79,00"
            }
        ],
        "total_amount": {
            "currency": "EUR",
            "amount": "0,00"
        },
        "payment_information": {
            "date": null,
            "payment": null,
            "card_number": null,
            "amount_currency": null,
            "payment_EUR": null
        },
        "balance_to_pay": {
            "currency": "EUR",
            "amount": "0,00"
        },
        "VAT_information": {
            "19,00% (Mwst)": {
                "net_amount_EUR": "0,00",
                "VAT_amount_EUR": "0,00",
                "VAT_gross_EUR": "0,00"
            },
            "7,00% (Mwst)": {
                "net_amount_EUR": "0,00",
                "VAT_amount_EUR": "0,00",
                "VAT_gross_EUR": "0,00"
            }
        },
        "issuer_information": {
            "name": "Motel One Stuttgart-Bad Cannstatt",
            "agent": "Sarah Golombiewski",
            "position": "Front Office Agent"
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

**Imported modules**:
- `11.11.2019`

## Testing & Execution

See project documentation for testing procedures.

---
*Generated by Repo Book Generator v1.0.0*

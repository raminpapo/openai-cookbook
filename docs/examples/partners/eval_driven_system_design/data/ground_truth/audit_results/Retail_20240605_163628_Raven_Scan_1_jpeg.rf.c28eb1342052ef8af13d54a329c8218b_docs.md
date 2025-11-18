# File Documentation: Retail_20240605_163628_Raven_Scan_1_jpeg.rf.c28eb1342052ef8af13d54a329c8218b.json

## File Metadata
- **Path**: `examples/partners/eval_driven_system_design/data/ground_truth/audit_results/Retail_20240605_163628_Raven_Scan_1_jpeg.rf.c28eb1342052ef8af13d54a329c8218b.json`
- **Size**: 841 bytes (841 characters)
- **Lines**: 9
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "not_travel_related": true,
  "amount_over_limit": true,
  "math_error": false,
  "handwritten_x": false,
  "reasoning": "1. NOT_TRAVEL_RELATED: The receipt is for home goods and cleaning supplies, which are not travel-related expenses. Therefore, this criterion is TRUE.\n\n2. AMOUNT_OVER_LIMIT: The total of the receipt is $273.52, which is over the $50 limit, making this criterion TRUE.\n\n3. MATH_ERROR: The subtotal adds up correctly when calculated with tax. The subtotal $252.67 plus tax $20.85 equals the total $273.52. Thus, there is no math error, and this is FALSE.\n\n4. HANDWRITTEN_X: There is no 'X' in the handwritten notes provided. Thus, this is FALSE.\n\nSince two of the criteria (AMOUNT_OVER_LIMIT and MATH_ERROR) are TRUE, the final determination is that this receipt needs to be audited.",
  "needs_audit": true
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

*Documentation generated for `examples/partners/eval_driven_system_design/data/ground_truth/audit_results/Retail_20240605_163628_Raven_Scan_1_jpeg.rf.c28eb1342052ef8af13d54a329c8218b.json`*

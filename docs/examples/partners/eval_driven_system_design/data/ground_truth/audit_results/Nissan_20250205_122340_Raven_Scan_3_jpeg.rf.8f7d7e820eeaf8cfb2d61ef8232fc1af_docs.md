# File Documentation: Nissan_20250205_122340_Raven_Scan_3_jpeg.rf.8f7d7e820eeaf8cfb2d61ef8232fc1af.json

## File Metadata
- **Path**: `examples/partners/eval_driven_system_design/data/ground_truth/audit_results/Nissan_20250205_122340_Raven_Scan_3_jpeg.rf.8f7d7e820eeaf8cfb2d61ef8232fc1af.json`
- **Size**: 594 bytes (594 characters)
- **Lines**: 9
- **Extension**: `.json`
- **Classification**: text

---

## Original Source

```json
{
  "not_travel_related": false,
  "amount_over_limit": true,
  "math_error": false,
  "handwritten_x": false,
  "reasoning": "The receipt is for fuel, which is considered travel-related, hence NOT_TRAVEL_RELATED is FALSE. The total amount of the receipt is $72.10, which exceeds the $50 limit making AMOUNT_OVER_LIMIT TRUE. The math adds up correctly as the subtotal matches the total, so MATH_ERROR is FALSE. There are no handwritten 'X's in the notes so HANDWRITTEN_X is FALSE. Since one of the criteria (AMOUNT_OVER_LIMIT) is violated, the receipt needs auditing.",
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

*Documentation generated for `examples/partners/eval_driven_system_design/data/ground_truth/audit_results/Nissan_20250205_122340_Raven_Scan_3_jpeg.rf.8f7d7e820eeaf8cfb2d61ef8232fc1af.json`*

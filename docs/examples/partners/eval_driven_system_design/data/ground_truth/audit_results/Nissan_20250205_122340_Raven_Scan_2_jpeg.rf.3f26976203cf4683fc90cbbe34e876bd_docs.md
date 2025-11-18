# File Documentation: Nissan_20250205_122340_Raven_Scan_2_jpeg.rf.3f26976203cf4683fc90cbbe34e876bd.json

## File Metadata
- **Path**: `examples/partners/eval_driven_system_design/data/ground_truth/audit_results/Nissan_20250205_122340_Raven_Scan_2_jpeg.rf.3f26976203cf4683fc90cbbe34e876bd.json`
- **Size**: 1,070 bytes (1,067 characters)
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
  "handwritten_x": true,
  "reasoning": "The receipt is for fuel, which is classified as a travel-related expense, hence it does not satisfy the NOT_TRAVEL_RELATED criterion. The total amount of $60.91 exceeds the $50 limit, thus satisfying the AMOUNT_OVER_LIMIT criterion. There are no discrepancies in the arithmetic calculations for the total, so MATH_ERROR is false. However, there is a handwritten 'X' noted in the handwritten notes, which satisfies the HANDWRITTEN_X criterion.   1. NOT_TRAVEL_RELATED: This is a fuel purchase (travel-related), so not_travel_related=false. 2. AMOUNT_OVER_LIMIT: Total of $60.91 exceeds $50, so amount_over_limit=true. 3. MATH_ERROR: 4.199×14.5076≈60.9174, which rounds up to $60.92 or truncates to $60.91, the listed total (either would be acceptable), so math_error=false. 4. HANDWRITTEN_X: The note 'X' is written on the the receipt, so handwritten_x=true. At least one criterion is violated, so needs_audit=true.",
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

*Documentation generated for `examples/partners/eval_driven_system_design/data/ground_truth/audit_results/Nissan_20250205_122340_Raven_Scan_2_jpeg.rf.3f26976203cf4683fc90cbbe34e876bd.json`*

# File Documentation: reportWebVitals.ts

## File Metadata
- **Path**: `examples/voice_solutions/one_way_translation_using_realtime_api/src/reportWebVitals.ts`
- **Size**: 425 bytes (425 characters)
- **Lines**: 16
- **Extension**: `.ts`
- **Classification**: text

---

## Original Source

```typescript
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;

```

---

## High-Level Overview

This is a TypeScript source file.

---

## Detailed Walkthrough

### Functions

- `reportWebVitals()`

### Dependencies/Imports

- `web-vitals`

---

## Performance & Security Notes


---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

```bash
# Run with Node.js
node examples/voice_solutions/one_way_translation_using_realtime_api/src/reportWebVitals.ts
```

---

*Documentation generated for `examples/voice_solutions/one_way_translation_using_realtime_api/src/reportWebVitals.ts`*

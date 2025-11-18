# File Documentation: index.js

## File Metadata
- **Path**: `examples/voice_solutions/one_way_translation_using_realtime_api/relay-server/index.js`
- **Size**: 453 bytes (453 characters)
- **Lines**: 19
- **Extension**: `.js`
- **Classification**: text

---

## Original Source

```javascript
import { RealtimeRelay } from './lib/relay.js';
import dotenv from 'dotenv';
dotenv.config({ override: true });

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

if (!OPENAI_API_KEY) {
  console.error(
    `Environment variable "OPENAI_API_KEY" is required.\n` +
      `Please set it in your .env file.`
  );
  process.exit(1);
}

const PORT = parseInt(process.env.PORT) || 8081;

const relay = new RealtimeRelay(OPENAI_API_KEY);
relay.listen(PORT);

```

---

## High-Level Overview

This is a JavaScript source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `./lib/relay.js`
- `dotenv`

---

## Performance & Security Notes


---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

```bash
# Run with Node.js
node examples/voice_solutions/one_way_translation_using_realtime_api/relay-server/index.js
```

---

*Documentation generated for `examples/voice_solutions/one_way_translation_using_realtime_api/relay-server/index.js`*

# File Documentation: realtime_api_transcription.mmd

## File Metadata
- **Path**: `examples/mermaid/realtime_api_transcription.mmd`
- **Size**: 388 bytes (386 characters)
- **Lines**: 13
- **Extension**: `.mmd`
- **Classification**: text

---

## Original Source

```
```mermaid
sequenceDiagram
    participant Mic
    participant App
    participant WS as "WebSocket"
    participant OAI as "Realtime Server"

    Mic ->> App: 20–40 ms PCM frames
    App ->> WS: Base64-encoded chunks<br/>input_audio_buffer.append
    WS  ->> OAI: Audio stream
    OAI -->> WS: JSON transcription events<br/>(partial & complete)
    WS  -->> App: Transcript updates
```
```

---

## High-Level Overview

This is a text file with extension `.mmd`.

---

## Detailed Walkthrough

---

## Performance & Security Notes


---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

Refer to the project README for instructions on how to use this file.

---

*Documentation generated for `examples/mermaid/realtime_api_transcription.mmd`*

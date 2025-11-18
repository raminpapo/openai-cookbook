# File Documentation: agents_sdk_transcription.mmd

## File Metadata
- **Path**: `examples/mermaid/agents_sdk_transcription.mmd`
- **Size**: 243 bytes (243 characters)
- **Lines**: 8
- **Extension**: `.mmd`
- **Classification**: text

---

## Original Source

```
```{mermaid}
graph LR
    Mic  -- "PCM frames" --> VP["VoicePipeline"]
    VP   -- "VAD & resample" --> Buf["Sentence buffer"]
    Buf  --> GPT["gpt-4o-transcribe"]
    GPT  --> Agent["Agent callbacks"]
    Agent -- "print / reply" --> App
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

*Documentation generated for `examples/mermaid/agents_sdk_transcription.mmd`*

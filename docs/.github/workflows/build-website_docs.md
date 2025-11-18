# File Documentation: build-website.yaml

## File Metadata
- **Path**: `.github/workflows/build-website.yaml`
- **Size**: 223 bytes (223 characters)
- **Lines**: 15
- **Extension**: `.yaml`
- **Classification**: text

---

## Original Source

```yaml
name: Rebuild Cookbook Website

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Call Deploy Hook
        run: curl -X POST ${{ secrets.WEBSITE_DEPLOY_HOOK_URL }}

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

*Documentation generated for `.github/workflows/build-website.yaml`*

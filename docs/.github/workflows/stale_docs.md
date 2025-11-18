# File Documentation: stale.yaml

## File Metadata
- **Path**: `.github/workflows/stale.yaml`
- **Size**: 873 bytes (873 characters)
- **Lines**: 20
- **Extension**: `.yaml`
- **Classification**: text

---

## Original Source

```yaml
name: "Close stale issues and PRs"
on:
  schedule:
    - cron: "30 1 * * *"

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v8
        with:
          stale-issue-message: "This issue is stale because it has been open 60 days with no activity. Remove stale label or comment or this will be closed in 10 days."
          stale-pr-message: "This PR is stale because it has been open 60 days with no activity. Remove stale label or comment or this will be closed in 10 days."
          close-issue-message: "This issue was closed because it has been stalled for 10 days with no activity."
          close-pr-message: "This PR was closed because it has been stalled for 10 days with no activity."
          days-before-issue-stale: 60
          days-before-pr-stale: 60
          days-before-issue-close: 10
          days-before-pr-close: 10

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

*Documentation generated for `.github/workflows/stale.yaml`*

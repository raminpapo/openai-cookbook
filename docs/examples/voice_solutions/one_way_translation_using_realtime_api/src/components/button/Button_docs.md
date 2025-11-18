# File Documentation: Button.scss

## File Metadata
- **Path**: `examples/voice_solutions/one_way_translation_using_realtime_api/src/components/button/Button.scss`
- **Size**: 1,412 bytes (1,412 characters)
- **Lines**: 84
- **Extension**: `.scss`
- **Classification**: text

---

## Original Source

```scss
[data-component='Button'] {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'Roboto Mono', monospace;
  font-size: 12px;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
  border: none;
  background-color: #ececf1;
  color: #101010;
  border-radius: 1000px;
  padding: 8px 24px;
  min-height: 42px;
  transition: transform 0.1s ease-in-out, background-color 0.1s ease-in-out;
  outline: none;

  &.button-style-action {
    background-color: #101010;
    color: #ececf1;
    &:hover:not([disabled]) {
      background-color: #404040;
    }
  }

  &.button-style-alert {
    background-color: #f00;
    color: #ececf1;
    &:hover:not([disabled]) {
      background-color: #f00;
    }
  }

  &.button-style-flush {
    background-color: rgba(255, 255, 255, 0);
  }

  &[disabled] {
    color: #999;
  }

  &:not([disabled]) {
    cursor: pointer;
  }

  &:hover:not([disabled]) {
    background-color: #d8d8d8;
  }

  &:active:not([disabled]) {
    transform: translateY(1px);
  }

  .icon {
    display: flex;
    &.icon-start {
      margin-left: -8px;
    }
    &.icon-end {
      margin-right: -8px;
    }
    svg {
      width: 16px;
      height: 16px;
    }
  }

  &.icon-red .icon {
    color: #cc0000;
  }
  &.icon-green .icon {
    color: #009900;
  }
  &.icon-grey .icon {
    color: #909090;
  }
  &.icon-fill {
    svg {
      fill: currentColor;
    }
  }
}

```

---

## High-Level Overview

This is a text file with extension `.scss`.

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

*Documentation generated for `examples/voice_solutions/one_way_translation_using_realtime_api/src/components/button/Button.scss`*

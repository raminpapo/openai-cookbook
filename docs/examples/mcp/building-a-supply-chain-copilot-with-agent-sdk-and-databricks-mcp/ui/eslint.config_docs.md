# File Documentation: eslint.config.js

## File Metadata
- **Path**: `examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/ui/eslint.config.js`
- **Size**: 844 bytes (844 characters)
- **Lines**: 34
- **Extension**: `.js`
- **Classification**: text

---

## Original Source

```javascript
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'

export default [
  { ignores: ['dist'] },
  {
    files: ['**/*.{js,jsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...js.configs.recommended.rules,
      ...reactHooks.configs.recommended.rules,
      'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  },
]

```

---

## High-Level Overview

This is a JavaScript source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `@eslint/js`
- `eslint-plugin-react-hooks`
- `eslint-plugin-react-refresh`
- `globals`

---

## Performance & Security Notes


---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

```bash
# Run with Node.js
node examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/ui/eslint.config.js
```

---

*Documentation generated for `examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/ui/eslint.config.js`*

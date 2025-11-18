# File Documentation: docker-compose.yml

## File Metadata
- **Path**: `examples/vector_databases/weaviate/docker-compose.yml`
- **Size**: 989 bytes (989 characters)
- **Lines**: 34
- **Extension**: `.yml`
- **Classification**: text

---

## Original Source

```yaml
#################
#
# This is an example Docker file for Weaviate with all OpenAI modules enabled
# You can, but don't have to set `OPENAI_APIKEY` because it can also be set at runtime
#
# Find the latest version here: https://weaviate.io/developers/weaviate/installation/docker-compose
#
#################
---
version: '3.4'
services:
  weaviate:
    command:
    - --host
    - 0.0.0.0
    - --port
    - '8080'
    - --scheme
    - http
    image: semitechnologies/weaviate:1.17.2
    ports:
    - 8080:8080
    restart: on-failure:0
    environment:
      QUERY_DEFAULTS_LIMIT: 25
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'
      PERSISTENCE_DATA_PATH: '/var/lib/weaviate'
      DEFAULT_VECTORIZER_MODULE: 'text2vec-openai'
      ENABLE_MODULES: 'text2vec-openai,qna-openai'
      CLUSTER_HOSTNAME: 'openai-weaviate-cluster'
      # The following parameter (`OPENAI_APIKEY`) is optional, as you can also provide it at insert/query time
      # OPENAI_APIKEY: sk-foobar 
...

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

*Documentation generated for `examples/vector_databases/weaviate/docker-compose.yml`*

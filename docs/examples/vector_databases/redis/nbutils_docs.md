# File Documentation: nbutils.py

## File Metadata
- **Path**: `examples/vector_databases/redis/nbutils.py`
- **Size**: 1,686 bytes (1,686 characters)
- **Lines**: 47
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import os
import wget
import zipfile
import numpy as np
import pandas as pd
from ast import literal_eval


def download_wikipedia_data(
    data_path: str = '../../data/',
    download_path: str = "./",
    file_name: str = "vector_database_wikipedia_articles_embedded") -> pd.DataFrame:

    data_url = 'https://cdn.openai.com/API/examples/data/vector_database_wikipedia_articles_embedded.zip'

    csv_file_path = os.path.join(data_path, file_name + ".csv")
    zip_file_path = os.path.join(download_path, file_name + ".zip")
    if os.path.isfile(csv_file_path):
        print("File Downloaded")
    else:
        if os.path.isfile(zip_file_path):
            print("Zip downloaded but not unzipped, unzipping now...")
        else:
            print("File not found, downloading now...")
            # Download the data
            wget.download(data_url, out=download_path)

        # Unzip the data
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(data_path)

        # Remove the zip file
        os.remove('vector_database_wikipedia_articles_embedded.zip')
        print(f"File downloaded to {data_path}")


def read_wikipedia_data(data_path: str = '../../data/', file_name: str = "vector_database_wikipedia_articles_embedded") -> pd.DataFrame:

    csv_file_path = os.path.join(data_path, file_name + ".csv")
    data = pd.read_csv(csv_file_path)
    # Read vectors from strings back into a list
    data['title_vector'] = data.title_vector.apply(literal_eval)
    data['content_vector'] = data.content_vector.apply(literal_eval)
    # Set vector_id to be a string
    data['vector_id'] = data['vector_id'].apply(str)
    return data

```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `ast`
- `numpy`
- `os`
- `pandas`
- `wget`
- `zipfile`

---

## Performance & Security Notes

- Ensure proper error handling is implemented
- Review for potential security vulnerabilities (SQL injection, XSS, etc.)
- Consider performance implications of loops and recursive functions

---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

```bash
# Run this file
python examples/vector_databases/redis/nbutils.py

# Run tests (if this is a test file)
pytest examples/vector_databases/redis/nbutils.py
```

---

*Documentation generated for `examples/vector_databases/redis/nbutils.py`*

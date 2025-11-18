# Documentation: Visualizing_embeddings_with_Atlas.ipynb

## File Metadata
- **Path**: `examples/third_party/Visualizing_embeddings_with_Atlas.ipynb`
- **Type**: .ipynb file
- **Size**: 5,807 bytes (5.67 KB)
- **Lines**: 208
- **Words**: 500
- **Characters**: 5,807

## Original Source

```json
{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualizing Open AI Embeddings in Atlas\n",
    "\n",
    "In this example, we will upload food review embeddings to [Atlas](https://atlas.nomic.ai) to visualize the embeddings."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is Atlas?\n",
    "\n",
    "[Atlas](https://atlas.nomic.ai) is a machine learning tool used to visualize massive datasets of embeddings in your web browser. Upload millions of embeddings to Atlas and interact with them in your web browser or jupyter notebook."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Login to Atlas.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": []
    }
   ],
   "source": [
    "!pip install nomic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from ast import literal_eval\n",
    "\n",
    "# Load the embeddings\n",
    "datafile_path = \"data/fine_food_reviews_with_embeddings_1k.csv\"\n",
    "df = pd.read_csv(datafile_path)\n",
    "\n",
    "# Convert to a list of lists of floats\n",
    "embeddings = np.array(df.embedding.apply(literal_eval).to_list())\n",
    "df = df.drop('embedding', axis=1)\n",
    "df = df.rename(columns={'Unnamed: 0': 'id'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": []
    }
   ],
   "source": [
    "import nomic\n",
    "from nomic import atlas\n",
    "nomic.login('7xDPkYXSYDc1_ErdTPIcoAR9RNd8YDlkS3nVNXcVoIMZ6') #demo account\n",
    "\n",
    "data = df.to_dict('records')\n",
    "project = atlas.map_embeddings(embeddings=embeddings, data=data,\n",
    "                               id_field='id',\n",
    "                               colorable_fields=['Score'])\n",
    "map = project.maps[0]"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Interact with your embeddings in Jupyter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "            <h3>Project: meek-laborer</h3>\n",
       "            <script>\n",
       "            destroy = function() {\n",
       "                document.getElementById(\"iframe463f4614-7689-47e4-b55b-1da0cc679559\").remove()\n",
       "            }\n",
       "        </script>\n",
       "\n",
       "        <h4>Projection ID: 463f4614-7689-47e4-b55b-1da0cc679559</h4>\n",
       "        <div class=\"actions\">\n",
       "            <div id=\"hide\" class=\"action\" onclick=\"destroy()\">Hide embedded project</div>\n",
       "            <div class=\"action\" id=\"out\">\n",
       "                <a href=\"https://atlas.nomic.ai/map/fddc0e07-97c5-477c-827c-96bca44519aa/463f4614-7689-47e4-b55b-1da0cc679559\" target=\"_blank\">Explore on atlas.nomic.ai</a>\n",
       "            </div>\n",
       "        </div>\n",
       "        \n",
       "        <iframe class=\"iframe\" id=\"iframe463f4614-7689-47e4-b55b-1da0cc679559\" allow=\"clipboard-read; clipboard-write\" src=\"https://atlas.nomic.ai/map/fddc0e07-97c5-477c-827c-96bca44519aa/463f4614-7689-47e4-b55b-1da0cc679559\">\n",
       "        </iframe>\n",
       "\n",
       "        <style>\n",
       "            .iframe {\n",
       "                /* vh can be **very** large in vscode ipynb. */\n",
       "                height: min(75vh, 66vw);\n",
       "                width: 100%;\n",
       "            }\n",
       "        </style>\n",
       "        \n",
       "        <style>\n",
       "            .actions {\n",
       "              display: block;\n",
       "            }\n",
       "            .action {\n",
       "              min-height: 18px;\n",
       "              margin: 5px;\n",
       "              transition: all 500ms ease-in-out;\n",
       "            }\n",
       "            .action:hover {\n",
       "              cursor: pointer;\n",
       "            }\n",
       "            #hide:hover::after {\n",
       "                content: \" X\";\n",
       "            }\n",
       "            #out:hover::after {\n",
       "                content: \"\";\n",
       "            }\n",
       "        </style>\n",
       "        \n",
       "            "
      ],
      "text/plain": [
       "meek-laborer: https://atlas.nomic.ai/map/fddc0e07-97c5-477c-827c-96bca44519aa/463f4614-7689-47e4-b55b-1da0cc679559"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  },
  "vscode": {
   "interpreter": {
    "hash": "365536dcbde60510dc9073d6b991cd35db2d9bac356a11f5b64279a5e6708b97"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

```



## High-Level Overview

Jupyter Notebook containing interactive code cells and documentation.

## Detailed Analysis

File contains 208 lines with structured content.

## Usage & Examples

Open in Jupyter:

```bash
jupyter notebook Visualizing_embeddings_with_Atlas.ipynb
```

## Performance & Security Notes

No specific performance or security concerns identified.

## Related Files

**Same directory**:
- [Code_quality_and_security_scan_with_GitHub_Actions.md](./Code_quality_and_security_scan_with_GitHub_Actions.md_docs.md)
- [GPT_finetuning_with_wandb.ipynb](./GPT_finetuning_with_wandb.ipynb_docs.md)
- [How_to_automate_S3_storage_with_functions.ipynb](./How_to_automate_S3_storage_with_functions.ipynb_docs.md)
- [Openai_monitoring_with_wandb_weave.ipynb](./Openai_monitoring_with_wandb_weave.ipynb_docs.md)
- [Visualizing_embeddings_in_Kangas.ipynb](./Visualizing_embeddings_in_Kangas.ipynb_docs.md)
- [Visualizing_embeddings_in_wandb.ipynb](./Visualizing_embeddings_in_wandb.ipynb_docs.md)
- [Web_search_with_google_api_bring_your_own_browser_tool.ipynb](./Web_search_with_google_api_bring_your_own_browser_tool.ipynb_docs.md)
- [financial_document_analysis_with_llamaindex.ipynb](./financial_document_analysis_with_llamaindex.ipynb_docs.md)

**Imported modules**:
- `ast`
- `atlas`
- `literal_eval`
- `nomic`
- `numpy`
- `pandas`

## Testing & Execution

Execute cells sequentially in Jupyter environment.

---
*Generated by Repo Book Generator v1.0.0*

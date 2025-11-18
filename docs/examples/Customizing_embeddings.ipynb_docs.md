# Documentation: Customizing_embeddings.ipynb

## File Metadata
- **Path**: `examples/Customizing_embeddings.ipynb`
- **Type**: .ipynb file
- **Size**: 448,479 bytes (437.97 KB)
- **Lines**: 13,022
- **Words**: 18,824
- **Characters**: 448,291

## Original Source

```json
{
  "cells": [
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "Vq31CdSRpgkI"
      },
      "source": [
        "# Customizing embeddings\n",
        "\n",
        "This notebook demonstrates one way to customize OpenAI embeddings to a particular task.\n",
        "\n",
        "The input is training data in the form of [text_1, text_2, label] where label is +1 if the pairs are similar and -1 if the pairs are dissimilar.\n",
        "\n",
        "The output is a matrix that you can use to multiply your embeddings. The product of this multiplication is a 'custom embedding' that will better emphasize aspects of the text relevant to your use case. In binary classification use cases, we've seen error rates drop by as much as 50%.\n",
        "\n",
        "In the following example, I use 1,000 sentence pairs picked from the SNLI corpus. Each pair of sentences are logically entailed (i.e., one implies the other). These pairs are our positives (label = 1). We generate synthetic negatives by combining sentences from different pairs, which are presumed to not be logically entailed (label = -1).\n",
        "\n",
        "For a clustering use case, you can generate positives by creating pairs from texts in the same clusters and generate negatives by creating pairs from sentences in different clusters.\n",
        "\n",
        "With other data sets, we have seen decent improvement with as little as ~100 training examples. Of course, performance will be better with  more examples."
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "arB38jFwpgkK"
      },
      "source": [
        "# 0. Imports"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "ifvM7g4apgkK"
      },
      "outputs": [],
      "source": [
        "# imports\n",
        "from typing import List, Tuple  # for type hints\n",
        "\n",
        "import numpy as np  # for manipulating arrays\n",
        "import pandas as pd  # for manipulating data in dataframes\n",
        "import pickle  # for saving the embeddings cache\n",
        "import plotly.express as px  # for plots\n",
        "import random  # for generating run IDs\n",
        "from sklearn.model_selection import train_test_split  # for splitting train & test data\n",
        "import torch  # for matrix optimization\n",
        "\n",
        "from utils.embeddings_utils import get_embedding, cosine_similarity  # for embeddings\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "DtBbryAapgkL"
      },
      "source": [
        "## 1. Inputs\n",
        "\n",
        "Most inputs are here. The key things to change are where to load your datset from, where to save a cache of embeddings to, and which embedding engine you want to use.\n",
        "\n",
        "Depending on how your data is formatted, you'll want to rewrite the process_input_data function."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "UzxcWRCkpgkM"
      },
      "outputs": [],
      "source": [
        "# input parameters\n",
        "embedding_cache_path = \"data/snli_embedding_cache.pkl\"  # embeddings will be saved/loaded here\n",
        "default_embedding_engine = \"text-embedding-3-small\"\n",
        "num_pairs_to_embed = 1000  # 1000 is arbitrary\n",
        "local_dataset_path = \"data/snli_1.0_train_2k.csv\"  # download from: https://nlp.stanford.edu/projects/snli/\n",
        "\n",
        "\n",
        "def process_input_data(df: pd.DataFrame) -> pd.DataFrame:\n",
        "    # you can customize this to preprocess your own dataset\n",
        "    # output should be a dataframe with 3 columns: text_1, text_2, label (1 for similar, -1 for dissimilar)\n",
        "    df[\"label\"] = df[\"gold_label\"]\n",
        "    df = df[df[\"label\"].isin([\"entailment\"])]\n",
        "    df[\"label\"] = df[\"label\"].apply(lambda x: {\"entailment\": 1, \"contradiction\": -1}[x])\n",
        "    df = df.rename(columns={\"sentence1\": \"text_1\", \"sentence2\": \"text_2\"})\n",
        "    df = df[[\"text_1\", \"text_2\", \"label\"]]\n",
        "    df = df.head(num_pairs_to_embed)\n",
        "    return df\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "aBbH71hEpgkM"
      },
      "source": [
        "## 2. Load and process input data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "kAKLjYG6pgkN",
        "outputId": "dc178688-e97d-4ad0-b26c-dff67b858966"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/var/folders/r4/x3kdvs816995fnnph2gdpwp40000gn/T/ipykernel_17509/1977422881.py:13: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  df[\"label\"] = df[\"label\"].apply(lambda x: {\"entailment\": 1, \"contradiction\": -1}[x])\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>text_1</th>\n",
              "      <th>text_2</th>\n",
              "      <th>label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>A person on a horse jumps over a broken down a...</td>\n",
              "      <td>A person is outdoors, on a horse.</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Children smiling and waving at camera</td>\n",
              "      <td>There are children present</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>A boy is jumping on skateboard in the middle o...</td>\n",
              "      <td>The boy does a skateboarding trick.</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>Two blond women are hugging one another.</td>\n",
              "      <td>There are women showing affection.</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>A few people in a restaurant setting, one of t...</td>\n",
              "      <td>The diners are at a restaurant.</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                               text_1  \\\n",
              "2   A person on a horse jumps over a broken down a...   \n",
              "4               Children smiling and waving at camera   \n",
              "7   A boy is jumping on skateboard in the middle o...   \n",
              "14           Two blond women are hugging one another.   \n",
              "17  A few people in a restaurant setting, one of t...   \n",
              "\n",
              "                                 text_2  label  \n",
              "2     A person is outdoors, on a horse.      1  \n",
              "4            There are children present      1  \n",
              "7   The boy does a skateboarding trick.      1  \n",
              "14   There are women showing affection.      1  \n",
              "17      The diners are at a restaurant.      1  "
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# load data\n",
        "df = pd.read_csv(local_dataset_path)\n",
        "\n",
        "# process input data\n",
        "df = process_input_data(df)  # this demonstrates training data containing only positives\n",
        "\n",
        "# view data\n",
        "df.head()\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "z2F1cCoYpgkO"
      },
      "source": [
        "## 3. Split data into training test sets\n",
        "\n",
        "Note that it's important to split data into training and test sets *before* generating synethetic negatives or positives. You don't want any text strings in the training data to show up in the test data. If there's contamination, the test metrics will look better than they'll actually be in production."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "50QmnH2qpgkO",
        "outputId": "6144029b-eb29-439e-9990-7aeb28168e56"
      },
      "outputs": [],
      "source": [
        "# split data into train and test sets\n",
        "test_fraction = 0.5  # 0.5 is fairly arbitrary\n",
        "random_seed = 123  # random seed is arbitrary, but is helpful in reproducibility\n",
        "train_df, test_df = train_test_split(\n",
        "    df, test_size=test_fraction, stratify=df[\"label\"], random_state=random_seed\n",
        ")\n",
        "train_df.loc[:, \"dataset\"] = \"train\"\n",
        "test_df.loc[:, \"dataset\"] = \"test\"\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "MzAFkA2opgkP"
      },
      "source": [
        "## 4. Generate synthetic negatives\n",
        "\n",
        "This is another piece of the code that you will need to modify to match your use case.\n",
        "\n",
        "If you have data with positives and negatives, you can skip this section.\n",
        "\n",
        "If you have data with only positives, you can mostly keep it as is, where it generates negatives only.\n",
        "\n",
        "If you have multiclass data, you will want to generate both positives and negatives. The positives can be pairs of text that share labels, and the negatives can be pairs of text that do not share labels.\n",
        "\n",
        "The final output should be a dataframe with text pairs, where each pair is labeled -1 or 1."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "rUYd9V0zpgkP"
      },
      "outputs": [],
      "source": [
        "# generate negatives\n",
        "def dataframe_of_negatives(dataframe_of_positives: pd.DataFrame) -> pd.DataFrame:\n",
        "    \"\"\"Return dataframe of negative pairs made by combining elements of positive pairs.\"\"\"\n",
        "    texts = set(dataframe_of_positives[\"text_1\"].values) | set(\n",
        "        dataframe_of_positives[\"text_2\"].values\n",
        "    )\n",
        "    all_pairs = {(t1, t2) for t1 in texts for t2 in texts if t1 < t2}\n",
        "    positive_pairs = set(\n",
        "        tuple(text_pair)\n",
        "        for text_pair in dataframe_of_positives[[\"text_1\", \"text_2\"]].values\n",
        "    )\n",
        "    negative_pairs = all_pairs - positive_pairs\n",
        "    df_of_negatives = pd.DataFrame(list(negative_pairs), columns=[\"text_1\", \"text_2\"])\n",
        "    df_of_negatives[\"label\"] = -1\n",
        "    return df_of_negatives\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "Rkh8-J89pgkP"
      },
      "outputs": [],
      "source": [
        "negatives_per_positive = (\n",
        "    1  # it will work at higher values too, but more data will be slower\n",
        ")\n",
        "# generate negatives for training dataset\n",
        "train_df_negatives = dataframe_of_negatives(train_df)\n",
        "train_df_negatives[\"dataset\"] = \"train\"\n",
        "# generate negatives for test dataset\n",
        "test_df_negatives = dataframe_of_negatives(test_df)\n",
        "test_df_negatives[\"dataset\"] = \"test\"\n",
        "# sample negatives and combine with positives\n",
        "train_df = pd.concat(\n",
        "    [\n",
        "        train_df,\n",
        "        train_df_negatives.sample(\n",
        "            n=len(train_df) * negatives_per_positive, random_state=random_seed\n",
        "        ),\n",
        "    ]\n",
        ")\n",
        "test_df = pd.concat(\n",
        "    [\n",
        "        test_df,\n",
        "        test_df_negatives.sample(\n",
        "            n=len(test_df) * negatives_per_positive, random_state=random_seed\n",
        "        ),\n",
        "    ]\n",
        ")\n",
        "\n",
        "df = pd.concat([train_df, test_df])\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "8MVSLMSrpgkQ"
      },
      "source": [
        "## 5. Calculate embeddings and cosine similarities\n",
        "\n",
        "Here, I create a cache to save the embeddings. This is handy so that you don't have to pay again if you want to run the code again."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "R6tWgS_ApgkQ"
      },
      "outputs": [],
      "source": [
        "# establish a cache of embeddings to avoid recomputing\n",
        "# cache is a dict of tuples (text, engine) -> embedding\n",
        "try:\n",
        "    with open(embedding_cache_path, \"rb\") as f:\n",
        "        embedding_cache = pickle.load(f)\n",
        "except FileNotFoundError:\n",
        "    precomputed_embedding_cache_path = \"https://cdn.openai.com/API/examples/data/snli_embedding_cache.pkl\"\n",
        "    embedding_cache = pd.read_pickle(precomputed_embedding_cache_path)\n",
        "\n",
        "\n",
        "# this function will get embeddings from the cache and save them there afterward\n",
        "def get_embedding_with_cache(\n",
        "    text: str,\n",
        "    engine: str = default_embedding_engine,\n",
        "    embedding_cache: dict = embedding_cache,\n",
        "    embedding_cache_path: str = embedding_cache_path,\n",
        ") -> list:\n",
        "    if (text, engine) not in embedding_cache.keys():\n",
        "        # if not in cache, call API to get embedding\n",
        "        embedding_cache[(text, engine)] = get_embedding(text, engine)\n",
        "        # save embeddings cache to disk after each update\n",
        "        with open(embedding_cache_path, \"wb\") as embedding_cache_file:\n",
        "            pickle.dump(embedding_cache, embedding_cache_file)\n",
        "    return embedding_cache[(text, engine)]\n",
        "\n",
        "\n",
        "# create column of embeddings\n",
        "for column in [\"text_1\", \"text_2\"]:\n",
        "    df[f\"{column}_embedding\"] = df[column].apply(get_embedding_with_cache)\n",
        "\n",
        "# create column of cosine similarity between embeddings\n",
        "df[\"cosine_similarity\"] = df.apply(\n",
        "    lambda row: cosine_similarity(row[\"text_1_embedding\"], row[\"text_2_embedding\"]),\n",
        "    axis=1,\n",
        ")\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "4pwn608LpgkQ"
      },
      "source": [
        "## 6. Plot distribution of cosine similarity\n",
        "\n",
        "Here we measure similarity of text using cosine similarity. In our experience, most distance functions (L1, L2, cosine similarity) all work about the same. Note that our embeddings are already normalized to length 1, so cosine similarity is equivalent to dot product.\n",
        "\n",
        "The graphs show how much the overlap there is between the distribution of cosine similarities for similar and dissimilar pairs. If there is a high amount of overlap, that means there are some dissimilar pairs with greater cosine similarity than some similar pairs.\n",
        "\n",
        "The accuracy I compute is the accuracy of a simple rule that predicts 'similar (1)' if the cosine similarity is above some threshold X and otherwise predicts 'dissimilar (0)'."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "SoeDF8vqpgkQ",
        "outputId": "17db817e-1702-4089-c4e8-8ca32d294930"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.plotly.v1+json": {
              "config": {
                "plotlyServerURL": "https://plot.ly"
              },
              "data": [
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=1<br>dataset=train<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "1",
                  "marker": {
                    "color": "#636efa",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "1",
                  "offsetgroup": "1",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "histogram",
                  "x": [
                    0.9267355919345323,
                    0.8959824209230313,
                    0.9119725922265434,
                    0.854066984766886,
                    0.892887342475088,
                    0.9197115510183956,
                    0.8645429616364463,
                    0.8314164166177409,
                    0.7243313891695883,
                    0.8819971504547897,
                    0.7956215051893748,
                    0.7959481856578454,
                    0.8682525487547492,
                    0.8973704561532523,
                    0.8648042605746787,
                    0.9236698981903941,
                    0.9834804742323746,
                    0.8152447410515193,
                    0.8251720025778885,
                    0.8138195587168373,
                    0.8041885875094662,
                    0.9329690881953521,
                    0.9560346908585096,
                    0.9727875559800526,
                    0.8739787488907723,
                    0.8208200937845748,
                    0.7246913159387628,
                    0.9324916305400826,
                    0.8285737172791849,
                    0.8797008558439083,
                    0.820333215489803,
                    0.9370111008629193,
                    0.8983827475968527,
                    0.8312111255338568,
                    0.8164052516323846,
                    0.8908148647559723,
                    0.7466264012908705,
                    0.749651964301876,
                    0.87375582683117,
                    0.7849398161817545,
                    0.8309506403579568,
                    0.9307212180139316,
                    0.8281747408531835,
                    0.9529528469109777,
                    0.7828662080109449,
                    0.887100957550481,
                    0.9000278356226864,
                    0.8805448739521785,
                    0.930239131235984,
                    0.8801954897699975,
                    0.8529206900756547,
                    0.9467797362617967,
                    0.950367690540818,
                    0.7030531843080301,
                    0.8643992401506337,
                    0.8536886651933216,
                    0.9619331104636477,
                    0.9798279220663803,
                    0.8545739729953584,
                    0.8957115039259408,
                    0.8241137169318955,
                    0.8234984837204449,
                    0.8936706246811023,
                    0.8987178417246647,
                    0.9081806514389928,
                    0.9208852073112466,
                    0.8961858080980447,
                    0.8831329491347061,
                    0.9282623092166472,
                    0.8990849228018752,
                    0.8284548395672304,
                    0.8202091311790463,
                    0.8647762700375631,
                    0.840136958242196,
                    0.9887387562448309,
                    0.833342655983456,
                    0.828533112298018,
                    0.9117757392019592,
                    0.8706628948983062,
                    0.9279786042901599,
                    0.7389559895894061,
                    0.8433932035736679,
                    0.9240307526722153,
                    0.950769936374633,
                    0.8586024431762636,
                    0.8685107120156628,
                    0.875535036209879,
                    0.9894909159640456,
                    0.8279650063634755,
                    0.9108703739124493,
                    0.9090161898700972,
                    0.8603952576151226,
                    0.7791958170479588,
                    0.8800175078297319,
                    0.8442387843179446,
                    0.7672266106337577,
                    0.9379753906877134,
                    0.8637536227406404,
                    0.9190295684769377,
                    0.813748744480001,
                    0.9134886375270357,
                    0.8043760086358624,
                    0.8792300492020616,
                    0.8716796296133559,
                    0.8669146731224541,
                    0.7736224659067634,
                    0.9437235456545872,
                    0.905686329875817,
                    0.9534823418409002,
                    0.9150626356433706,
                    0.9409873570135594,
                    0.8111212499450311,
                    0.9171209901271343,
                    0.9126582215550586,
                    0.8337042981493767,
                    0.7317859043960847,
                    0.8444929460069593,
                    0.8561920422842992,
                    0.7765276739806221,
                    0.8526116779814181,
                    0.9178549171995068,
                    0.9238337665547537,
                    0.7218806795387105,
                    0.8180162420894919,
                    0.9687438998025378,
                    0.8354559162714565,
                    0.9146160667909478,
                    0.8082103463995212,
                    0.9563444955040953,
                    0.9066029892990775,
                    0.8485102485675593,
                    0.8154210965438722,
                    0.8860338155558548,
                    0.9280705420457523,
                    0.9835182434488767,
                    0.9653797793986199,
                    0.7815047672209323,
                    0.7156150747063292,
                    0.9256075945804699,
                    0.8135073898727201,
                    0.965501517353668,
                    0.8222681603043882,
                    0.907212186549752,
                    0.8611990749004483,
                    0.9075083701591861,
                    0.9452697087352507,
                    0.8792221638449876,
                    0.9261547230875113,
                    0.8628843081873457,
                    0.7825774684929468,
                    0.826587869384389,
                    0.7399697967202743,
                    0.7855475169419611,
                    0.9111614040328055,
                    0.8871057104665023,
                    0.8824403169032524,
                    0.8618250237448342,
                    0.9787037901590712,
                    0.8066230600465234,
                    0.82769109211187,
                    0.9246432066709112,
                    0.8840853142719706,
                    0.786484352300887,
                    0.9106863314452291,
                    0.9342800776988389,
                    0.8573335079738363,
                    0.7780871062391552,
                    0.7913314665963198,
                    0.8574377397709955,
                    0.9078366114351649,
                    0.7529739278117176,
                    0.8630106564789936,
                    0.9051526759332171,
                    0.7715467442267975,
                    0.894146587858075,
                    0.8095881901541373,
                    0.7733578316514722,
                    0.7600408374028372,
                    0.7819972017869313,
                    0.9003461714649055,
                    0.7428048011790054,
                    0.8645936498599726,
                    0.8158769881622202,
                    0.8338827592994027,
                    0.8272653967731632,
                    0.9017517376316297,
                    0.8480852025321463,
                    0.7970818331146111,
                    0.84837067058732,
                    0.9272909953469497,
                    0.9511439765702141,
                    0.8796630924442385,
                    0.8297595339070903,
                    0.8132311695727563,
                    0.846096509352579,
                    0.8787645385610889,
                    0.8591367322994465,
                    0.8452813265723063,
                    0.708120854745005,
                    0.8769677220320785,
                    0.957621649201,
                    0.7463356296247886,
                    0.8618039385828121,
                    0.9560112462834625,
                    0.8478374736767776,
                    0.769289015775232,
                    0.8456866935685449,
                    0.9014601942765245,
                    0.8816990623836058,
                    0.8836365012367311,
                    0.8078009762348856,
                    0.898471670333294,
                    0.9064470715463968,
                    0.8762712610709371,
                    0.9178852315161201,
                    0.7896235958446132,
                    0.8939345739482307,
                    0.9534018415944343,
                    0.8358882135213556,
                    0.9488657107840998,
                    0.9046799883600772,
                    0.7583576517359092,
                    0.9080459939022663,
                    0.7709722685822517,
                    0.9635512477648485,
                    0.9792712672362888,
                    0.8526700765974843,
                    0.8278133097990042,
                    0.9735858611728696,
                    0.721230194834802,
                    0.8257425311085005,
                    0.9243205490037274,
                    0.9183796453898277,
                    0.9029146937248601,
                    0.9410246048181872,
                    0.9609604036664618,
                    0.7467407974920351,
                    0.8831901217813377,
                    0.8173287200784538,
                    0.8067347032404598,
                    0.7921957436175584,
                    0.9110994793014074,
                    0.8678737504217436,
                    0.9117743220816726,
                    0.781256498099708,
                    0.8553931170417658,
                    0.8798565764815073,
                    0.8485358179238083,
                    0.7748765495278522,
                    0.9432062986428599,
                    0.8328320716129907,
                    0.7983629771463491,
                    0.9345589964322458,
                    0.780034700168418,
                    0.9894680324844076,
                    0.8239308905190431,
                    0.8236003498823307,
                    0.8346101074957768,
                    0.8273793488443836,
                    0.7872103673165679,
                    0.9502897884724039,
                    0.83306630344504,
                    0.9346568240975981,
                    0.8082083566882774,
                    0.8920672687911747,
                    0.8566523137465843,
                    0.7636170858064102,
                    0.8271498146927989,
                    0.8450776675259235,
                    0.9045266249905214,
                    0.8578964053464326,
                    0.8673866119197355,
                    0.8804224181917263,
                    0.8199459545727489,
                    0.932410033971128,
                    0.9096821262750205,
                    0.8658255622247675,
                    0.9386720385226357,
                    0.8517830114204678,
                    0.889433736353776,
                    0.978847593529176,
                    0.8369738178686744,
                    0.8438616304896431,
                    0.9457050132083015,
                    0.8699723446274389,
                    0.7795221418941651,
                    0.9136284834408402,
                    0.839461038218975,
                    0.9453279809479284,
                    0.7899532071809374,
                    0.9078373589637019,
                    0.8434980548175782,
                    0.8112068688921613,
                    0.9466506411385276,
                    0.931413666561485,
                    0.7932453730948084,
                    0.8205411414836395,
                    0.9243834389669592,
                    0.719616209472987,
                    0.7552985082978257,
                    0.9593440978701407,
                    0.917557937781671,
                    0.8643861907339583,
                    0.8315201130646898,
                    0.7608819746989568,
                    0.9704324558544556,
                    0.8037085307118571,
                    0.7785270629127378,
                    0.8044961889638995,
                    0.8313307525316546,
                    0.8064106357955508,
                    0.9291149169587132,
                    0.8412940941318643,
                    0.6917091086045903,
                    0.895204432897799,
                    0.8182250729145697,
                    0.8645847241904496,
                    0.8532020284403578,
                    0.8143634597102418,
                    0.8825747762544934,
                    0.7764652529619696,
                    0.850099367461302,
                    0.8616919096196407,
                    0.9257293995599788,
                    0.935772204341753,
                    0.7742657205171264,
                    0.7898710076766889,
                    0.8590438495382458,
                    0.9317809680608741,
                    0.9087109944408146,
                    0.949297999227784,
                    0.8813316524294974,
                    0.7372081408133433,
                    0.8838176418404169
                  ],
                  "xaxis": "x2",
                  "yaxis": "y2"
                },
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=1<br>dataset=test<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "1",
                  "marker": {
                    "color": "#636efa",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "1",
                  "offsetgroup": "1",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "histogram",
                  "x": [
                    0.9424796847531719,
                    0.9078956620721231,
                    0.8334324872928349,
                    0.9352180099421901,
                    0.9055462980371385,
                    0.8981939710469806,
                    0.8310153256803275,
                    0.8504676050313356,
                    0.8456281884302819,
                    0.8845204616348977,
                    0.9575409743129409,
                    0.8867362111499236,
                    0.8268148049156373,
                    0.9197424487445726,
                    0.7868932880014918,
                    0.7584994087629051,
                    0.9184151106611779,
                    0.8634069821364065,
                    0.8347803687511831,
                    0.8293627315810226,
                    0.9290633380383377,
                    0.8385821691321573,
                    0.9389267221382397,
                    0.890818442649049,
                    0.86634760562554,
                    0.8406483291061461,
                    0.8084243397427517,
                    0.8909500804242533,
                    0.9262896019507018,
                    0.8955541231110083,
                    0.8055268512037249,
                    0.758607678624549,
                    0.9609058491722305,
                    0.91495905751538,
                    0.8670137150812314,
                    0.8813831602682358,
                    0.8602255150075953,
                    0.9239960998195261,
                    0.91732217769794,
                    0.8037285395908439,
                    0.9196344979660896,
                    0.8179495018382927,
                    0.9015423003762686,
                    0.9054394610623084,
                    0.9309412941515826,
                    0.9421722892808463,
                    0.7632823176731237,
                    0.8622055676377434,
                    0.9855273108710355,
                    0.9144155566597573,
                    0.916057392559463,
                    0.8027504546689012,
                    0.7131090055200247,
                    0.86174194818737,
                    0.982873171115144,
                    0.8100227539053508,
                    0.8923878603823862,
                    0.8096643432711604,
                    0.8707613707684018,
                    0.8786740148818871,
                    0.8274639911687568,
                    0.8927098767487393,
                    0.9565597075186062,
                    0.9060728095743347,
                    0.738307517030644,
                    0.9645943657917937,
                    0.8755564011033787,
                    0.879644342330288,
                    0.8679709669180851,
                    0.9304235148160597,
                    0.8902804960376421,
                    0.8748369557157689,
                    0.9999999999999999,
                    0.7979398167195422,
                    0.8182553472910762,
                    0.7782108671759803,
                    0.8427610550014142,
                    0.8696408842646327,
                    0.8747903026537825,
                    0.914973368517656,
                    0.9651568968718233,
                    0.9775547988384379,
                    0.8964005885715726,
                    0.8689760349348122,
                    0.8501707274497268,
                    0.9069421089316828,
                    0.7682621587597694,
                    0.9658683147667629,
                    0.8946443487011166,
                    0.7855154267442119,
                    0.8963791544804274,
                    0.8062904921192978,
                    0.8165205978948239,
                    0.8392522254625653,
                    0.9456080863923884,
                    0.7904904126133966,
                    0.833126792097794,
                    0.7852156051245299,
                    0.7859162398886373,
                    0.9097674992318959,
                    0.8868692153350769,
                    0.9391826646753169,
                    0.9428151202937937,
                    0.7923603877885725,
                    0.9018727189911658,
                    0.9723161942344292,
                    0.7820369113228325,
                    0.9667234201162873,
                    0.978769627389609,
                    0.9155729781931277,
                    0.8273013970664075,
                    0.9603319621485501,
                    0.9298975009081959,
                    0.8775117467919693,
                    0.8614509568162568,
                    0.9144155657624043,
                    0.7783710792186642,
                    0.9701880190033496,
                    0.7858944693777298,
                    0.9278353490304795,
                    0.9472367444800102,
                    0.7834809788888359,
                    0.7997358978342995,
                    0.8459052935830644,
                    0.8612076995259889,
                    0.8470901722260982,
                    0.824037271004761,
                    0.865608650068826,
                    0.8023193246081538,
                    0.7836788857151791,
                    0.880404135119559,
                    0.8491559249509729,
                    0.788345270395367,
                    0.9461393747813323,
                    0.835123385080455,
                    0.8158174048388718,
                    0.8604581300972295,
                    0.9623616555004862,
                    0.8564688397784819,
                    0.8576867681204893,
                    0.8973905356978807,
                    0.8634447095761868,
                    0.8149528594606367,
                    0.873171253801101,
                    0.8653347676818378,
                    0.929525558735665,
                    0.8358267202818717,
                    0.971888682386554,
                    0.8500189240129448,
                    0.6201715858790215,
                    0.8982737437906866,
                    0.8919523978597029,
                    0.7327218620224804,
                    0.8329671225228632,
                    0.9265589851585685,
                    0.8976605724257473,
                    0.8865148832512937,
                    0.7893917264917192,
                    0.7303107673595587,
                    0.8428958487387793,
                    0.8712646524042454,
                    0.9726111208329614,
                    0.9368020234351375,
                    0.9270010843622818,
                    0.8900608737128451,
                    0.7975173141451626,
                    0.9403308743666237,
                    0.8484005148509558,
                    0.9285585494125882,
                    0.8461714640960527,
                    0.9301612552439464,
                    0.9840391344904358,
                    0.8305503032909712,
                    0.8985536902480058,
                    0.9476344055766088,
                    0.9342892661789283,
                    0.8849523247638441,
                    0.7736620851030366,
                    0.8083290901088768,
                    0.9510007696957726,
                    0.8677438102591386,
                    0.8324233959261911,
                    0.7379868650067231,
                    0.9049462205283083,
                    0.9044068964151009,
                    0.7810399099399672,
                    0.9040280419401343,
                    0.7720832557964016,
                    0.7168259249496903,
                    0.8657076231674912,
                    0.9689982290529879,
                    0.9330371348632155,
                    0.7014093149115691,
                    0.9056081832768474,
                    0.8483474394912361,
                    0.8729108893663646,
                    0.8494252835407102,
                    0.8702668029663239,
                    0.8703072652243842,
                    0.9279473628052111,
                    0.8615930026010632,
                    0.7590822846968434,
                    0.8435232136599701,
                    0.8264379743713927,
                    0.8793126202650794,
                    0.847452301256391,
                    0.7546334370590053,
                    0.8870818568791698,
                    0.8349553719854912,
                    0.9232007589383142,
                    0.7924421895458662,
                    0.8556103146657943,
                    0.8397958720336148,
                    0.9358165878534705,
                    0.904577353436614,
                    0.9022537114781464,
                    0.775603917181226,
                    0.946091618927627,
                    0.8264119461162666,
                    0.8261258105029201,
                    0.8605336598142989,
                    0.7518422489499549,
                    0.849587557879856,
                    0.9922578397415717,
                    0.7499254104864422,
                    0.8845204616348977,
                    0.8361936554693772,
                    0.9172228808488442,
                    0.8068135566092208,
                    0.795739929008372,
                    0.8632611464779958,
                    0.7612462576141025,
                    0.9589125421073597,
                    0.9555759038945358,
                    0.8822980105025566,
                    0.9663740139243834,
                    0.9071760951442449,
                    0.9335338894977118,
                    0.8042262160785201,
                    0.9399607295068667,
                    0.8318513711395181,
                    0.8697471272873054,
                    0.9103391819002411,
                    0.8272582065159091,
                    0.7868989539137853,
                    0.7416168920325092,
                    0.8828593510646834,
                    0.9141342991325323,
                    0.7259887492833588,
                    0.9478299721997572,
                    0.843766518385904,
                    0.919830425538435,
                    0.9069062941852448,
                    0.9036466185261808,
                    0.9817542893707696,
                    0.8833292621745382,
                    0.832556614533968,
                    0.8135910443631924,
                    0.9628932969024508,
                    0.9450804655496136,
                    0.9226384091529121,
                    0.8401818103049188,
                    0.723691406760321,
                    0.6828741135249211,
                    0.834410523069395,
                    0.9959256404542386,
                    0.952870396433041,
                    0.969514692554192,
                    0.9220387806044666,
                    0.9511950116111251,
                    0.87442203104197,
                    0.8399026046246612,
                    0.9029483760650204,
                    0.9097073428917352,
                    0.8651925582004045,
                    0.9178332691819033,
                    0.7556713752294848,
                    0.8601740894614596,
                    0.8250804250840363,
                    0.799473306929639,
                    0.8911389639861809,
                    0.915913776235107,
                    0.7867422041389165,
                    0.8035116695233039,
                    0.7702882636946234,
                    0.9060460430333088,
                    0.7214029229730072,
                    0.8607904806397634,
                    0.8228468643082103,
                    0.8900020169140401,
                    0.9343567736626528,
                    0.9305049279291139,
                    0.9664193138643489,
                    0.9008537853184969,
                    0.7625840742620333,
                    0.815302054727336,
                    0.9215061720798934,
                    0.7192673801865671,
                    0.8949994067748966,
                    0.9367566547265034,
                    0.7602684166275758,
                    0.8184439767612992,
                    0.8361983856596491,
                    0.7761725471827079,
                    0.7724780968772909,
                    0.9249211346782868,
                    0.8718843131924867,
                    0.8522890335712519,
                    0.9015475867709434,
                    0.8720699810318118,
                    0.8937599387455695,
                    0.8721713573852221,
                    0.8100783166142076,
                    1.0000000000000002,
                    0.8213222537973748,
                    0.8361185401136565,
                    0.8371907459006128,
                    0.9065697385076582,
                    0.752240671472798,
                    0.8283078905766531,
                    0.8499886819287953,
                    0.9097932369637356,
                    0.9529813104528191,
                    0.8449289750214674,
                    1,
                    0.8302949362084788,
                    0.7741532046500113,
                    0.8743828037305432,
                    0.8201855611163867,
                    0.8194689758101458,
                    0.7925076796225758,
                    0.8748126117575765,
                    0.8299510305557958,
                    0.9619426561868236,
                    0.8627070029199212
                  ],
                  "xaxis": "x",
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=-1<br>dataset=train<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "-1",
                  "marker": {
                    "color": "#EF553B",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "-1",
                  "offsetgroup": "-1",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "histogram",
                  "x": [
                    0.7299945446332757,
                    0.761829365033925,
                    0.676235270353631,
                    0.7023016593603112,
                    0.7350156032869306,
                    0.7735236691667362,
                    0.7187241641280292,
                    0.8063818744486255,
                    0.7115273138749911,
                    0.7402039545462252,
                    0.7372226375565185,
                    0.719606336264161,
                    0.8344052997670786,
                    0.6881482918877712,
                    0.650513335277676,
                    0.7182967436895931,
                    0.7659970793010594,
                    0.6361476177437694,
                    0.7957002158983555,
                    0.7395402073375513,
                    0.7614384854511241,
                    0.6835300790002988,
                    0.6209194558826169,
                    0.7907726220786139,
                    0.7215750502680501,
                    0.7271947538454276,
                    0.6962333614625641,
                    0.7517476038206041,
                    0.7135529871009506,
                    0.7522919529124952,
                    0.7120639628754573,
                    0.7623014780353815,
                    0.7939574492876662,
                    0.6998873138766412,
                    0.7700594720774577,
                    0.7766161530342343,
                    0.7285080945118152,
                    0.7562511166739386,
                    0.8086622737220109,
                    0.7565297004511734,
                    0.7315242427462245,
                    0.791225232078265,
                    0.7281092467134649,
                    0.7675685917886341,
                    0.7122436997016454,
                    0.7600255476588682,
                    0.769465992253443,
                    0.7552507233110458,
                    0.7373719614604455,
                    0.7681449827665134,
                    0.7760194768221379,
                    0.8035677492769473,
                    0.7771752906080505,
                    0.6514739683312004,
                    0.744787832649546,
                    0.7700232252518491,
                    0.6901772464238046,
                    0.721128796446804,
                    0.686814078974691,
                    0.796786900996621,
                    0.8242176320872988,
                    0.7806742901384496,
                    0.7697696656361902,
                    0.7868668497422822,
                    0.7304548331410279,
                    0.7296767182508448,
                    0.699401040331297,
                    0.8332660282838579,
                    0.6513224421864793,
                    0.6927364371405096,
                    0.7491793002300279,
                    0.7909034218879171,
                    0.7754176150761527,
                    0.8004827006684735,
                    0.6659923526948868,
                    0.8129618884980553,
                    0.7496476113488948,
                    0.6519665061955423,
                    0.7319506042291191,
                    0.7367099004846358,
                    0.8590817275589286,
                    0.6684490623528697,
                    0.7469140136676841,
                    0.7269016830127544,
                    0.6834261236240542,
                    0.6390380393123325,
                    0.7129209978685723,
                    0.6879274953497815,
                    0.6720427402498903,
                    0.7343923261152341,
                    0.5977941468082364,
                    0.7574521074337901,
                    0.7302129263006347,
                    0.7380209108764002,
                    0.7280177437983031,
                    0.6870880300968067,
                    0.6928024686173956,
                    0.6403900073451696,
                    0.7209247906698092,
                    0.666799070142464,
                    0.7233569397428488,
                    0.7555267048881131,
                    0.7275931437975757,
                    0.7562785127332186,
                    0.736649021802634,
                    0.762569980781232,
                    0.7741923768467133,
                    0.6669773662198453,
                    0.7499779113599104,
                    0.7783371410262362,
                    0.7798574909618832,
                    0.7068277719647446,
                    0.7718066533969561,
                    0.7078874155127759,
                    0.7238814624322412,
                    0.8729026036201937,
                    0.7106759057210158,
                    0.7585767440008555,
                    0.6923565683937588,
                    0.6693898561996529,
                    0.7219944003835542,
                    0.7188064794656569,
                    0.7491451951131076,
                    0.6750197249394477,
                    0.7009868838756784,
                    0.6519589230722103,
                    0.775109860666869,
                    0.6682014813660948,
                    0.6618358724923147,
                    0.6218362070243146,
                    0.7518134154555007,
                    0.7571307427362168,
                    0.7546823360234822,
                    0.7416435744760188,
                    0.7676464608286054,
                    0.5799855321635428,
                    0.796191792361925,
                    0.6845373357552841,
                    0.7667984177770908,
                    0.7393609881148844,
                    0.7544580057165962,
                    0.7397495323890664,
                    0.7658298386950907,
                    0.6611125314078552,
                    0.7977728876184589,
                    0.831090991824215,
                    0.6982347705041605,
                    0.6312226759947304,
                    0.6482907496231076,
                    0.7658362595299695,
                    0.7518400125995974,
                    0.8025480920087656,
                    0.7461501494015976,
                    0.7239149641844659,
                    0.7090055516721123,
                    0.6846622430587006,
                    0.7112212118684095,
                    0.6794460508450644,
                    0.8344462829585355,
                    0.7638782230495382,
                    0.6558255308015893,
                    0.6799836520005059,
                    0.7148088830660722,
                    0.7658007439571484,
                    0.6581857665503666,
                    0.648734015773256,
                    0.8156725527309459,
                    0.6929202590284855,
                    0.7490919589112273,
                    0.7090723359022927,
                    0.7105572886194162,
                    0.7461374422467866,
                    0.7084742440808511,
                    0.6889378818898818,
                    0.7551565238112727,
                    0.7198789279593328,
                    0.7270482774940944,
                    0.6971190427893721,
                    0.7391610904601401,
                    0.6344734499604212,
                    0.6719507302378157,
                    0.6861159059531602,
                    0.6516118314317232,
                    0.7199095105818035,
                    0.6817881072485698,
                    0.7207373940156253,
                    0.7745467156569463,
                    0.6258059783246434,
                    0.7481056513643776,
                    0.7183327989261993,
                    0.7624705969064652,
                    0.703717229048042,
                    0.7487365873620485,
                    0.7495555007485976,
                    0.6409624588579408,
                    0.7176245775200687,
                    0.7537100520717849,
                    0.7569868075002099,
                    0.7392135510982174,
                    0.7188471960732984,
                    0.697413550280765,
                    0.7138614496887067,
                    0.7057641350396069,
                    0.7675079665142936,
                    0.7310427541091186,
                    0.7808018818735418,
                    0.7567255895826445,
                    0.7035962262766099,
                    0.7040750813384501,
                    0.8183159919038065,
                    0.7953911933398697,
                    0.7464891038038547,
                    0.6751591827598264,
                    0.7849943676377955,
                    0.7155963442284841,
                    0.7428993249606122,
                    0.7131100645054201,
                    0.7227595311429733,
                    0.6519548345531954,
                    0.7201522118536183,
                    0.86540799716664,
                    0.8128819241371503,
                    0.7278912446692862,
                    0.7305867175950502,
                    0.7171875192153516,
                    0.6755179003509543,
                    0.7256221359402913,
                    0.7003814947129137,
                    0.7486334697158199,
                    0.7232489166529666,
                    0.7347697330652992,
                    0.6493837702986368,
                    0.6454310256268904,
                    0.7085305859966166,
                    0.7709963397003181,
                    0.7628122486461532,
                    0.7260869667056613,
                    0.7656074896314918,
                    0.7309944223135776,
                    0.7575162043117213,
                    0.7425954755181217,
                    0.7978452334414571,
                    0.7414129597626153,
                    0.7369987033441427,
                    0.7249664966482501,
                    0.663939118162477,
                    0.7490232329485363,
                    0.7532303509685747,
                    0.6505502824396713,
                    0.6820403873171862,
                    0.7458589415356044,
                    0.65106761846338,
                    0.8190794585362886,
                    0.6404595320063431,
                    0.7620011212588133,
                    0.6793344580417779,
                    0.7470455239529016,
                    0.6254743025101126,
                    0.714021296346165,
                    0.7624376857959331,
                    0.6124088443110871,
                    0.7190909082546953,
                    0.7667977482791689,
                    0.7390282391537781,
                    0.731411776312689,
                    0.6910654011387792,
                    0.7669731150300952,
                    0.7473599833172766,
                    0.7757742306046117,
                    0.7524096654164605,
                    0.668078105815945,
                    0.6797298899209671,
                    0.734572374544983,
                    0.7851097143298676,
                    0.7342031538272321,
                    0.7372538892798539,
                    0.7335209046034747,
                    0.6838366965805461,
                    0.6892908218001774,
                    0.7368799079039347,
                    0.667817778038092,
                    0.7436021083467266,
                    0.643687287978847,
                    0.6459012534104801,
                    0.717961524900317,
                    0.651811280493696,
                    0.774663511332172,
                    0.6481450536649574,
                    0.7135017154296592,
                    0.718243043672562,
                    0.6840974559559992,
                    0.6237039667424505,
                    0.7511301324631847,
                    0.6731554748777204,
                    0.7311433676647258,
                    0.7407740108803432,
                    0.7219713524118947,
                    0.6945284597258313,
                    0.7403964086997485,
                    0.7281416758951161,
                    0.767616849591671,
                    0.7623013461443361,
                    0.794278871148869,
                    0.7094595086377886,
                    0.6363511838820268,
                    0.6955392554405656,
                    0.7448982185809608,
                    0.7328610107493276,
                    0.7208624134565648,
                    0.6762963031433926,
                    0.7755406771546928,
                    0.7045876515082797,
                    0.6244682388287953,
                    0.6742169930443296,
                    0.8182351707309709,
                    0.7329206562104693,
                    0.7750198586773644,
                    0.7686712995024062,
                    0.7382706738683358,
                    0.6670365140953741,
                    0.7122098843228497,
                    0.720363344417827,
                    0.7260325476617868,
                    0.7455849615803621,
                    0.7135971488970759,
                    0.7597698332957011,
                    0.7261113201174606,
                    0.7802411718313292,
                    0.6937507195359754,
                    0.7842882648198792,
                    0.6900501446041246,
                    0.760860218311663,
                    0.7134088358525988,
                    0.7053629634417926
                  ],
                  "xaxis": "x2",
                  "yaxis": "y2"
                },
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=-1<br>dataset=test<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "-1",
                  "marker": {
                    "color": "#EF553B",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "-1",
                  "offsetgroup": "-1",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "histogram",
                  "x": [
                    0.698216609902851,
                    0.7175312484264973,
                    0.7186004945024,
                    0.8000305631283213,
                    0.6982596730429885,
                    0.7632305498724974,
                    0.7138465594512551,
                    0.6788567152998355,
                    0.7373203069430523,
                    0.6873036529619025,
                    0.6503465541274354,
                    0.7365009792588864,
                    0.741093678604772,
                    0.735107851927508,
                    0.7789882788330387,
                    0.6997359150722298,
                    0.7996799028712657,
                    0.7467428244049107,
                    0.6687862526227949,
                    0.743064589979991,
                    0.8567601871608912,
                    0.7518934598338161,
                    0.7026922402796603,
                    0.7211365080382613,
                    0.706354045904417,
                    0.779427003097291,
                    0.7362962393365906,
                    0.7291751132805836,
                    0.7122378769301289,
                    0.7140477948952889,
                    0.7173405960056081,
                    0.7634875929311733,
                    0.7977581390590794,
                    0.7301463738402032,
                    0.7615332057968679,
                    0.682227985030492,
                    0.7334635989895589,
                    0.7386028577038499,
                    0.659084291835728,
                    0.7899820114980755,
                    0.7247172517704278,
                    0.7438155210487466,
                    0.7005346860296618,
                    0.6648553956533266,
                    0.7701566644966253,
                    0.7514961574415904,
                    0.7587991656983686,
                    0.7001882273133521,
                    0.6910707516646375,
                    0.7394355361240693,
                    0.7276824899179835,
                    0.6759744362016779,
                    0.8302185470787163,
                    0.6928641094502374,
                    0.7120538723839331,
                    0.7224960785372221,
                    0.7198045816069757,
                    0.6813558762031737,
                    0.7165801628045559,
                    0.7120832723046919,
                    0.8420619371167495,
                    0.946387336435492,
                    0.7554566849916029,
                    0.6539169025880401,
                    0.7809846972343978,
                    0.7724403150471626,
                    0.7005276086814838,
                    0.6393757830582598,
                    0.8206678516495857,
                    0.7220887623700465,
                    0.6457268309147112,
                    0.7355556783165726,
                    0.7154485704709247,
                    0.736485552747626,
                    0.6279868336962336,
                    0.6826307018159569,
                    0.6893086023402188,
                    0.6662701662224271,
                    0.7867533724923507,
                    0.7767747518359883,
                    0.8265509786609969,
                    0.7191298707058883,
                    0.7022356632617615,
                    0.7327905404619434,
                    0.744068997548466,
                    0.7610196098150734,
                    0.7115456073990181,
                    0.7432332956176703,
                    0.7893785433034154,
                    0.7290401089931655,
                    0.6577253300110991,
                    0.7003577024217508,
                    0.6656632326716906,
                    0.777774068734494,
                    0.7332058736487923,
                    0.6832255453323396,
                    0.7959026283113317,
                    0.7447573588360193,
                    0.6641622569109379,
                    0.6536973982676278,
                    0.6665423422110455,
                    0.6839542281076658,
                    0.7423443203765382,
                    0.7548386221527327,
                    0.6027110439271006,
                    0.6910860362919979,
                    0.6562817652314046,
                    0.716178983425107,
                    0.724403115068019,
                    0.7259909803954812,
                    0.7571530348849562,
                    0.733442357026098,
                    0.7422263713152575,
                    0.7194490356714829,
                    0.8324274302968815,
                    0.7326854438693811,
                    0.6965534375434462,
                    0.6112368704742529,
                    0.7304384905441154,
                    0.7720040972080942,
                    0.6935032899149339,
                    0.6744196671055273,
                    0.7147585872166342,
                    0.7752945283086001,
                    0.7247252468203336,
                    0.7487128692844189,
                    0.7073695766484023,
                    0.7770002807438351,
                    0.6765039364068596,
                    0.6337555851438214,
                    0.7894145395726685,
                    0.808127657824718,
                    0.6806212157836168,
                    0.6631556694778886,
                    0.7026864982467919,
                    0.6616453779258454,
                    0.7884566439105933,
                    0.7066759939380831,
                    0.6337579382878964,
                    0.6487574469000645,
                    0.772145520185077,
                    0.7232462166936153,
                    0.7901145921506159,
                    0.6972515066616096,
                    0.7122390390469722,
                    0.7192738985202007,
                    0.6592857746430886,
                    0.7609468966795828,
                    0.6603956483288737,
                    0.7457664593808938,
                    0.6826889303879785,
                    0.7934081087742163,
                    0.6763383894378445,
                    0.6839731303810913,
                    0.6687692061586001,
                    0.6991702352595418,
                    0.7797875942740597,
                    0.7663428993137384,
                    0.7674609664886143,
                    0.7252797254797089,
                    0.6976652869077468,
                    0.7158816756428659,
                    0.718241456712601,
                    0.7632800029357677,
                    0.7220393239650442,
                    0.7734594213360495,
                    0.6831354341128338,
                    0.8050740585092945,
                    0.8304016729411579,
                    0.6942297180429666,
                    0.7777210539532041,
                    0.7971492766742209,
                    0.7551377672686813,
                    0.756111346085797,
                    0.7377139073001521,
                    0.7292914327831885,
                    0.6619852966467218,
                    0.6633387313486273,
                    0.7753943622795527,
                    0.6931366760284077,
                    0.6879938635549627,
                    0.7934277451864097,
                    0.7095961561996172,
                    0.6721647904665006,
                    0.6639348167332335,
                    0.7190874751718003,
                    0.6487682662731885,
                    0.7712237228183192,
                    0.7195541308325332,
                    0.7624245070018526,
                    0.7066568592895756,
                    0.6955819267956074,
                    0.762644689565747,
                    0.696550099953965,
                    0.72160309057877,
                    0.6589853583691466,
                    0.7781076723886485,
                    0.7844353288099747,
                    0.6499942545071061,
                    0.7586643115109818,
                    0.7851245713510661,
                    0.6825431110733673,
                    0.7920473550917971,
                    0.7505505200683399,
                    0.7112992195413225,
                    0.6872424297540068,
                    0.6629403755138552,
                    0.7754417757832819,
                    0.7445419843378304,
                    0.7064660255551196,
                    0.7102764764345906,
                    0.7166584523700176,
                    0.745706231193076,
                    0.7628022956052315,
                    0.6960882904963708,
                    0.6837468719098787,
                    0.7520487263229376,
                    0.7604129787986132,
                    0.7522054011542562,
                    0.6898973175025894,
                    0.712053903439596,
                    0.7339122116041967,
                    0.6789458999380491,
                    0.763449576758855,
                    0.7406926320689465,
                    0.6976029213628422,
                    0.7734670110437211,
                    0.7670042286239444,
                    0.7194794729796166,
                    0.8039337600845294,
                    0.822887238017454,
                    0.7546355748553022,
                    0.712175872919759,
                    0.6283408438534046,
                    0.7277722488820856,
                    0.7848289730316366,
                    0.6470175548703326,
                    0.7175970646556328,
                    0.6982508276209234,
                    0.6931585425755658,
                    0.7105706262503181,
                    0.6541269887120206,
                    0.8404400660965669,
                    0.7278163563567496,
                    0.8022018950050529,
                    0.7449136144274442,
                    0.7254549036563473,
                    0.7708530061010334,
                    0.7226568414320923,
                    0.7174427406313559,
                    0.7242867487973796,
                    0.7465548093208114,
                    0.6481248100208876,
                    0.715420475795481,
                    0.7818995378198694,
                    0.710140386310007,
                    0.779070581516581,
                    0.7022765286826387,
                    0.7920014977874291,
                    0.7028249663680173,
                    0.7464011128583546,
                    0.6874796697586977,
                    0.7834259382246206,
                    0.7487992683674399,
                    0.6256280566008573,
                    0.7248416704075088,
                    0.6787298488859722,
                    0.7604099689852636,
                    0.7563309422531382,
                    0.6536692254847523,
                    0.7277402265583088,
                    0.7961681595257355,
                    0.7183023940359037,
                    0.8578324194628058,
                    0.6890352710148969,
                    0.711616174722821,
                    0.6560825239577808,
                    0.7235723022023411,
                    0.6649236563739442,
                    0.6800589793852263,
                    0.7785177771732936,
                    0.8277144895457349,
                    0.7047472917613488,
                    0.6981993581133783,
                    0.69214194925211,
                    0.7175225477364914,
                    0.6821700037384272,
                    0.6934882153010823,
                    0.6671459724713757,
                    0.7577056235720239,
                    0.7452347481085622,
                    0.7540647847248615,
                    0.7623045528688165,
                    0.8419961516314336,
                    0.7607631404114222,
                    0.7104592749279437,
                    0.7907219223857475,
                    0.6626370861321504,
                    0.7293323972767943,
                    0.6747790790615374,
                    0.7205393564241827,
                    0.7182141925188444,
                    0.6698620455142402,
                    0.7774615433926413,
                    0.68441903533162,
                    0.7195176784475413,
                    0.7765542578440102,
                    0.7653003235671018,
                    0.6588957811563716,
                    0.7049538466814345,
                    0.6767019827253833,
                    0.6852115350974048,
                    0.7159808946533304,
                    0.6275008181698795,
                    0.6641598464064111,
                    0.7653064009797307,
                    0.7846062245731015,
                    0.7131195190890488,
                    0.7388407888274415,
                    0.7078575690975646,
                    0.7922969773693673,
                    0.6399205949452071,
                    0.7522331808600956,
                    0.756127025845852,
                    0.7527950868321375,
                    0.7791392496558245,
                    0.7388745760013306,
                    0.6739605493576779,
                    0.6432673241279167,
                    0.7124181751534668,
                    0.669456709871883,
                    0.7067049471522552,
                    0.6685698115209102,
                    0.7430777123010961,
                    0.7510627360284545
                  ],
                  "xaxis": "x",
                  "yaxis": "y"
                }
              ],
              "layout": {
                "annotations": [
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "dataset=test",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.2425,
                    "yanchor": "middle",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "dataset=train",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.7575000000000001,
                    "yanchor": "middle",
                    "yref": "paper"
                  }
                ],
                "barmode": "overlay",
                "legend": {
                  "title": {
                    "text": "label"
                  },
                  "tracegroupgap": 0
                },
                "margin": {
                  "t": 60
                },
                "template": {
                  "data": {
                    "bar": [
                      {
                        "error_x": {
                          "color": "#2a3f5f"
                        },
                        "error_y": {
                          "color": "#2a3f5f"
                        },
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "bar"
                      }
                    ],
                    "barpolar": [
                      {
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "barpolar"
                      }
                    ],
                    "carpet": [
                      {
                        "aaxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "baxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "type": "carpet"
                      }
                    ],
                    "choropleth": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "choropleth"
                      }
                    ],
                    "contour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "contour"
                      }
                    ],
                    "contourcarpet": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "contourcarpet"
                      }
                    ],
                    "heatmap": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmap"
                      }
                    ],
                    "heatmapgl": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmapgl"
                      }
                    ],
                    "histogram": [
                      {
                        "marker": {
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "histogram"
                      }
                    ],
                    "histogram2d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2d"
                      }
                    ],
                    "histogram2dcontour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2dcontour"
                      }
                    ],
                    "mesh3d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "mesh3d"
                      }
                    ],
                    "parcoords": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "parcoords"
                      }
                    ],
                    "pie": [
                      {
                        "automargin": true,
                        "type": "pie"
                      }
                    ],
                    "scatter": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter"
                      }
                    ],
                    "scatter3d": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter3d"
                      }
                    ],
                    "scattercarpet": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattercarpet"
                      }
                    ],
                    "scattergeo": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergeo"
                      }
                    ],
                    "scattergl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergl"
                      }
                    ],
                    "scattermapbox": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattermapbox"
                      }
                    ],
                    "scatterpolar": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolar"
                      }
                    ],
                    "scatterpolargl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolargl"
                      }
                    ],
                    "scatterternary": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterternary"
                      }
                    ],
                    "surface": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "surface"
                      }
                    ],
                    "table": [
                      {
                        "cells": {
                          "fill": {
                            "color": "#EBF0F8"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "header": {
                          "fill": {
                            "color": "#C8D4E3"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "type": "table"
                      }
                    ]
                  },
                  "layout": {
                    "annotationdefaults": {
                      "arrowcolor": "#2a3f5f",
                      "arrowhead": 0,
                      "arrowwidth": 1
                    },
                    "autotypenumbers": "strict",
                    "coloraxis": {
                      "colorbar": {
                        "outlinewidth": 0,
                        "ticks": ""
                      }
                    },
                    "colorscale": {
                      "diverging": [
                        [
                          0,
                          "#8e0152"
                        ],
                        [
                          0.1,
                          "#c51b7d"
                        ],
                        [
                          0.2,
                          "#de77ae"
                        ],
                        [
                          0.3,
                          "#f1b6da"
                        ],
                        [
                          0.4,
                          "#fde0ef"
                        ],
                        [
                          0.5,
                          "#f7f7f7"
                        ],
                        [
                          0.6,
                          "#e6f5d0"
                        ],
                        [
                          0.7,
                          "#b8e186"
                        ],
                        [
                          0.8,
                          "#7fbc41"
                        ],
                        [
                          0.9,
                          "#4d9221"
                        ],
                        [
                          1,
                          "#276419"
                        ]
                      ],
                      "sequential": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ],
                      "sequentialminus": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ]
                    },
                    "colorway": [
                      "#636efa",
                      "#EF553B",
                      "#00cc96",
                      "#ab63fa",
                      "#FFA15A",
                      "#19d3f3",
                      "#FF6692",
                      "#B6E880",
                      "#FF97FF",
                      "#FECB52"
                    ],
                    "font": {
                      "color": "#2a3f5f"
                    },
                    "geo": {
                      "bgcolor": "white",
                      "lakecolor": "white",
                      "landcolor": "#E5ECF6",
                      "showlakes": true,
                      "showland": true,
                      "subunitcolor": "white"
                    },
                    "hoverlabel": {
                      "align": "left"
                    },
                    "hovermode": "closest",
                    "mapbox": {
                      "style": "light"
                    },
                    "paper_bgcolor": "white",
                    "plot_bgcolor": "#E5ECF6",
                    "polar": {
                      "angularaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "radialaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "scene": {
                      "xaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "yaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "zaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      }
                    },
                    "shapedefaults": {
                      "line": {
                        "color": "#2a3f5f"
                      }
                    },
                    "ternary": {
                      "aaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "baxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "caxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "title": {
                      "x": 0.05
                    },
                    "xaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    },
                    "yaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    }
                  }
                },
                "width": 500,
                "xaxis": {
                  "anchor": "y",
                  "domain": [
                    0,
                    0.98
                  ],
                  "title": {
                    "text": "cosine_similarity"
                  }
                },
                "xaxis2": {
                  "anchor": "y2",
                  "domain": [
                    0,
                    0.98
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "yaxis": {
                  "anchor": "x",
                  "domain": [
                    0,
                    0.485
                  ],
                  "title": {
                    "text": "count"
                  }
                },
                "yaxis2": {
                  "anchor": "x2",
                  "domain": [
                    0.515,
                    1
                  ],
                  "matches": "y",
                  "title": {
                    "text": "count"
                  }
                }
              }
            }
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "train accuracy: 89.1% ± 2.4%\n",
            "test accuracy: 88.8% ± 2.4%\n"
          ]
        }
      ],
      "source": [
        "# calculate accuracy (and its standard error) of predicting label=1 if similarity>x\n",
        "# x is optimized by sweeping from -1 to 1 in steps of 0.01\n",
        "def accuracy_and_se(cosine_similarity: float, labeled_similarity: int) -> Tuple[float]:\n",
        "    accuracies = []\n",
        "    for threshold_thousandths in range(-1000, 1000, 1):\n",
        "        threshold = threshold_thousandths / 1000\n",
        "        total = 0\n",
        "        correct = 0\n",
        "        for cs, ls in zip(cosine_similarity, labeled_similarity):\n",
        "            total += 1\n",
        "            if cs > threshold:\n",
        "                prediction = 1\n",
        "            else:\n",
        "                prediction = -1\n",
        "            if prediction == ls:\n",
        "                correct += 1\n",
        "        accuracy = correct / total\n",
        "        accuracies.append(accuracy)\n",
        "    a = max(accuracies)\n",
        "    n = len(cosine_similarity)\n",
        "    standard_error = (a * (1 - a) / n) ** 0.5  # standard error of binomial\n",
        "    return a, standard_error\n",
        "\n",
        "\n",
        "# check that training and test sets are balanced\n",
        "px.histogram(\n",
        "    df,\n",
        "    x=\"cosine_similarity\",\n",
        "    color=\"label\",\n",
        "    barmode=\"overlay\",\n",
        "    width=500,\n",
        "    facet_row=\"dataset\",\n",
        ").show()\n",
        "\n",
        "for dataset in [\"train\", \"test\"]:\n",
        "    data = df[df[\"dataset\"] == dataset]\n",
        "    a, se = accuracy_and_se(data[\"cosine_similarity\"], data[\"label\"])\n",
        "    print(f\"{dataset} accuracy: {a:0.1%} ± {1.96 * se:0.1%}\")\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "zHLxlnsApgkR"
      },
      "source": [
        "## 7. Optimize the matrix using the training data provided"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "z52V0x8IpgkR"
      },
      "outputs": [],
      "source": [
        "def embedding_multiplied_by_matrix(\n",
        "    embedding: List[float], matrix: torch.tensor\n",
        ") -> np.array:\n",
        "    embedding_tensor = torch.tensor(embedding).float()\n",
        "    modified_embedding = embedding_tensor @ matrix\n",
        "    modified_embedding = modified_embedding.detach().numpy()\n",
        "    return modified_embedding\n",
        "\n",
        "\n",
        "# compute custom embeddings and new cosine similarities\n",
        "def apply_matrix_to_embeddings_dataframe(matrix: torch.tensor, df: pd.DataFrame):\n",
        "    for column in [\"text_1_embedding\", \"text_2_embedding\"]:\n",
        "        df[f\"{column}_custom\"] = df[column].apply(\n",
        "            lambda x: embedding_multiplied_by_matrix(x, matrix)\n",
        "        )\n",
        "    df[\"cosine_similarity_custom\"] = df.apply(\n",
        "        lambda row: cosine_similarity(\n",
        "            row[\"text_1_embedding_custom\"], row[\"text_2_embedding_custom\"]\n",
        "        ),\n",
        "        axis=1,\n",
        "    )\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "p2ZSXu6spgkR"
      },
      "outputs": [],
      "source": [
        "def optimize_matrix(\n",
        "    modified_embedding_length: int = 2048,  # in my brief experimentation, bigger was better (2048 is length of babbage encoding)\n",
        "    batch_size: int = 100,\n",
        "    max_epochs: int = 100,\n",
        "    learning_rate: float = 100.0,  # seemed to work best when similar to batch size - feel free to try a range of values\n",
        "    dropout_fraction: float = 0.0,  # in my testing, dropout helped by a couple percentage points (definitely not necessary)\n",
        "    df: pd.DataFrame = df,\n",
        "    print_progress: bool = True,\n",
        "    save_results: bool = True,\n",
        ") -> torch.tensor:\n",
        "    \"\"\"Return matrix optimized to minimize loss on training data.\"\"\"\n",
        "    run_id = random.randint(0, 2 ** 31 - 1)  # (range is arbitrary)\n",
        "    # convert from dataframe to torch tensors\n",
        "    # e is for embedding, s for similarity label\n",
        "    def tensors_from_dataframe(\n",
        "        df: pd.DataFrame,\n",
        "        embedding_column_1: str,\n",
        "        embedding_column_2: str,\n",
        "        similarity_label_column: str,\n",
        "    ) -> Tuple[torch.tensor]:\n",
        "        e1 = np.stack(np.array(df[embedding_column_1].values))\n",
        "        e2 = np.stack(np.array(df[embedding_column_2].values))\n",
        "        s = np.stack(np.array(df[similarity_label_column].astype(\"float\").values))\n",
        "\n",
        "        e1 = torch.from_numpy(e1).float()\n",
        "        e2 = torch.from_numpy(e2).float()\n",
        "        s = torch.from_numpy(s).float()\n",
        "\n",
        "        return e1, e2, s\n",
        "\n",
        "    e1_train, e2_train, s_train = tensors_from_dataframe(\n",
        "        df[df[\"dataset\"] == \"train\"], \"text_1_embedding\", \"text_2_embedding\", \"label\"\n",
        "    )\n",
        "    e1_test, e2_test, s_test = tensors_from_dataframe(\n",
        "        df[df[\"dataset\"] == \"test\"], \"text_1_embedding\", \"text_2_embedding\", \"label\"\n",
        "    )\n",
        "\n",
        "    # create dataset and loader\n",
        "    dataset = torch.utils.data.TensorDataset(e1_train, e2_train, s_train)\n",
        "    train_loader = torch.utils.data.DataLoader(\n",
        "        dataset, batch_size=batch_size, shuffle=True\n",
        "    )\n",
        "\n",
        "    # define model (similarity of projected embeddings)\n",
        "    def model(embedding_1, embedding_2, matrix, dropout_fraction=dropout_fraction):\n",
        "        e1 = torch.nn.functional.dropout(embedding_1, p=dropout_fraction)\n",
        "        e2 = torch.nn.functional.dropout(embedding_2, p=dropout_fraction)\n",
        "        modified_embedding_1 = e1 @ matrix  # @ is matrix multiplication\n",
        "        modified_embedding_2 = e2 @ matrix\n",
        "        similarity = torch.nn.functional.cosine_similarity(\n",
        "            modified_embedding_1, modified_embedding_2\n",
        "        )\n",
        "        return similarity\n",
        "\n",
        "    # define loss function to minimize\n",
        "    def mse_loss(predictions, targets):\n",
        "        difference = predictions - targets\n",
        "        return torch.sum(difference * difference) / difference.numel()\n",
        "\n",
        "    # initialize projection matrix\n",
        "    embedding_length = len(df[\"text_1_embedding\"].values[0])\n",
        "    matrix = torch.randn(\n",
        "        embedding_length, modified_embedding_length, requires_grad=True\n",
        "    )\n",
        "\n",
        "    epochs, types, losses, accuracies, matrices = [], [], [], [], []\n",
        "    for epoch in range(1, 1 + max_epochs):\n",
        "        # iterate through training dataloader\n",
        "        for a, b, actual_similarity in train_loader:\n",
        "            # generate prediction\n",
        "            predicted_similarity = model(a, b, matrix)\n",
        "            # get loss and perform backpropagation\n",
        "            loss = mse_loss(predicted_similarity, actual_similarity)\n",
        "            loss.backward()\n",
        "            # update the weights\n",
        "            with torch.no_grad():\n",
        "                matrix -= matrix.grad * learning_rate\n",
        "                # set gradients to zero\n",
        "                matrix.grad.zero_()\n",
        "        # calculate test loss\n",
        "        test_predictions = model(e1_test, e2_test, matrix)\n",
        "        test_loss = mse_loss(test_predictions, s_test)\n",
        "\n",
        "        # compute custom embeddings and new cosine similarities\n",
        "        apply_matrix_to_embeddings_dataframe(matrix, df)\n",
        "\n",
        "        # calculate test accuracy\n",
        "        for dataset in [\"train\", \"test\"]:\n",
        "            data = df[df[\"dataset\"] == dataset]\n",
        "            a, se = accuracy_and_se(data[\"cosine_similarity_custom\"], data[\"label\"])\n",
        "\n",
        "            # record results of each epoch\n",
        "            epochs.append(epoch)\n",
        "            types.append(dataset)\n",
        "            losses.append(loss.item() if dataset == \"train\" else test_loss.item())\n",
        "            accuracies.append(a)\n",
        "            matrices.append(matrix.detach().numpy())\n",
        "\n",
        "            # optionally print accuracies\n",
        "            if print_progress is True:\n",
        "                print(\n",
        "                    f\"Epoch {epoch}/{max_epochs}: {dataset} accuracy: {a:0.1%} ± {1.96 * se:0.1%}\"\n",
        "                )\n",
        "\n",
        "    data = pd.DataFrame(\n",
        "        {\"epoch\": epochs, \"type\": types, \"loss\": losses, \"accuracy\": accuracies}\n",
        "    )\n",
        "    data[\"run_id\"] = run_id\n",
        "    data[\"modified_embedding_length\"] = modified_embedding_length\n",
        "    data[\"batch_size\"] = batch_size\n",
        "    data[\"max_epochs\"] = max_epochs\n",
        "    data[\"learning_rate\"] = learning_rate\n",
        "    data[\"dropout_fraction\"] = dropout_fraction\n",
        "    data[\n",
        "        \"matrix\"\n",
        "    ] = matrices  # saving every single matrix can get big; feel free to delete/change\n",
        "    if save_results is True:\n",
        "        data.to_csv(f\"{run_id}_optimization_results.csv\", index=False)\n",
        "\n",
        "    return data\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "nlcUW-zEpgkS",
        "outputId": "4bd4bdff-628a-406f-fffe-aedbfad66446"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Epoch 1/30: train accuracy: 89.1% ± 2.4%\n",
            "Epoch 1/30: test accuracy: 88.4% ± 2.4%\n",
            "Epoch 2/30: train accuracy: 89.5% ± 2.3%\n",
            "Epoch 2/30: test accuracy: 88.8% ± 2.4%\n",
            "Epoch 3/30: train accuracy: 90.6% ± 2.2%\n",
            "Epoch 3/30: test accuracy: 89.3% ± 2.3%\n",
            "Epoch 4/30: train accuracy: 91.2% ± 2.2%\n",
            "Epoch 4/30: test accuracy: 89.7% ± 2.3%\n",
            "Epoch 5/30: train accuracy: 91.5% ± 2.1%\n",
            "Epoch 5/30: test accuracy: 90.0% ± 2.3%\n",
            "Epoch 6/30: train accuracy: 91.9% ± 2.1%\n",
            "Epoch 6/30: test accuracy: 90.4% ± 2.2%\n",
            "Epoch 7/30: train accuracy: 92.2% ± 2.0%\n",
            "Epoch 7/30: test accuracy: 90.7% ± 2.2%\n",
            "Epoch 8/30: train accuracy: 92.7% ± 2.0%\n",
            "Epoch 8/30: test accuracy: 90.9% ± 2.2%\n",
            "Epoch 9/30: train accuracy: 92.7% ± 2.0%\n",
            "Epoch 9/30: test accuracy: 91.0% ± 2.2%\n",
            "Epoch 10/30: train accuracy: 93.0% ± 1.9%\n",
            "Epoch 10/30: test accuracy: 91.6% ± 2.1%\n",
            "Epoch 11/30: train accuracy: 93.1% ± 1.9%\n",
            "Epoch 11/30: test accuracy: 91.8% ± 2.1%\n",
            "Epoch 12/30: train accuracy: 93.4% ± 1.9%\n",
            "Epoch 12/30: test accuracy: 92.1% ± 2.0%\n",
            "Epoch 13/30: train accuracy: 93.6% ± 1.9%\n",
            "Epoch 13/30: test accuracy: 92.4% ± 2.0%\n",
            "Epoch 14/30: train accuracy: 93.7% ± 1.8%\n",
            "Epoch 14/30: test accuracy: 92.7% ± 2.0%\n",
            "Epoch 15/30: train accuracy: 93.7% ± 1.8%\n",
            "Epoch 15/30: test accuracy: 92.7% ± 2.0%\n",
            "Epoch 16/30: train accuracy: 94.0% ± 1.8%\n",
            "Epoch 16/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 17/30: train accuracy: 94.0% ± 1.8%\n",
            "Epoch 17/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 18/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 18/30: test accuracy: 93.1% ± 1.9%\n",
            "Epoch 19/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 19/30: test accuracy: 93.1% ± 1.9%\n",
            "Epoch 20/30: train accuracy: 94.3% ± 1.8%\n",
            "Epoch 20/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 21/30: train accuracy: 94.5% ± 1.7%\n",
            "Epoch 21/30: test accuracy: 93.1% ± 1.9%\n",
            "Epoch 22/30: train accuracy: 94.5% ± 1.7%\n",
            "Epoch 22/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 23/30: train accuracy: 94.6% ± 1.7%\n",
            "Epoch 23/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 24/30: train accuracy: 94.6% ± 1.7%\n",
            "Epoch 24/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 25/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 25/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 26/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 26/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 27/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 27/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 28/30: train accuracy: 94.9% ± 1.7%\n",
            "Epoch 28/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 29/30: train accuracy: 94.9% ± 1.7%\n",
            "Epoch 29/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 30/30: train accuracy: 94.9% ± 1.7%\n",
            "Epoch 30/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 1/30: train accuracy: 89.7% ± 2.3%\n",
            "Epoch 1/30: test accuracy: 89.1% ± 2.4%\n",
            "Epoch 2/30: train accuracy: 89.8% ± 2.3%\n",
            "Epoch 2/30: test accuracy: 89.9% ± 2.3%\n",
            "Epoch 3/30: train accuracy: 90.3% ± 2.2%\n",
            "Epoch 3/30: test accuracy: 90.0% ± 2.3%\n",
            "Epoch 4/30: train accuracy: 91.0% ± 2.2%\n",
            "Epoch 4/30: test accuracy: 90.3% ± 2.2%\n",
            "Epoch 5/30: train accuracy: 91.3% ± 2.1%\n",
            "Epoch 5/30: test accuracy: 90.3% ± 2.2%\n",
            "Epoch 6/30: train accuracy: 91.8% ± 2.1%\n",
            "Epoch 6/30: test accuracy: 90.4% ± 2.2%\n",
            "Epoch 7/30: train accuracy: 92.4% ± 2.0%\n",
            "Epoch 7/30: test accuracy: 91.0% ± 2.2%\n",
            "Epoch 8/30: train accuracy: 92.8% ± 2.0%\n",
            "Epoch 8/30: test accuracy: 91.3% ± 2.1%\n",
            "Epoch 9/30: train accuracy: 93.1% ± 1.9%\n",
            "Epoch 9/30: test accuracy: 91.6% ± 2.1%\n",
            "Epoch 10/30: train accuracy: 93.4% ± 1.9%\n",
            "Epoch 10/30: test accuracy: 91.9% ± 2.1%\n",
            "Epoch 11/30: train accuracy: 93.4% ± 1.9%\n",
            "Epoch 11/30: test accuracy: 91.8% ± 2.1%\n",
            "Epoch 12/30: train accuracy: 93.6% ± 1.9%\n",
            "Epoch 12/30: test accuracy: 92.1% ± 2.0%\n",
            "Epoch 13/30: train accuracy: 93.7% ± 1.8%\n",
            "Epoch 13/30: test accuracy: 92.4% ± 2.0%\n",
            "Epoch 14/30: train accuracy: 93.7% ± 1.8%\n",
            "Epoch 14/30: test accuracy: 92.5% ± 2.0%\n",
            "Epoch 15/30: train accuracy: 93.9% ± 1.8%\n",
            "Epoch 15/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 16/30: train accuracy: 94.0% ± 1.8%\n",
            "Epoch 16/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 17/30: train accuracy: 94.0% ± 1.8%\n",
            "Epoch 17/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 18/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 18/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 19/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 19/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 20/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 20/30: test accuracy: 93.1% ± 1.9%\n",
            "Epoch 21/30: train accuracy: 94.3% ± 1.8%\n",
            "Epoch 21/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 22/30: train accuracy: 94.3% ± 1.8%\n",
            "Epoch 22/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 23/30: train accuracy: 94.5% ± 1.7%\n",
            "Epoch 23/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 24/30: train accuracy: 94.5% ± 1.7%\n",
            "Epoch 24/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 25/30: train accuracy: 94.6% ± 1.7%\n",
            "Epoch 25/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 26/30: train accuracy: 94.6% ± 1.7%\n",
            "Epoch 26/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 27/30: train accuracy: 94.6% ± 1.7%\n",
            "Epoch 27/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 28/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 28/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 29/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 29/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 30/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 30/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 1/30: train accuracy: 90.7% ± 2.2%\n",
            "Epoch 1/30: test accuracy: 89.9% ± 2.3%\n",
            "Epoch 2/30: train accuracy: 90.9% ± 2.2%\n",
            "Epoch 2/30: test accuracy: 90.3% ± 2.2%\n",
            "Epoch 3/30: train accuracy: 91.6% ± 2.1%\n",
            "Epoch 3/30: test accuracy: 90.3% ± 2.2%\n",
            "Epoch 4/30: train accuracy: 92.2% ± 2.0%\n",
            "Epoch 4/30: test accuracy: 90.7% ± 2.2%\n",
            "Epoch 5/30: train accuracy: 92.4% ± 2.0%\n",
            "Epoch 5/30: test accuracy: 91.3% ± 2.1%\n",
            "Epoch 6/30: train accuracy: 92.5% ± 2.0%\n",
            "Epoch 6/30: test accuracy: 91.8% ± 2.1%\n",
            "Epoch 7/30: train accuracy: 93.0% ± 1.9%\n",
            "Epoch 7/30: test accuracy: 92.2% ± 2.0%\n",
            "Epoch 8/30: train accuracy: 93.1% ± 1.9%\n",
            "Epoch 8/30: test accuracy: 92.7% ± 2.0%\n",
            "Epoch 9/30: train accuracy: 93.3% ± 1.9%\n",
            "Epoch 9/30: test accuracy: 92.5% ± 2.0%\n",
            "Epoch 10/30: train accuracy: 93.4% ± 1.9%\n",
            "Epoch 10/30: test accuracy: 92.7% ± 2.0%\n",
            "Epoch 11/30: train accuracy: 93.6% ± 1.9%\n",
            "Epoch 11/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 12/30: train accuracy: 93.7% ± 1.8%\n",
            "Epoch 12/30: test accuracy: 92.8% ± 2.0%\n",
            "Epoch 13/30: train accuracy: 94.0% ± 1.8%\n",
            "Epoch 13/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 14/30: train accuracy: 93.9% ± 1.8%\n",
            "Epoch 14/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 15/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 15/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 16/30: train accuracy: 94.2% ± 1.8%\n",
            "Epoch 16/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 17/30: train accuracy: 94.3% ± 1.8%\n",
            "Epoch 17/30: test accuracy: 93.0% ± 1.9%\n",
            "Epoch 18/30: train accuracy: 94.5% ± 1.7%\n",
            "Epoch 18/30: test accuracy: 93.1% ± 1.9%\n",
            "Epoch 19/30: train accuracy: 94.5% ± 1.7%\n",
            "Epoch 19/30: test accuracy: 93.1% ± 1.9%\n",
            "Epoch 20/30: train accuracy: 94.6% ± 1.7%\n",
            "Epoch 20/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 21/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 21/30: test accuracy: 93.3% ± 1.9%\n",
            "Epoch 22/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 22/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 23/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 23/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 24/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 24/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 25/30: train accuracy: 94.8% ± 1.7%\n",
            "Epoch 25/30: test accuracy: 93.4% ± 1.9%\n",
            "Epoch 26/30: train accuracy: 94.9% ± 1.7%\n",
            "Epoch 26/30: test accuracy: 93.6% ± 1.9%\n",
            "Epoch 27/30: train accuracy: 94.9% ± 1.7%\n",
            "Epoch 27/30: test accuracy: 93.6% ± 1.9%\n",
            "Epoch 28/30: train accuracy: 94.9% ± 1.7%\n",
            "Epoch 28/30: test accuracy: 93.6% ± 1.9%\n",
            "Epoch 29/30: train accuracy: 95.1% ± 1.6%\n",
            "Epoch 29/30: test accuracy: 93.6% ± 1.9%\n",
            "Epoch 30/30: train accuracy: 95.1% ± 1.6%\n",
            "Epoch 30/30: test accuracy: 93.6% ± 1.9%\n"
          ]
        }
      ],
      "source": [
        "# example hyperparameter search\n",
        "# I recommend starting with max_epochs=10 while initially exploring\n",
        "results = []\n",
        "max_epochs = 30\n",
        "dropout_fraction = 0.2\n",
        "for batch_size, learning_rate in [(10, 10), (100, 100), (1000, 1000)]:\n",
        "    result = optimize_matrix(\n",
        "        batch_size=batch_size,\n",
        "        learning_rate=learning_rate,\n",
        "        max_epochs=max_epochs,\n",
        "        dropout_fraction=dropout_fraction,\n",
        "        save_results=False,\n",
        "    )\n",
        "    results.append(result)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "PoTZWC1SpgkS",
        "outputId": "207360e5-fd07-4180-a143-0ec5dd27ffe1"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.plotly.v1+json": {
              "config": {
                "plotlyServerURL": "https://plot.ly"
              },
              "data": [
                {
                  "customdata": [
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=train<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=1449308123<br>epoch=%{x}<br>loss=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "train",
                  "line": {
                    "color": "#636efa",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "train",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x7",
                  "y": [
                    1.1652076244354248,
                    0.8190054297447205,
                    0.9203463792800903,
                    0.9908844232559204,
                    0.8408004641532898,
                    0.7119297981262207,
                    0.6632728576660156,
                    0.8289280533790588,
                    0.8687358498573303,
                    0.8235021829605103,
                    0.895695149898529,
                    0.6677632331848145,
                    0.7526643872261047,
                    0.7708764672279358,
                    0.68276047706604,
                    0.6613249778747559,
                    0.5960850119590759,
                    0.8617165684700012,
                    0.724422037601471,
                    0.9765143394470215,
                    0.5958823561668396,
                    0.7277706265449524,
                    0.7929649353027344,
                    0.8311190009117126,
                    0.484933465719223,
                    0.6846191883087158,
                    0.6711297035217285,
                    0.738968551158905,
                    0.5267000198364258,
                    0.9111422300338745
                  ],
                  "yaxis": "y7"
                },
                {
                  "customdata": [
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=train<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=676326879<br>epoch=%{x}<br>loss=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "train",
                  "line": {
                    "color": "#636efa",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "train",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x5",
                  "y": [
                    1.06173574924469,
                    0.9195982813835144,
                    0.8605211973190308,
                    0.7780925631523132,
                    0.7680334448814392,
                    0.7896735072135925,
                    0.7652512788772583,
                    0.7015480399131775,
                    0.8019503951072693,
                    0.7844551801681519,
                    0.823682427406311,
                    0.711807131767273,
                    0.7855805158615112,
                    0.7014225125312805,
                    0.7862630486488342,
                    0.6663534045219421,
                    0.7388879060745239,
                    0.6876973509788513,
                    0.7274147272109985,
                    0.7191041111946106,
                    0.8075127601623535,
                    0.7195712924003601,
                    0.746185839176178,
                    0.7220138311386108,
                    0.7456589341163635,
                    0.6642791032791138,
                    0.7399784326553345,
                    0.7393214106559753,
                    0.6680636405944824,
                    0.6562733054161072
                  ],
                  "yaxis": "y5"
                },
                {
                  "customdata": [
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=train<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=881033356<br>epoch=%{x}<br>loss=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "train",
                  "line": {
                    "color": "#636efa",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "train",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x3",
                  "y": [
                    1.299358606338501,
                    1.0686416625976562,
                    0.8467883467674255,
                    0.7818496823310852,
                    0.7742239236831665,
                    0.7678887844085693,
                    0.7696077227592468,
                    0.766943097114563,
                    0.7572135925292969,
                    0.7593567967414856,
                    0.7546665668487549,
                    0.7499144077301025,
                    0.7492073178291321,
                    0.7394933700561523,
                    0.743760883808136,
                    0.7366983294487,
                    0.7340478301048279,
                    0.7297782897949219,
                    0.7292298674583435,
                    0.7229472994804382,
                    0.7246285080909729,
                    0.721783459186554,
                    0.7177888751029968,
                    0.7198930978775024,
                    0.7123011946678162,
                    0.7132685780525208,
                    0.7121831178665161,
                    0.7118210196495056,
                    0.7035670280456543,
                    0.7066351771354675
                  ],
                  "yaxis": "y3"
                },
                {
                  "customdata": [
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=test<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=1449308123<br>epoch=%{x}<br>loss=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "test",
                  "line": {
                    "color": "#EF553B",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "test",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x7",
                  "y": [
                    1.1514005661010742,
                    0.9815413355827332,
                    0.8687632083892822,
                    0.8124286532402039,
                    0.7918410301208496,
                    0.7831570506095886,
                    0.7777765393257141,
                    0.7735418677330017,
                    0.7701976895332336,
                    0.7720419764518738,
                    0.7726959586143494,
                    0.7650123834609985,
                    0.7650409936904907,
                    0.765683114528656,
                    0.7626248598098755,
                    0.7623012065887451,
                    0.7609940767288208,
                    0.7587862610816956,
                    0.7559080123901367,
                    0.7571383118629456,
                    0.7588285803794861,
                    0.7556950449943542,
                    0.7562108039855957,
                    0.7484216690063477,
                    0.7531804442405701,
                    0.7502257823944092,
                    0.7496891617774963,
                    0.7472137808799744,
                    0.748519241809845,
                    0.7483490705490112
                  ],
                  "yaxis": "y7"
                },
                {
                  "customdata": [
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=test<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=676326879<br>epoch=%{x}<br>loss=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "test",
                  "line": {
                    "color": "#EF553B",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "test",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x5",
                  "y": [
                    1.1180120706558228,
                    0.9514004588127136,
                    0.8425014019012451,
                    0.8078141212463379,
                    0.7853298187255859,
                    0.7790449857711792,
                    0.7733959555625916,
                    0.7792260646820068,
                    0.7700104117393494,
                    0.7700384855270386,
                    0.764447033405304,
                    0.7696305513381958,
                    0.7642591595649719,
                    0.7629777193069458,
                    0.7620665431022644,
                    0.7622931003570557,
                    0.7602745890617371,
                    0.7564830780029297,
                    0.761269748210907,
                    0.7550154328346252,
                    0.7560049295425415,
                    0.7538376450538635,
                    0.7503026127815247,
                    0.7528620958328247,
                    0.7485130429267883,
                    0.7481465339660645,
                    0.7483287453651428,
                    0.742965817451477,
                    0.7445206642150879,
                    0.7476803064346313
                  ],
                  "yaxis": "y5"
                },
                {
                  "customdata": [
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=test<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=881033356<br>epoch=%{x}<br>loss=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "test",
                  "line": {
                    "color": "#EF553B",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "test",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x3",
                  "y": [
                    1.0644111633300781,
                    0.8446540236473083,
                    0.783637285232544,
                    0.7773287892341614,
                    0.7771273851394653,
                    0.7754599452018738,
                    0.7732424736022949,
                    0.7710903882980347,
                    0.772106945514679,
                    0.7645512223243713,
                    0.7639281153678894,
                    0.7609775066375732,
                    0.7558433413505554,
                    0.7579177618026733,
                    0.7527595162391663,
                    0.7520467042922974,
                    0.7534357309341431,
                    0.7487133145332336,
                    0.7478086352348328,
                    0.747072160243988,
                    0.7411499619483948,
                    0.7459169030189514,
                    0.7451942563056946,
                    0.7394304275512695,
                    0.7337468862533569,
                    0.734693169593811,
                    0.7376500368118286,
                    0.7371401190757751,
                    0.731780469417572,
                    0.727291464805603
                  ],
                  "yaxis": "y3"
                }
              ],
              "layout": {
                "annotations": [
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "batch_size=10",
                    "x": 0.15666666666666665,
                    "xanchor": "center",
                    "xref": "paper",
                    "y": 0.9999999999999998,
                    "yanchor": "bottom",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "batch_size=100",
                    "x": 0.49,
                    "xanchor": "center",
                    "xref": "paper",
                    "y": 0.9999999999999998,
                    "yanchor": "bottom",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "batch_size=1000",
                    "x": 0.8233333333333333,
                    "xanchor": "center",
                    "xref": "paper",
                    "y": 0.9999999999999998,
                    "yanchor": "bottom",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "learning_rate=1000",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.15666666666666665,
                    "yanchor": "middle",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "learning_rate=100",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.4999999999999999,
                    "yanchor": "middle",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "learning_rate=10",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.8433333333333332,
                    "yanchor": "middle",
                    "yref": "paper"
                  }
                ],
                "legend": {
                  "title": {
                    "text": "type"
                  },
                  "tracegroupgap": 0
                },
                "margin": {
                  "t": 60
                },
                "template": {
                  "data": {
                    "bar": [
                      {
                        "error_x": {
                          "color": "#2a3f5f"
                        },
                        "error_y": {
                          "color": "#2a3f5f"
                        },
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "bar"
                      }
                    ],
                    "barpolar": [
                      {
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "barpolar"
                      }
                    ],
                    "carpet": [
                      {
                        "aaxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "baxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "type": "carpet"
                      }
                    ],
                    "choropleth": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "choropleth"
                      }
                    ],
                    "contour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "contour"
                      }
                    ],
                    "contourcarpet": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "contourcarpet"
                      }
                    ],
                    "heatmap": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmap"
                      }
                    ],
                    "heatmapgl": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmapgl"
                      }
                    ],
                    "histogram": [
                      {
                        "marker": {
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "histogram"
                      }
                    ],
                    "histogram2d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2d"
                      }
                    ],
                    "histogram2dcontour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2dcontour"
                      }
                    ],
                    "mesh3d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "mesh3d"
                      }
                    ],
                    "parcoords": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "parcoords"
                      }
                    ],
                    "pie": [
                      {
                        "automargin": true,
                        "type": "pie"
                      }
                    ],
                    "scatter": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter"
                      }
                    ],
                    "scatter3d": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter3d"
                      }
                    ],
                    "scattercarpet": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattercarpet"
                      }
                    ],
                    "scattergeo": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergeo"
                      }
                    ],
                    "scattergl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergl"
                      }
                    ],
                    "scattermapbox": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattermapbox"
                      }
                    ],
                    "scatterpolar": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolar"
                      }
                    ],
                    "scatterpolargl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolargl"
                      }
                    ],
                    "scatterternary": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterternary"
                      }
                    ],
                    "surface": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "surface"
                      }
                    ],
                    "table": [
                      {
                        "cells": {
                          "fill": {
                            "color": "#EBF0F8"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "header": {
                          "fill": {
                            "color": "#C8D4E3"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "type": "table"
                      }
                    ]
                  },
                  "layout": {
                    "annotationdefaults": {
                      "arrowcolor": "#2a3f5f",
                      "arrowhead": 0,
                      "arrowwidth": 1
                    },
                    "autotypenumbers": "strict",
                    "coloraxis": {
                      "colorbar": {
                        "outlinewidth": 0,
                        "ticks": ""
                      }
                    },
                    "colorscale": {
                      "diverging": [
                        [
                          0,
                          "#8e0152"
                        ],
                        [
                          0.1,
                          "#c51b7d"
                        ],
                        [
                          0.2,
                          "#de77ae"
                        ],
                        [
                          0.3,
                          "#f1b6da"
                        ],
                        [
                          0.4,
                          "#fde0ef"
                        ],
                        [
                          0.5,
                          "#f7f7f7"
                        ],
                        [
                          0.6,
                          "#e6f5d0"
                        ],
                        [
                          0.7,
                          "#b8e186"
                        ],
                        [
                          0.8,
                          "#7fbc41"
                        ],
                        [
                          0.9,
                          "#4d9221"
                        ],
                        [
                          1,
                          "#276419"
                        ]
                      ],
                      "sequential": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ],
                      "sequentialminus": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ]
                    },
                    "colorway": [
                      "#636efa",
                      "#EF553B",
                      "#00cc96",
                      "#ab63fa",
                      "#FFA15A",
                      "#19d3f3",
                      "#FF6692",
                      "#B6E880",
                      "#FF97FF",
                      "#FECB52"
                    ],
                    "font": {
                      "color": "#2a3f5f"
                    },
                    "geo": {
                      "bgcolor": "white",
                      "lakecolor": "white",
                      "landcolor": "#E5ECF6",
                      "showlakes": true,
                      "showland": true,
                      "subunitcolor": "white"
                    },
                    "hoverlabel": {
                      "align": "left"
                    },
                    "hovermode": "closest",
                    "mapbox": {
                      "style": "light"
                    },
                    "paper_bgcolor": "white",
                    "plot_bgcolor": "#E5ECF6",
                    "polar": {
                      "angularaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "radialaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "scene": {
                      "xaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "yaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "zaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      }
                    },
                    "shapedefaults": {
                      "line": {
                        "color": "#2a3f5f"
                      }
                    },
                    "ternary": {
                      "aaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "baxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "caxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "title": {
                      "x": 0.05
                    },
                    "xaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    },
                    "yaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    }
                  }
                },
                "width": 500,
                "xaxis": {
                  "anchor": "y",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "title": {
                    "text": "epoch"
                  }
                },
                "xaxis2": {
                  "anchor": "y2",
                  "domain": [
                    0.3333333333333333,
                    0.6466666666666666
                  ],
                  "matches": "x",
                  "title": {
                    "text": "epoch"
                  }
                },
                "xaxis3": {
                  "anchor": "y3",
                  "domain": [
                    0.6666666666666666,
                    0.98
                  ],
                  "matches": "x",
                  "title": {
                    "text": "epoch"
                  }
                },
                "xaxis4": {
                  "anchor": "y4",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis5": {
                  "anchor": "y5",
                  "domain": [
                    0.3333333333333333,
                    0.6466666666666666
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis6": {
                  "anchor": "y6",
                  "domain": [
                    0.6666666666666666,
                    0.98
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis7": {
                  "anchor": "y7",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis8": {
                  "anchor": "y8",
                  "domain": [
                    0.3333333333333333,
                    0.6466666666666666
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis9": {
                  "anchor": "y9",
                  "domain": [
                    0.6666666666666666,
                    0.98
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "yaxis": {
                  "anchor": "x",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "title": {
                    "text": "loss"
                  }
                },
                "yaxis2": {
                  "anchor": "x2",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis3": {
                  "anchor": "x3",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis4": {
                  "anchor": "x4",
                  "domain": [
                    0.34333333333333327,
                    0.6566666666666665
                  ],
                  "matches": "y",
                  "title": {
                    "text": "loss"
                  }
                },
                "yaxis5": {
                  "anchor": "x5",
                  "domain": [
                    0.34333333333333327,
                    0.6566666666666665
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis6": {
                  "anchor": "x6",
                  "domain": [
                    0.34333333333333327,
                    0.6566666666666665
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis7": {
                  "anchor": "x7",
                  "domain": [
                    0.6866666666666665,
                    0.9999999999999998
                  ],
                  "matches": "y",
                  "title": {
                    "text": "loss"
                  }
                },
                "yaxis8": {
                  "anchor": "x8",
                  "domain": [
                    0.6866666666666665,
                    0.9999999999999998
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis9": {
                  "anchor": "x9",
                  "domain": [
                    0.6866666666666665,
                    0.9999999999999998
                  ],
                  "matches": "y",
                  "showticklabels": false
                }
              }
            }
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "application/vnd.plotly.v1+json": {
              "config": {
                "plotlyServerURL": "https://plot.ly"
              },
              "data": [
                {
                  "customdata": [
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=train<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=1449308123<br>epoch=%{x}<br>accuracy=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "train",
                  "line": {
                    "color": "#636efa",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "train",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x7",
                  "y": [
                    0.8907185628742516,
                    0.8952095808383234,
                    0.905688622754491,
                    0.9116766467065869,
                    0.9146706586826348,
                    0.9191616766467066,
                    0.9221556886227545,
                    0.9266467065868264,
                    0.9266467065868264,
                    0.9296407185628742,
                    0.9311377245508982,
                    0.9341317365269461,
                    0.9356287425149701,
                    0.937125748502994,
                    0.937125748502994,
                    0.9401197604790419,
                    0.9401197604790419,
                    0.9416167664670658,
                    0.9416167664670658,
                    0.9431137724550899,
                    0.9446107784431138,
                    0.9446107784431138,
                    0.9461077844311377,
                    0.9461077844311377,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9491017964071856,
                    0.9491017964071856,
                    0.9491017964071856
                  ],
                  "yaxis": "y7"
                },
                {
                  "customdata": [
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=train<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=676326879<br>epoch=%{x}<br>accuracy=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "train",
                  "line": {
                    "color": "#636efa",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "train",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x5",
                  "y": [
                    0.8967065868263473,
                    0.8982035928143712,
                    0.9026946107784432,
                    0.9101796407185628,
                    0.9131736526946108,
                    0.9176646706586826,
                    0.9236526946107785,
                    0.9281437125748503,
                    0.9311377245508982,
                    0.9341317365269461,
                    0.9341317365269461,
                    0.9356287425149701,
                    0.937125748502994,
                    0.937125748502994,
                    0.938622754491018,
                    0.9401197604790419,
                    0.9401197604790419,
                    0.9416167664670658,
                    0.9416167664670658,
                    0.9416167664670658,
                    0.9431137724550899,
                    0.9431137724550899,
                    0.9446107784431138,
                    0.9446107784431138,
                    0.9461077844311377,
                    0.9461077844311377,
                    0.9461077844311377,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9476047904191617
                  ],
                  "yaxis": "y5"
                },
                {
                  "customdata": [
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=train<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=881033356<br>epoch=%{x}<br>accuracy=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "train",
                  "line": {
                    "color": "#636efa",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "train",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x3",
                  "y": [
                    0.907185628742515,
                    0.9086826347305389,
                    0.9161676646706587,
                    0.9221556886227545,
                    0.9236526946107785,
                    0.9251497005988024,
                    0.9296407185628742,
                    0.9311377245508982,
                    0.9326347305389222,
                    0.9341317365269461,
                    0.9356287425149701,
                    0.937125748502994,
                    0.9401197604790419,
                    0.938622754491018,
                    0.9416167664670658,
                    0.9416167664670658,
                    0.9431137724550899,
                    0.9446107784431138,
                    0.9446107784431138,
                    0.9461077844311377,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9476047904191617,
                    0.9491017964071856,
                    0.9491017964071856,
                    0.9491017964071856,
                    0.9505988023952096,
                    0.9505988023952096
                  ],
                  "yaxis": "y3"
                },
                {
                  "customdata": [
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ],
                    [
                      10,
                      10,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=test<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=1449308123<br>epoch=%{x}<br>accuracy=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "test",
                  "line": {
                    "color": "#EF553B",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "test",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x7",
                  "y": [
                    0.8835820895522388,
                    0.8880597014925373,
                    0.8925373134328358,
                    0.8970149253731343,
                    0.9,
                    0.9044776119402985,
                    0.9074626865671642,
                    0.908955223880597,
                    0.9104477611940298,
                    0.9164179104477612,
                    0.917910447761194,
                    0.9208955223880597,
                    0.9238805970149254,
                    0.926865671641791,
                    0.926865671641791,
                    0.9298507462686567,
                    0.9298507462686567,
                    0.9313432835820895,
                    0.9313432835820895,
                    0.9298507462686567,
                    0.9313432835820895,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.9328358208955224
                  ],
                  "yaxis": "y7"
                },
                {
                  "customdata": [
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ],
                    [
                      100,
                      100,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=test<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=676326879<br>epoch=%{x}<br>accuracy=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "test",
                  "line": {
                    "color": "#EF553B",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "test",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x5",
                  "y": [
                    0.891044776119403,
                    0.8985074626865671,
                    0.9,
                    0.9029850746268657,
                    0.9029850746268657,
                    0.9044776119402985,
                    0.9104477611940298,
                    0.9134328358208955,
                    0.9164179104477612,
                    0.9194029850746268,
                    0.917910447761194,
                    0.9208955223880597,
                    0.9238805970149254,
                    0.9253731343283582,
                    0.9283582089552239,
                    0.9283582089552239,
                    0.9283582089552239,
                    0.9283582089552239,
                    0.9283582089552239,
                    0.9313432835820895,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9343283582089552,
                    0.9328358208955224,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.9328358208955224,
                    0.9343283582089552
                  ],
                  "yaxis": "y5"
                },
                {
                  "customdata": [
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ],
                    [
                      1000,
                      1000,
                      0.2
                    ]
                  ],
                  "hovertemplate": "type=test<br>learning_rate=%{customdata[1]}<br>batch_size=%{customdata[0]}<br>run_id=881033356<br>epoch=%{x}<br>accuracy=%{y}<br>dropout_fraction=%{customdata[2]}<extra></extra>",
                  "legendgroup": "test",
                  "line": {
                    "color": "#EF553B",
                    "dash": "solid"
                  },
                  "marker": {
                    "symbol": "circle"
                  },
                  "mode": "lines",
                  "name": "test",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "scatter",
                  "x": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30
                  ],
                  "xaxis": "x3",
                  "y": [
                    0.8985074626865671,
                    0.9029850746268657,
                    0.9029850746268657,
                    0.9074626865671642,
                    0.9134328358208955,
                    0.917910447761194,
                    0.9223880597014925,
                    0.926865671641791,
                    0.9253731343283582,
                    0.926865671641791,
                    0.9283582089552239,
                    0.9283582089552239,
                    0.9298507462686567,
                    0.9298507462686567,
                    0.9298507462686567,
                    0.9298507462686567,
                    0.9298507462686567,
                    0.9313432835820895,
                    0.9313432835820895,
                    0.9328358208955224,
                    0.9328358208955224,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.9343283582089552,
                    0.935820895522388,
                    0.935820895522388,
                    0.935820895522388,
                    0.935820895522388,
                    0.935820895522388
                  ],
                  "yaxis": "y3"
                }
              ],
              "layout": {
                "annotations": [
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "batch_size=10",
                    "x": 0.15666666666666665,
                    "xanchor": "center",
                    "xref": "paper",
                    "y": 0.9999999999999998,
                    "yanchor": "bottom",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "batch_size=100",
                    "x": 0.49,
                    "xanchor": "center",
                    "xref": "paper",
                    "y": 0.9999999999999998,
                    "yanchor": "bottom",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "batch_size=1000",
                    "x": 0.8233333333333333,
                    "xanchor": "center",
                    "xref": "paper",
                    "y": 0.9999999999999998,
                    "yanchor": "bottom",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "learning_rate=1000",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.15666666666666665,
                    "yanchor": "middle",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "learning_rate=100",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.4999999999999999,
                    "yanchor": "middle",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "learning_rate=10",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.8433333333333332,
                    "yanchor": "middle",
                    "yref": "paper"
                  }
                ],
                "legend": {
                  "title": {
                    "text": "type"
                  },
                  "tracegroupgap": 0
                },
                "margin": {
                  "t": 60
                },
                "template": {
                  "data": {
                    "bar": [
                      {
                        "error_x": {
                          "color": "#2a3f5f"
                        },
                        "error_y": {
                          "color": "#2a3f5f"
                        },
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "bar"
                      }
                    ],
                    "barpolar": [
                      {
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "barpolar"
                      }
                    ],
                    "carpet": [
                      {
                        "aaxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "baxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "type": "carpet"
                      }
                    ],
                    "choropleth": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "choropleth"
                      }
                    ],
                    "contour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "contour"
                      }
                    ],
                    "contourcarpet": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "contourcarpet"
                      }
                    ],
                    "heatmap": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmap"
                      }
                    ],
                    "heatmapgl": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmapgl"
                      }
                    ],
                    "histogram": [
                      {
                        "marker": {
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "histogram"
                      }
                    ],
                    "histogram2d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2d"
                      }
                    ],
                    "histogram2dcontour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2dcontour"
                      }
                    ],
                    "mesh3d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "mesh3d"
                      }
                    ],
                    "parcoords": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "parcoords"
                      }
                    ],
                    "pie": [
                      {
                        "automargin": true,
                        "type": "pie"
                      }
                    ],
                    "scatter": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter"
                      }
                    ],
                    "scatter3d": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter3d"
                      }
                    ],
                    "scattercarpet": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattercarpet"
                      }
                    ],
                    "scattergeo": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergeo"
                      }
                    ],
                    "scattergl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergl"
                      }
                    ],
                    "scattermapbox": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattermapbox"
                      }
                    ],
                    "scatterpolar": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolar"
                      }
                    ],
                    "scatterpolargl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolargl"
                      }
                    ],
                    "scatterternary": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterternary"
                      }
                    ],
                    "surface": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "surface"
                      }
                    ],
                    "table": [
                      {
                        "cells": {
                          "fill": {
                            "color": "#EBF0F8"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "header": {
                          "fill": {
                            "color": "#C8D4E3"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "type": "table"
                      }
                    ]
                  },
                  "layout": {
                    "annotationdefaults": {
                      "arrowcolor": "#2a3f5f",
                      "arrowhead": 0,
                      "arrowwidth": 1
                    },
                    "autotypenumbers": "strict",
                    "coloraxis": {
                      "colorbar": {
                        "outlinewidth": 0,
                        "ticks": ""
                      }
                    },
                    "colorscale": {
                      "diverging": [
                        [
                          0,
                          "#8e0152"
                        ],
                        [
                          0.1,
                          "#c51b7d"
                        ],
                        [
                          0.2,
                          "#de77ae"
                        ],
                        [
                          0.3,
                          "#f1b6da"
                        ],
                        [
                          0.4,
                          "#fde0ef"
                        ],
                        [
                          0.5,
                          "#f7f7f7"
                        ],
                        [
                          0.6,
                          "#e6f5d0"
                        ],
                        [
                          0.7,
                          "#b8e186"
                        ],
                        [
                          0.8,
                          "#7fbc41"
                        ],
                        [
                          0.9,
                          "#4d9221"
                        ],
                        [
                          1,
                          "#276419"
                        ]
                      ],
                      "sequential": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ],
                      "sequentialminus": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ]
                    },
                    "colorway": [
                      "#636efa",
                      "#EF553B",
                      "#00cc96",
                      "#ab63fa",
                      "#FFA15A",
                      "#19d3f3",
                      "#FF6692",
                      "#B6E880",
                      "#FF97FF",
                      "#FECB52"
                    ],
                    "font": {
                      "color": "#2a3f5f"
                    },
                    "geo": {
                      "bgcolor": "white",
                      "lakecolor": "white",
                      "landcolor": "#E5ECF6",
                      "showlakes": true,
                      "showland": true,
                      "subunitcolor": "white"
                    },
                    "hoverlabel": {
                      "align": "left"
                    },
                    "hovermode": "closest",
                    "mapbox": {
                      "style": "light"
                    },
                    "paper_bgcolor": "white",
                    "plot_bgcolor": "#E5ECF6",
                    "polar": {
                      "angularaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "radialaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "scene": {
                      "xaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "yaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "zaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      }
                    },
                    "shapedefaults": {
                      "line": {
                        "color": "#2a3f5f"
                      }
                    },
                    "ternary": {
                      "aaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "baxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "caxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "title": {
                      "x": 0.05
                    },
                    "xaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    },
                    "yaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    }
                  }
                },
                "width": 500,
                "xaxis": {
                  "anchor": "y",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "title": {
                    "text": "epoch"
                  }
                },
                "xaxis2": {
                  "anchor": "y2",
                  "domain": [
                    0.3333333333333333,
                    0.6466666666666666
                  ],
                  "matches": "x",
                  "title": {
                    "text": "epoch"
                  }
                },
                "xaxis3": {
                  "anchor": "y3",
                  "domain": [
                    0.6666666666666666,
                    0.98
                  ],
                  "matches": "x",
                  "title": {
                    "text": "epoch"
                  }
                },
                "xaxis4": {
                  "anchor": "y4",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis5": {
                  "anchor": "y5",
                  "domain": [
                    0.3333333333333333,
                    0.6466666666666666
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis6": {
                  "anchor": "y6",
                  "domain": [
                    0.6666666666666666,
                    0.98
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis7": {
                  "anchor": "y7",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis8": {
                  "anchor": "y8",
                  "domain": [
                    0.3333333333333333,
                    0.6466666666666666
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "xaxis9": {
                  "anchor": "y9",
                  "domain": [
                    0.6666666666666666,
                    0.98
                  ],
                  "matches": "x",
                  "showticklabels": false
                },
                "yaxis": {
                  "anchor": "x",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "title": {
                    "text": "accuracy"
                  }
                },
                "yaxis2": {
                  "anchor": "x2",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis3": {
                  "anchor": "x3",
                  "domain": [
                    0,
                    0.3133333333333333
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis4": {
                  "anchor": "x4",
                  "domain": [
                    0.34333333333333327,
                    0.6566666666666665
                  ],
                  "matches": "y",
                  "title": {
                    "text": "accuracy"
                  }
                },
                "yaxis5": {
                  "anchor": "x5",
                  "domain": [
                    0.34333333333333327,
                    0.6566666666666665
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis6": {
                  "anchor": "x6",
                  "domain": [
                    0.34333333333333327,
                    0.6566666666666665
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis7": {
                  "anchor": "x7",
                  "domain": [
                    0.6866666666666665,
                    0.9999999999999998
                  ],
                  "matches": "y",
                  "title": {
                    "text": "accuracy"
                  }
                },
                "yaxis8": {
                  "anchor": "x8",
                  "domain": [
                    0.6866666666666665,
                    0.9999999999999998
                  ],
                  "matches": "y",
                  "showticklabels": false
                },
                "yaxis9": {
                  "anchor": "x9",
                  "domain": [
                    0.6866666666666665,
                    0.9999999999999998
                  ],
                  "matches": "y",
                  "showticklabels": false
                }
              }
            }
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "runs_df = pd.concat(results)\n",
        "\n",
        "# plot training loss and test loss over time\n",
        "px.line(\n",
        "    runs_df,\n",
        "    line_group=\"run_id\",\n",
        "    x=\"epoch\",\n",
        "    y=\"loss\",\n",
        "    color=\"type\",\n",
        "    hover_data=[\"batch_size\", \"learning_rate\", \"dropout_fraction\"],\n",
        "    facet_row=\"learning_rate\",\n",
        "    facet_col=\"batch_size\",\n",
        "    width=500,\n",
        ").show()\n",
        "\n",
        "# plot accuracy over time\n",
        "px.line(\n",
        "    runs_df,\n",
        "    line_group=\"run_id\",\n",
        "    x=\"epoch\",\n",
        "    y=\"accuracy\",\n",
        "    color=\"type\",\n",
        "    hover_data=[\"batch_size\", \"learning_rate\", \"dropout_fraction\"],\n",
        "    facet_row=\"learning_rate\",\n",
        "    facet_col=\"batch_size\",\n",
        "    width=500,\n",
        ").show()\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "MiBQDcMPpgkS"
      },
      "source": [
        "## 8. Plot the before & after, showing the results of the best matrix found during training\n",
        "\n",
        "The better the matrix is, the more cleanly it will separate the similar and dissimilar pairs."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "hzjoyLDOpgkS"
      },
      "outputs": [],
      "source": [
        "# apply result of best run to original data\n",
        "best_run = runs_df.sort_values(by=\"accuracy\", ascending=False).iloc[0]\n",
        "best_matrix = best_run[\"matrix\"]\n",
        "apply_matrix_to_embeddings_dataframe(best_matrix, df)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "nLnvABnXpgkS",
        "outputId": "0c070faa-6e3e-4765-b082-565c72a609be"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.plotly.v1+json": {
              "config": {
                "plotlyServerURL": "https://plot.ly"
              },
              "data": [
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=1<br>dataset=train<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "1",
                  "marker": {
                    "color": "#636efa",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "1",
                  "offsetgroup": "1",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "histogram",
                  "x": [
                    0.9267355919345323,
                    0.8959824209230313,
                    0.9119725922265434,
                    0.854066984766886,
                    0.892887342475088,
                    0.9197115510183956,
                    0.8645429616364463,
                    0.8314164166177409,
                    0.7243313891695883,
                    0.8819971504547897,
                    0.7956215051893748,
                    0.7959481856578454,
                    0.8682525487547492,
                    0.8973704561532523,
                    0.8648042605746787,
                    0.9236698981903941,
                    0.9834804742323746,
                    0.8152447410515193,
                    0.8251720025778885,
                    0.8138195587168373,
                    0.8041885875094662,
                    0.9329690881953521,
                    0.9560346908585096,
                    0.9727875559800526,
                    0.8739787488907723,
                    0.8208200937845748,
                    0.7246913159387628,
                    0.9324916305400826,
                    0.8285737172791849,
                    0.8797008558439083,
                    0.820333215489803,
                    0.9370111008629193,
                    0.8983827475968527,
                    0.8312111255338568,
                    0.8164052516323846,
                    0.8908148647559723,
                    0.7466264012908705,
                    0.749651964301876,
                    0.87375582683117,
                    0.7849398161817545,
                    0.8309506403579568,
                    0.9307212180139316,
                    0.8281747408531835,
                    0.9529528469109777,
                    0.7828662080109449,
                    0.887100957550481,
                    0.9000278356226864,
                    0.8805448739521785,
                    0.930239131235984,
                    0.8801954897699975,
                    0.8529206900756547,
                    0.9467797362617967,
                    0.950367690540818,
                    0.7030531843080301,
                    0.8643992401506337,
                    0.8536886651933216,
                    0.9619331104636477,
                    0.9798279220663803,
                    0.8545739729953584,
                    0.8957115039259408,
                    0.8241137169318955,
                    0.8234984837204449,
                    0.8936706246811023,
                    0.8987178417246647,
                    0.9081806514389928,
                    0.9208852073112466,
                    0.8961858080980447,
                    0.8831329491347061,
                    0.9282623092166472,
                    0.8990849228018752,
                    0.8284548395672304,
                    0.8202091311790463,
                    0.8647762700375631,
                    0.840136958242196,
                    0.9887387562448309,
                    0.833342655983456,
                    0.828533112298018,
                    0.9117757392019592,
                    0.8706628948983062,
                    0.9279786042901599,
                    0.7389559895894061,
                    0.8433932035736679,
                    0.9240307526722153,
                    0.950769936374633,
                    0.8586024431762636,
                    0.8685107120156628,
                    0.875535036209879,
                    0.9894909159640456,
                    0.8279650063634755,
                    0.9108703739124493,
                    0.9090161898700972,
                    0.8603952576151226,
                    0.7791958170479588,
                    0.8800175078297319,
                    0.8442387843179446,
                    0.7672266106337577,
                    0.9379753906877134,
                    0.8637536227406404,
                    0.9190295684769377,
                    0.813748744480001,
                    0.9134886375270357,
                    0.8043760086358624,
                    0.8792300492020616,
                    0.8716796296133559,
                    0.8669146731224541,
                    0.7736224659067634,
                    0.9437235456545872,
                    0.905686329875817,
                    0.9534823418409002,
                    0.9150626356433706,
                    0.9409873570135594,
                    0.8111212499450311,
                    0.9171209901271343,
                    0.9126582215550586,
                    0.8337042981493767,
                    0.7317859043960847,
                    0.8444929460069593,
                    0.8561920422842992,
                    0.7765276739806221,
                    0.8526116779814181,
                    0.9178549171995068,
                    0.9238337665547537,
                    0.7218806795387105,
                    0.8180162420894919,
                    0.9687438998025378,
                    0.8354559162714565,
                    0.9146160667909478,
                    0.8082103463995212,
                    0.9563444955040953,
                    0.9066029892990775,
                    0.8485102485675593,
                    0.8154210965438722,
                    0.8860338155558548,
                    0.9280705420457523,
                    0.9835182434488767,
                    0.9653797793986199,
                    0.7815047672209323,
                    0.7156150747063292,
                    0.9256075945804699,
                    0.8135073898727201,
                    0.965501517353668,
                    0.8222681603043882,
                    0.907212186549752,
                    0.8611990749004483,
                    0.9075083701591861,
                    0.9452697087352507,
                    0.8792221638449876,
                    0.9261547230875113,
                    0.8628843081873457,
                    0.7825774684929468,
                    0.826587869384389,
                    0.7399697967202743,
                    0.7855475169419611,
                    0.9111614040328055,
                    0.8871057104665023,
                    0.8824403169032524,
                    0.8618250237448342,
                    0.9787037901590712,
                    0.8066230600465234,
                    0.82769109211187,
                    0.9246432066709112,
                    0.8840853142719706,
                    0.786484352300887,
                    0.9106863314452291,
                    0.9342800776988389,
                    0.8573335079738363,
                    0.7780871062391552,
                    0.7913314665963198,
                    0.8574377397709955,
                    0.9078366114351649,
                    0.7529739278117176,
                    0.8630106564789936,
                    0.9051526759332171,
                    0.7715467442267975,
                    0.894146587858075,
                    0.8095881901541373,
                    0.7733578316514722,
                    0.7600408374028372,
                    0.7819972017869313,
                    0.9003461714649055,
                    0.7428048011790054,
                    0.8645936498599726,
                    0.8158769881622202,
                    0.8338827592994027,
                    0.8272653967731632,
                    0.9017517376316297,
                    0.8480852025321463,
                    0.7970818331146111,
                    0.84837067058732,
                    0.9272909953469497,
                    0.9511439765702141,
                    0.8796630924442385,
                    0.8297595339070903,
                    0.8132311695727563,
                    0.846096509352579,
                    0.8787645385610889,
                    0.8591367322994465,
                    0.8452813265723063,
                    0.708120854745005,
                    0.8769677220320785,
                    0.957621649201,
                    0.7463356296247886,
                    0.8618039385828121,
                    0.9560112462834625,
                    0.8478374736767776,
                    0.769289015775232,
                    0.8456866935685449,
                    0.9014601942765245,
                    0.8816990623836058,
                    0.8836365012367311,
                    0.8078009762348856,
                    0.898471670333294,
                    0.9064470715463968,
                    0.8762712610709371,
                    0.9178852315161201,
                    0.7896235958446132,
                    0.8939345739482307,
                    0.9534018415944343,
                    0.8358882135213556,
                    0.9488657107840998,
                    0.9046799883600772,
                    0.7583576517359092,
                    0.9080459939022663,
                    0.7709722685822517,
                    0.9635512477648485,
                    0.9792712672362888,
                    0.8526700765974843,
                    0.8278133097990042,
                    0.9735858611728696,
                    0.721230194834802,
                    0.8257425311085005,
                    0.9243205490037274,
                    0.9183796453898277,
                    0.9029146937248601,
                    0.9410246048181872,
                    0.9609604036664618,
                    0.7467407974920351,
                    0.8831901217813377,
                    0.8173287200784538,
                    0.8067347032404598,
                    0.7921957436175584,
                    0.9110994793014074,
                    0.8678737504217436,
                    0.9117743220816726,
                    0.781256498099708,
                    0.8553931170417658,
                    0.8798565764815073,
                    0.8485358179238083,
                    0.7748765495278522,
                    0.9432062986428599,
                    0.8328320716129907,
                    0.7983629771463491,
                    0.9345589964322458,
                    0.780034700168418,
                    0.9894680324844076,
                    0.8239308905190431,
                    0.8236003498823307,
                    0.8346101074957768,
                    0.8273793488443836,
                    0.7872103673165679,
                    0.9502897884724039,
                    0.83306630344504,
                    0.9346568240975981,
                    0.8082083566882774,
                    0.8920672687911747,
                    0.8566523137465843,
                    0.7636170858064102,
                    0.8271498146927989,
                    0.8450776675259235,
                    0.9045266249905214,
                    0.8578964053464326,
                    0.8673866119197355,
                    0.8804224181917263,
                    0.8199459545727489,
                    0.932410033971128,
                    0.9096821262750205,
                    0.8658255622247675,
                    0.9386720385226357,
                    0.8517830114204678,
                    0.889433736353776,
                    0.978847593529176,
                    0.8369738178686744,
                    0.8438616304896431,
                    0.9457050132083015,
                    0.8699723446274389,
                    0.7795221418941651,
                    0.9136284834408402,
                    0.839461038218975,
                    0.9453279809479284,
                    0.7899532071809374,
                    0.9078373589637019,
                    0.8434980548175782,
                    0.8112068688921613,
                    0.9466506411385276,
                    0.931413666561485,
                    0.7932453730948084,
                    0.8205411414836395,
                    0.9243834389669592,
                    0.719616209472987,
                    0.7552985082978257,
                    0.9593440978701407,
                    0.917557937781671,
                    0.8643861907339583,
                    0.8315201130646898,
                    0.7608819746989568,
                    0.9704324558544556,
                    0.8037085307118571,
                    0.7785270629127378,
                    0.8044961889638995,
                    0.8313307525316546,
                    0.8064106357955508,
                    0.9291149169587132,
                    0.8412940941318643,
                    0.6917091086045903,
                    0.895204432897799,
                    0.8182250729145697,
                    0.8645847241904496,
                    0.8532020284403578,
                    0.8143634597102418,
                    0.8825747762544934,
                    0.7764652529619696,
                    0.850099367461302,
                    0.8616919096196407,
                    0.9257293995599788,
                    0.935772204341753,
                    0.7742657205171264,
                    0.7898710076766889,
                    0.8590438495382458,
                    0.9317809680608741,
                    0.9087109944408146,
                    0.949297999227784,
                    0.8813316524294974,
                    0.7372081408133433,
                    0.8838176418404169
                  ],
                  "xaxis": "x2",
                  "yaxis": "y2"
                },
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=1<br>dataset=test<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "1",
                  "marker": {
                    "color": "#636efa",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "1",
                  "offsetgroup": "1",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "histogram",
                  "x": [
                    0.9424796847531719,
                    0.9078956620721231,
                    0.8334324872928349,
                    0.9352180099421901,
                    0.9055462980371385,
                    0.8981939710469806,
                    0.8310153256803275,
                    0.8504676050313356,
                    0.8456281884302819,
                    0.8845204616348977,
                    0.9575409743129409,
                    0.8867362111499236,
                    0.8268148049156373,
                    0.9197424487445726,
                    0.7868932880014918,
                    0.7584994087629051,
                    0.9184151106611779,
                    0.8634069821364065,
                    0.8347803687511831,
                    0.8293627315810226,
                    0.9290633380383377,
                    0.8385821691321573,
                    0.9389267221382397,
                    0.890818442649049,
                    0.86634760562554,
                    0.8406483291061461,
                    0.8084243397427517,
                    0.8909500804242533,
                    0.9262896019507018,
                    0.8955541231110083,
                    0.8055268512037249,
                    0.758607678624549,
                    0.9609058491722305,
                    0.91495905751538,
                    0.8670137150812314,
                    0.8813831602682358,
                    0.8602255150075953,
                    0.9239960998195261,
                    0.91732217769794,
                    0.8037285395908439,
                    0.9196344979660896,
                    0.8179495018382927,
                    0.9015423003762686,
                    0.9054394610623084,
                    0.9309412941515826,
                    0.9421722892808463,
                    0.7632823176731237,
                    0.8622055676377434,
                    0.9855273108710355,
                    0.9144155566597573,
                    0.916057392559463,
                    0.8027504546689012,
                    0.7131090055200247,
                    0.86174194818737,
                    0.982873171115144,
                    0.8100227539053508,
                    0.8923878603823862,
                    0.8096643432711604,
                    0.8707613707684018,
                    0.8786740148818871,
                    0.8274639911687568,
                    0.8927098767487393,
                    0.9565597075186062,
                    0.9060728095743347,
                    0.738307517030644,
                    0.9645943657917937,
                    0.8755564011033787,
                    0.879644342330288,
                    0.8679709669180851,
                    0.9304235148160597,
                    0.8902804960376421,
                    0.8748369557157689,
                    0.9999999999999999,
                    0.7979398167195422,
                    0.8182553472910762,
                    0.7782108671759803,
                    0.8427610550014142,
                    0.8696408842646327,
                    0.8747903026537825,
                    0.914973368517656,
                    0.9651568968718233,
                    0.9775547988384379,
                    0.8964005885715726,
                    0.8689760349348122,
                    0.8501707274497268,
                    0.9069421089316828,
                    0.7682621587597694,
                    0.9658683147667629,
                    0.8946443487011166,
                    0.7855154267442119,
                    0.8963791544804274,
                    0.8062904921192978,
                    0.8165205978948239,
                    0.8392522254625653,
                    0.9456080863923884,
                    0.7904904126133966,
                    0.833126792097794,
                    0.7852156051245299,
                    0.7859162398886373,
                    0.9097674992318959,
                    0.8868692153350769,
                    0.9391826646753169,
                    0.9428151202937937,
                    0.7923603877885725,
                    0.9018727189911658,
                    0.9723161942344292,
                    0.7820369113228325,
                    0.9667234201162873,
                    0.978769627389609,
                    0.9155729781931277,
                    0.8273013970664075,
                    0.9603319621485501,
                    0.9298975009081959,
                    0.8775117467919693,
                    0.8614509568162568,
                    0.9144155657624043,
                    0.7783710792186642,
                    0.9701880190033496,
                    0.7858944693777298,
                    0.9278353490304795,
                    0.9472367444800102,
                    0.7834809788888359,
                    0.7997358978342995,
                    0.8459052935830644,
                    0.8612076995259889,
                    0.8470901722260982,
                    0.824037271004761,
                    0.865608650068826,
                    0.8023193246081538,
                    0.7836788857151791,
                    0.880404135119559,
                    0.8491559249509729,
                    0.788345270395367,
                    0.9461393747813323,
                    0.835123385080455,
                    0.8158174048388718,
                    0.8604581300972295,
                    0.9623616555004862,
                    0.8564688397784819,
                    0.8576867681204893,
                    0.8973905356978807,
                    0.8634447095761868,
                    0.8149528594606367,
                    0.873171253801101,
                    0.8653347676818378,
                    0.929525558735665,
                    0.8358267202818717,
                    0.971888682386554,
                    0.8500189240129448,
                    0.6201715858790215,
                    0.8982737437906866,
                    0.8919523978597029,
                    0.7327218620224804,
                    0.8329671225228632,
                    0.9265589851585685,
                    0.8976605724257473,
                    0.8865148832512937,
                    0.7893917264917192,
                    0.7303107673595587,
                    0.8428958487387793,
                    0.8712646524042454,
                    0.9726111208329614,
                    0.9368020234351375,
                    0.9270010843622818,
                    0.8900608737128451,
                    0.7975173141451626,
                    0.9403308743666237,
                    0.8484005148509558,
                    0.9285585494125882,
                    0.8461714640960527,
                    0.9301612552439464,
                    0.9840391344904358,
                    0.8305503032909712,
                    0.8985536902480058,
                    0.9476344055766088,
                    0.9342892661789283,
                    0.8849523247638441,
                    0.7736620851030366,
                    0.8083290901088768,
                    0.9510007696957726,
                    0.8677438102591386,
                    0.8324233959261911,
                    0.7379868650067231,
                    0.9049462205283083,
                    0.9044068964151009,
                    0.7810399099399672,
                    0.9040280419401343,
                    0.7720832557964016,
                    0.7168259249496903,
                    0.8657076231674912,
                    0.9689982290529879,
                    0.9330371348632155,
                    0.7014093149115691,
                    0.9056081832768474,
                    0.8483474394912361,
                    0.8729108893663646,
                    0.8494252835407102,
                    0.8702668029663239,
                    0.8703072652243842,
                    0.9279473628052111,
                    0.8615930026010632,
                    0.7590822846968434,
                    0.8435232136599701,
                    0.8264379743713927,
                    0.8793126202650794,
                    0.847452301256391,
                    0.7546334370590053,
                    0.8870818568791698,
                    0.8349553719854912,
                    0.9232007589383142,
                    0.7924421895458662,
                    0.8556103146657943,
                    0.8397958720336148,
                    0.9358165878534705,
                    0.904577353436614,
                    0.9022537114781464,
                    0.775603917181226,
                    0.946091618927627,
                    0.8264119461162666,
                    0.8261258105029201,
                    0.8605336598142989,
                    0.7518422489499549,
                    0.849587557879856,
                    0.9922578397415717,
                    0.7499254104864422,
                    0.8845204616348977,
                    0.8361936554693772,
                    0.9172228808488442,
                    0.8068135566092208,
                    0.795739929008372,
                    0.8632611464779958,
                    0.7612462576141025,
                    0.9589125421073597,
                    0.9555759038945358,
                    0.8822980105025566,
                    0.9663740139243834,
                    0.9071760951442449,
                    0.9335338894977118,
                    0.8042262160785201,
                    0.9399607295068667,
                    0.8318513711395181,
                    0.8697471272873054,
                    0.9103391819002411,
                    0.8272582065159091,
                    0.7868989539137853,
                    0.7416168920325092,
                    0.8828593510646834,
                    0.9141342991325323,
                    0.7259887492833588,
                    0.9478299721997572,
                    0.843766518385904,
                    0.919830425538435,
                    0.9069062941852448,
                    0.9036466185261808,
                    0.9817542893707696,
                    0.8833292621745382,
                    0.832556614533968,
                    0.8135910443631924,
                    0.9628932969024508,
                    0.9450804655496136,
                    0.9226384091529121,
                    0.8401818103049188,
                    0.723691406760321,
                    0.6828741135249211,
                    0.834410523069395,
                    0.9959256404542386,
                    0.952870396433041,
                    0.969514692554192,
                    0.9220387806044666,
                    0.9511950116111251,
                    0.87442203104197,
                    0.8399026046246612,
                    0.9029483760650204,
                    0.9097073428917352,
                    0.8651925582004045,
                    0.9178332691819033,
                    0.7556713752294848,
                    0.8601740894614596,
                    0.8250804250840363,
                    0.799473306929639,
                    0.8911389639861809,
                    0.915913776235107,
                    0.7867422041389165,
                    0.8035116695233039,
                    0.7702882636946234,
                    0.9060460430333088,
                    0.7214029229730072,
                    0.8607904806397634,
                    0.8228468643082103,
                    0.8900020169140401,
                    0.9343567736626528,
                    0.9305049279291139,
                    0.9664193138643489,
                    0.9008537853184969,
                    0.7625840742620333,
                    0.815302054727336,
                    0.9215061720798934,
                    0.7192673801865671,
                    0.8949994067748966,
                    0.9367566547265034,
                    0.7602684166275758,
                    0.8184439767612992,
                    0.8361983856596491,
                    0.7761725471827079,
                    0.7724780968772909,
                    0.9249211346782868,
                    0.8718843131924867,
                    0.8522890335712519,
                    0.9015475867709434,
                    0.8720699810318118,
                    0.8937599387455695,
                    0.8721713573852221,
                    0.8100783166142076,
                    1.0000000000000002,
                    0.8213222537973748,
                    0.8361185401136565,
                    0.8371907459006128,
                    0.9065697385076582,
                    0.752240671472798,
                    0.8283078905766531,
                    0.8499886819287953,
                    0.9097932369637356,
                    0.9529813104528191,
                    0.8449289750214674,
                    1,
                    0.8302949362084788,
                    0.7741532046500113,
                    0.8743828037305432,
                    0.8201855611163867,
                    0.8194689758101458,
                    0.7925076796225758,
                    0.8748126117575765,
                    0.8299510305557958,
                    0.9619426561868236,
                    0.8627070029199212
                  ],
                  "xaxis": "x",
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=-1<br>dataset=train<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "-1",
                  "marker": {
                    "color": "#EF553B",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "-1",
                  "offsetgroup": "-1",
                  "orientation": "v",
                  "showlegend": true,
                  "type": "histogram",
                  "x": [
                    0.7299945446332757,
                    0.761829365033925,
                    0.676235270353631,
                    0.7023016593603112,
                    0.7350156032869306,
                    0.7735236691667362,
                    0.7187241641280292,
                    0.8063818744486255,
                    0.7115273138749911,
                    0.7402039545462252,
                    0.7372226375565185,
                    0.719606336264161,
                    0.8344052997670786,
                    0.6881482918877712,
                    0.650513335277676,
                    0.7182967436895931,
                    0.7659970793010594,
                    0.6361476177437694,
                    0.7957002158983555,
                    0.7395402073375513,
                    0.7614384854511241,
                    0.6835300790002988,
                    0.6209194558826169,
                    0.7907726220786139,
                    0.7215750502680501,
                    0.7271947538454276,
                    0.6962333614625641,
                    0.7517476038206041,
                    0.7135529871009506,
                    0.7522919529124952,
                    0.7120639628754573,
                    0.7623014780353815,
                    0.7939574492876662,
                    0.6998873138766412,
                    0.7700594720774577,
                    0.7766161530342343,
                    0.7285080945118152,
                    0.7562511166739386,
                    0.8086622737220109,
                    0.7565297004511734,
                    0.7315242427462245,
                    0.791225232078265,
                    0.7281092467134649,
                    0.7675685917886341,
                    0.7122436997016454,
                    0.7600255476588682,
                    0.769465992253443,
                    0.7552507233110458,
                    0.7373719614604455,
                    0.7681449827665134,
                    0.7760194768221379,
                    0.8035677492769473,
                    0.7771752906080505,
                    0.6514739683312004,
                    0.744787832649546,
                    0.7700232252518491,
                    0.6901772464238046,
                    0.721128796446804,
                    0.686814078974691,
                    0.796786900996621,
                    0.8242176320872988,
                    0.7806742901384496,
                    0.7697696656361902,
                    0.7868668497422822,
                    0.7304548331410279,
                    0.7296767182508448,
                    0.699401040331297,
                    0.8332660282838579,
                    0.6513224421864793,
                    0.6927364371405096,
                    0.7491793002300279,
                    0.7909034218879171,
                    0.7754176150761527,
                    0.8004827006684735,
                    0.6659923526948868,
                    0.8129618884980553,
                    0.7496476113488948,
                    0.6519665061955423,
                    0.7319506042291191,
                    0.7367099004846358,
                    0.8590817275589286,
                    0.6684490623528697,
                    0.7469140136676841,
                    0.7269016830127544,
                    0.6834261236240542,
                    0.6390380393123325,
                    0.7129209978685723,
                    0.6879274953497815,
                    0.6720427402498903,
                    0.7343923261152341,
                    0.5977941468082364,
                    0.7574521074337901,
                    0.7302129263006347,
                    0.7380209108764002,
                    0.7280177437983031,
                    0.6870880300968067,
                    0.6928024686173956,
                    0.6403900073451696,
                    0.7209247906698092,
                    0.666799070142464,
                    0.7233569397428488,
                    0.7555267048881131,
                    0.7275931437975757,
                    0.7562785127332186,
                    0.736649021802634,
                    0.762569980781232,
                    0.7741923768467133,
                    0.6669773662198453,
                    0.7499779113599104,
                    0.7783371410262362,
                    0.7798574909618832,
                    0.7068277719647446,
                    0.7718066533969561,
                    0.7078874155127759,
                    0.7238814624322412,
                    0.8729026036201937,
                    0.7106759057210158,
                    0.7585767440008555,
                    0.6923565683937588,
                    0.6693898561996529,
                    0.7219944003835542,
                    0.7188064794656569,
                    0.7491451951131076,
                    0.6750197249394477,
                    0.7009868838756784,
                    0.6519589230722103,
                    0.775109860666869,
                    0.6682014813660948,
                    0.6618358724923147,
                    0.6218362070243146,
                    0.7518134154555007,
                    0.7571307427362168,
                    0.7546823360234822,
                    0.7416435744760188,
                    0.7676464608286054,
                    0.5799855321635428,
                    0.796191792361925,
                    0.6845373357552841,
                    0.7667984177770908,
                    0.7393609881148844,
                    0.7544580057165962,
                    0.7397495323890664,
                    0.7658298386950907,
                    0.6611125314078552,
                    0.7977728876184589,
                    0.831090991824215,
                    0.6982347705041605,
                    0.6312226759947304,
                    0.6482907496231076,
                    0.7658362595299695,
                    0.7518400125995974,
                    0.8025480920087656,
                    0.7461501494015976,
                    0.7239149641844659,
                    0.7090055516721123,
                    0.6846622430587006,
                    0.7112212118684095,
                    0.6794460508450644,
                    0.8344462829585355,
                    0.7638782230495382,
                    0.6558255308015893,
                    0.6799836520005059,
                    0.7148088830660722,
                    0.7658007439571484,
                    0.6581857665503666,
                    0.648734015773256,
                    0.8156725527309459,
                    0.6929202590284855,
                    0.7490919589112273,
                    0.7090723359022927,
                    0.7105572886194162,
                    0.7461374422467866,
                    0.7084742440808511,
                    0.6889378818898818,
                    0.7551565238112727,
                    0.7198789279593328,
                    0.7270482774940944,
                    0.6971190427893721,
                    0.7391610904601401,
                    0.6344734499604212,
                    0.6719507302378157,
                    0.6861159059531602,
                    0.6516118314317232,
                    0.7199095105818035,
                    0.6817881072485698,
                    0.7207373940156253,
                    0.7745467156569463,
                    0.6258059783246434,
                    0.7481056513643776,
                    0.7183327989261993,
                    0.7624705969064652,
                    0.703717229048042,
                    0.7487365873620485,
                    0.7495555007485976,
                    0.6409624588579408,
                    0.7176245775200687,
                    0.7537100520717849,
                    0.7569868075002099,
                    0.7392135510982174,
                    0.7188471960732984,
                    0.697413550280765,
                    0.7138614496887067,
                    0.7057641350396069,
                    0.7675079665142936,
                    0.7310427541091186,
                    0.7808018818735418,
                    0.7567255895826445,
                    0.7035962262766099,
                    0.7040750813384501,
                    0.8183159919038065,
                    0.7953911933398697,
                    0.7464891038038547,
                    0.6751591827598264,
                    0.7849943676377955,
                    0.7155963442284841,
                    0.7428993249606122,
                    0.7131100645054201,
                    0.7227595311429733,
                    0.6519548345531954,
                    0.7201522118536183,
                    0.86540799716664,
                    0.8128819241371503,
                    0.7278912446692862,
                    0.7305867175950502,
                    0.7171875192153516,
                    0.6755179003509543,
                    0.7256221359402913,
                    0.7003814947129137,
                    0.7486334697158199,
                    0.7232489166529666,
                    0.7347697330652992,
                    0.6493837702986368,
                    0.6454310256268904,
                    0.7085305859966166,
                    0.7709963397003181,
                    0.7628122486461532,
                    0.7260869667056613,
                    0.7656074896314918,
                    0.7309944223135776,
                    0.7575162043117213,
                    0.7425954755181217,
                    0.7978452334414571,
                    0.7414129597626153,
                    0.7369987033441427,
                    0.7249664966482501,
                    0.663939118162477,
                    0.7490232329485363,
                    0.7532303509685747,
                    0.6505502824396713,
                    0.6820403873171862,
                    0.7458589415356044,
                    0.65106761846338,
                    0.8190794585362886,
                    0.6404595320063431,
                    0.7620011212588133,
                    0.6793344580417779,
                    0.7470455239529016,
                    0.6254743025101126,
                    0.714021296346165,
                    0.7624376857959331,
                    0.6124088443110871,
                    0.7190909082546953,
                    0.7667977482791689,
                    0.7390282391537781,
                    0.731411776312689,
                    0.6910654011387792,
                    0.7669731150300952,
                    0.7473599833172766,
                    0.7757742306046117,
                    0.7524096654164605,
                    0.668078105815945,
                    0.6797298899209671,
                    0.734572374544983,
                    0.7851097143298676,
                    0.7342031538272321,
                    0.7372538892798539,
                    0.7335209046034747,
                    0.6838366965805461,
                    0.6892908218001774,
                    0.7368799079039347,
                    0.667817778038092,
                    0.7436021083467266,
                    0.643687287978847,
                    0.6459012534104801,
                    0.717961524900317,
                    0.651811280493696,
                    0.774663511332172,
                    0.6481450536649574,
                    0.7135017154296592,
                    0.718243043672562,
                    0.6840974559559992,
                    0.6237039667424505,
                    0.7511301324631847,
                    0.6731554748777204,
                    0.7311433676647258,
                    0.7407740108803432,
                    0.7219713524118947,
                    0.6945284597258313,
                    0.7403964086997485,
                    0.7281416758951161,
                    0.767616849591671,
                    0.7623013461443361,
                    0.794278871148869,
                    0.7094595086377886,
                    0.6363511838820268,
                    0.6955392554405656,
                    0.7448982185809608,
                    0.7328610107493276,
                    0.7208624134565648,
                    0.6762963031433926,
                    0.7755406771546928,
                    0.7045876515082797,
                    0.6244682388287953,
                    0.6742169930443296,
                    0.8182351707309709,
                    0.7329206562104693,
                    0.7750198586773644,
                    0.7686712995024062,
                    0.7382706738683358,
                    0.6670365140953741,
                    0.7122098843228497,
                    0.720363344417827,
                    0.7260325476617868,
                    0.7455849615803621,
                    0.7135971488970759,
                    0.7597698332957011,
                    0.7261113201174606,
                    0.7802411718313292,
                    0.6937507195359754,
                    0.7842882648198792,
                    0.6900501446041246,
                    0.760860218311663,
                    0.7134088358525988,
                    0.7053629634417926
                  ],
                  "xaxis": "x2",
                  "yaxis": "y2"
                },
                {
                  "alignmentgroup": "True",
                  "bingroup": "x",
                  "hovertemplate": "label=-1<br>dataset=test<br>cosine_similarity=%{x}<br>count=%{y}<extra></extra>",
                  "legendgroup": "-1",
                  "marker": {
                    "color": "#EF553B",
                    "opacity": 0.5,
                    "pattern": {
                      "shape": ""
                    }
                  },
                  "name": "-1",
                  "offsetgroup": "-1",
                  "orientation": "v",
                  "showlegend": false,
                  "type": "histogram",
                  "x": [
                    0.698216609902851,
                    0.7175312484264973,
                    0.7186004945024,
                    0.8000305631283213,
                    0.6982596730429885,
                    0.7632305498724974,
                    0.7138465594512551,
                    0.6788567152998355,
                    0.7373203069430523,
                    0.6873036529619025,
                    0.6503465541274354,
                    0.7365009792588864,
                    0.741093678604772,
                    0.735107851927508,
                    0.7789882788330387,
                    0.6997359150722298,
                    0.7996799028712657,
                    0.7467428244049107,
                    0.6687862526227949,
                    0.743064589979991,
                    0.8567601871608912,
                    0.7518934598338161,
                    0.7026922402796603,
                    0.7211365080382613,
                    0.706354045904417,
                    0.779427003097291,
                    0.7362962393365906,
                    0.7291751132805836,
                    0.7122378769301289,
                    0.7140477948952889,
                    0.7173405960056081,
                    0.7634875929311733,
                    0.7977581390590794,
                    0.7301463738402032,
                    0.7615332057968679,
                    0.682227985030492,
                    0.7334635989895589,
                    0.7386028577038499,
                    0.659084291835728,
                    0.7899820114980755,
                    0.7247172517704278,
                    0.7438155210487466,
                    0.7005346860296618,
                    0.6648553956533266,
                    0.7701566644966253,
                    0.7514961574415904,
                    0.7587991656983686,
                    0.7001882273133521,
                    0.6910707516646375,
                    0.7394355361240693,
                    0.7276824899179835,
                    0.6759744362016779,
                    0.8302185470787163,
                    0.6928641094502374,
                    0.7120538723839331,
                    0.7224960785372221,
                    0.7198045816069757,
                    0.6813558762031737,
                    0.7165801628045559,
                    0.7120832723046919,
                    0.8420619371167495,
                    0.946387336435492,
                    0.7554566849916029,
                    0.6539169025880401,
                    0.7809846972343978,
                    0.7724403150471626,
                    0.7005276086814838,
                    0.6393757830582598,
                    0.8206678516495857,
                    0.7220887623700465,
                    0.6457268309147112,
                    0.7355556783165726,
                    0.7154485704709247,
                    0.736485552747626,
                    0.6279868336962336,
                    0.6826307018159569,
                    0.6893086023402188,
                    0.6662701662224271,
                    0.7867533724923507,
                    0.7767747518359883,
                    0.8265509786609969,
                    0.7191298707058883,
                    0.7022356632617615,
                    0.7327905404619434,
                    0.744068997548466,
                    0.7610196098150734,
                    0.7115456073990181,
                    0.7432332956176703,
                    0.7893785433034154,
                    0.7290401089931655,
                    0.6577253300110991,
                    0.7003577024217508,
                    0.6656632326716906,
                    0.777774068734494,
                    0.7332058736487923,
                    0.6832255453323396,
                    0.7959026283113317,
                    0.7447573588360193,
                    0.6641622569109379,
                    0.6536973982676278,
                    0.6665423422110455,
                    0.6839542281076658,
                    0.7423443203765382,
                    0.7548386221527327,
                    0.6027110439271006,
                    0.6910860362919979,
                    0.6562817652314046,
                    0.716178983425107,
                    0.724403115068019,
                    0.7259909803954812,
                    0.7571530348849562,
                    0.733442357026098,
                    0.7422263713152575,
                    0.7194490356714829,
                    0.8324274302968815,
                    0.7326854438693811,
                    0.6965534375434462,
                    0.6112368704742529,
                    0.7304384905441154,
                    0.7720040972080942,
                    0.6935032899149339,
                    0.6744196671055273,
                    0.7147585872166342,
                    0.7752945283086001,
                    0.7247252468203336,
                    0.7487128692844189,
                    0.7073695766484023,
                    0.7770002807438351,
                    0.6765039364068596,
                    0.6337555851438214,
                    0.7894145395726685,
                    0.808127657824718,
                    0.6806212157836168,
                    0.6631556694778886,
                    0.7026864982467919,
                    0.6616453779258454,
                    0.7884566439105933,
                    0.7066759939380831,
                    0.6337579382878964,
                    0.6487574469000645,
                    0.772145520185077,
                    0.7232462166936153,
                    0.7901145921506159,
                    0.6972515066616096,
                    0.7122390390469722,
                    0.7192738985202007,
                    0.6592857746430886,
                    0.7609468966795828,
                    0.6603956483288737,
                    0.7457664593808938,
                    0.6826889303879785,
                    0.7934081087742163,
                    0.6763383894378445,
                    0.6839731303810913,
                    0.6687692061586001,
                    0.6991702352595418,
                    0.7797875942740597,
                    0.7663428993137384,
                    0.7674609664886143,
                    0.7252797254797089,
                    0.6976652869077468,
                    0.7158816756428659,
                    0.718241456712601,
                    0.7632800029357677,
                    0.7220393239650442,
                    0.7734594213360495,
                    0.6831354341128338,
                    0.8050740585092945,
                    0.8304016729411579,
                    0.6942297180429666,
                    0.7777210539532041,
                    0.7971492766742209,
                    0.7551377672686813,
                    0.756111346085797,
                    0.7377139073001521,
                    0.7292914327831885,
                    0.6619852966467218,
                    0.6633387313486273,
                    0.7753943622795527,
                    0.6931366760284077,
                    0.6879938635549627,
                    0.7934277451864097,
                    0.7095961561996172,
                    0.6721647904665006,
                    0.6639348167332335,
                    0.7190874751718003,
                    0.6487682662731885,
                    0.7712237228183192,
                    0.7195541308325332,
                    0.7624245070018526,
                    0.7066568592895756,
                    0.6955819267956074,
                    0.762644689565747,
                    0.696550099953965,
                    0.72160309057877,
                    0.6589853583691466,
                    0.7781076723886485,
                    0.7844353288099747,
                    0.6499942545071061,
                    0.7586643115109818,
                    0.7851245713510661,
                    0.6825431110733673,
                    0.7920473550917971,
                    0.7505505200683399,
                    0.7112992195413225,
                    0.6872424297540068,
                    0.6629403755138552,
                    0.7754417757832819,
                    0.7445419843378304,
                    0.7064660255551196,
                    0.7102764764345906,
                    0.7166584523700176,
                    0.745706231193076,
                    0.7628022956052315,
                    0.6960882904963708,
                    0.6837468719098787,
                    0.7520487263229376,
                    0.7604129787986132,
                    0.7522054011542562,
                    0.6898973175025894,
                    0.712053903439596,
                    0.7339122116041967,
                    0.6789458999380491,
                    0.763449576758855,
                    0.7406926320689465,
                    0.6976029213628422,
                    0.7734670110437211,
                    0.7670042286239444,
                    0.7194794729796166,
                    0.8039337600845294,
                    0.822887238017454,
                    0.7546355748553022,
                    0.712175872919759,
                    0.6283408438534046,
                    0.7277722488820856,
                    0.7848289730316366,
                    0.6470175548703326,
                    0.7175970646556328,
                    0.6982508276209234,
                    0.6931585425755658,
                    0.7105706262503181,
                    0.6541269887120206,
                    0.8404400660965669,
                    0.7278163563567496,
                    0.8022018950050529,
                    0.7449136144274442,
                    0.7254549036563473,
                    0.7708530061010334,
                    0.7226568414320923,
                    0.7174427406313559,
                    0.7242867487973796,
                    0.7465548093208114,
                    0.6481248100208876,
                    0.715420475795481,
                    0.7818995378198694,
                    0.710140386310007,
                    0.779070581516581,
                    0.7022765286826387,
                    0.7920014977874291,
                    0.7028249663680173,
                    0.7464011128583546,
                    0.6874796697586977,
                    0.7834259382246206,
                    0.7487992683674399,
                    0.6256280566008573,
                    0.7248416704075088,
                    0.6787298488859722,
                    0.7604099689852636,
                    0.7563309422531382,
                    0.6536692254847523,
                    0.7277402265583088,
                    0.7961681595257355,
                    0.7183023940359037,
                    0.8578324194628058,
                    0.6890352710148969,
                    0.711616174722821,
                    0.6560825239577808,
                    0.7235723022023411,
                    0.6649236563739442,
                    0.6800589793852263,
                    0.7785177771732936,
                    0.8277144895457349,
                    0.7047472917613488,
                    0.6981993581133783,
                    0.69214194925211,
                    0.7175225477364914,
                    0.6821700037384272,
                    0.6934882153010823,
                    0.6671459724713757,
                    0.7577056235720239,
                    0.7452347481085622,
                    0.7540647847248615,
                    0.7623045528688165,
                    0.8419961516314336,
                    0.7607631404114222,
                    0.7104592749279437,
                    0.7907219223857475,
                    0.6626370861321504,
                    0.7293323972767943,
                    0.6747790790615374,
                    0.7205393564241827,
                    0.7182141925188444,
                    0.6698620455142402,
                    0.7774615433926413,
                    0.68441903533162,
                    0.7195176784475413,
                    0.7765542578440102,
                    0.7653003235671018,
                    0.6588957811563716,
                    0.7049538466814345,
                    0.6767019827253833,
                    0.6852115350974048,
                    0.7159808946533304,
                    0.6275008181698795,
                    0.6641598464064111,
                    0.7653064009797307,
                    0.7846062245731015,
                    0.7131195190890488,
                    0.7388407888274415,
                    0.7078575690975646,
                    0.7922969773693673,
                    0.6399205949452071,
                    0.7522331808600956,
                    0.756127025845852,
                    0.7527950868321375,
                    0.7791392496558245,
                    0.7388745760013306,
                    0.6739605493576779,
                    0.6432673241279167,
                    0.7124181751534668,
                    0.669456709871883,
                    0.7067049471522552,
                    0.6685698115209102,
                    0.7430777123010961,
                    0.7510627360284545
                  ],
                  "xaxis": "x",
                  "yaxis": "y"
                }
              ],
              "layout": {
                "annotations": [
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "dataset=test",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.2425,
                    "yanchor": "middle",
                    "yref": "paper"
                  },
                  {
                    "font": {},
                    "showarrow": false,
                    "text": "dataset=train",
                    "textangle": 90,
                    "x": 0.98,
                    "xanchor": "left",
                    "xref": "paper",
                    "y": 0.7575000000000001,
                    "yanchor": "middle",
                    "yref": "paper"
                  }
                ],
                "barmode": "overlay",
                "legend": {
                  "title": {
                    "text": "label"
                  },
                  "tracegroupgap": 0
                },
                "margin": {
                  "t": 60
                },
                "template": {
                  "data": {
                    "bar": [
                      {
                        "error_x": {
                          "color": "#2a3f5f"
                        },
                        "error_y": {
                          "color": "#2a3f5f"
                        },
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "bar"
                      }
                    ],
                    "barpolar": [
                      {
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          },
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "barpolar"
                      }
                    ],
                    "carpet": [
                      {
                        "aaxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "baxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "type": "carpet"
                      }
                    ],
                    "choropleth": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "choropleth"
                      }
                    ],
                    "contour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "contour"
                      }
                    ],
                    "contourcarpet": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "contourcarpet"
                      }
                    ],
                    "heatmap": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmap"
                      }
                    ],
                    "heatmapgl": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmapgl"
                      }
                    ],
                    "histogram": [
                      {
                        "marker": {
                          "pattern": {
                            "fillmode": "overlay",
                            "size": 10,
                            "solidity": 0.2
                          }
                        },
                        "type": "histogram"
                      }
                    ],
                    "histogram2d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2d"
                      }
                    ],
                    "histogram2dcontour": [
                      {

... (truncated 3022 lines) ...
```

**Note**: Source truncated for display. Full file is 13022 lines.

## High-Level Overview

Jupyter Notebook containing interactive code cells and documentation.

## Detailed Analysis

File contains 13022 lines with structured content.

## Usage & Examples

Open in Jupyter:

```bash
jupyter notebook Customizing_embeddings.ipynb
```

## Performance & Security Notes

📊 **Performance**: Contains nested loops - consider complexity
📊 **Performance**: Large file - may impact load times

## Related Files

**Same directory**:
- [Assistants_API_overview_python.ipynb](./Assistants_API_overview_python.ipynb_docs.md)
- [Build_a_coding_agent_with_GPT-5.1.ipynb](./Build_a_coding_agent_with_GPT-5.1.ipynb_docs.md)
- [Chat_finetuning_data_prep.ipynb](./Chat_finetuning_data_prep.ipynb_docs.md)
- [Classification_using_embeddings.ipynb](./Classification_using_embeddings.ipynb_docs.md)
- [Clustering.ipynb](./Clustering.ipynb_docs.md)
- [Clustering_for_transaction_classification.ipynb](./Clustering_for_transaction_classification.ipynb_docs.md)
- [Code_search_using_embeddings.ipynb](./Code_search_using_embeddings.ipynb_docs.md)
- [Context_summarization_with_realtime_api.ipynb](./Context_summarization_with_realtime_api.ipynb_docs.md)
- [Creating_slides_with_Assistants_API_and_DALL-E3.ipynb](./Creating_slides_with_Assistants_API_and_DALL-E3.ipynb_docs.md)
- [Custom-LLM-as-a-Judge.ipynb](./Custom-LLM-as-a-Judge.ipynb_docs.md)

**Imported modules**:
- `List`
- `a`
- `dataframe`
- `different`
- `get_embedding`
- `numpy`
- `pandas`
- `pickle`
- `plotly.express`
- `random`
- `sentences`
- `sklearn.model_selection`
- `texts`
- `the`
- `torch`

## Testing & Execution

Execute cells sequentially in Jupyter environment.

---
*Generated by Repo Book Generator v1.0.0*

# BacDive AI models

This is a small command line tool bundled with selected BacDive-AI models to predict bacterial phenotypes from InterPro annotations.


This package comes with an example InterPro annotation of the strain [*Actinomyces dentalis* DSM 19115](https://bacdive.dsmz.de/strain/189). The annotated file in TSV format is named as `1120941.3.faa.tsv`. The genome is derived from [BV-BRC](https://www.bv-brc.org/view/Genome/1120941.3) (formerly PATRIC).

For reference, the used command to generate the Pfams with [InterProScan](https://interproscan-docs.readthedocs.io/en/latest/) was:
```bash
interproscan.sh -i 1120941.3.faa -f tsv -d ./ -appl Pfam
```

To start the prediction of a single trait, you can use the following example code in the project folder:

```bash
python predict.py gram-positive 1120941.3.faa.tsv
```

For the aforementioned call, you can select one of the following values:

| Value           | Trait              |
| --------------- | ------------------ |
| gram-positive   | Gram-positive      |
| spore-forming   | Spore-forming      |
| aerobic         | Aerobic            |
| anaerobic       | Anaerobic          |
| thermophile     | Thermophilic       |
| halophile       | Halophilic         |
| motile          | Motile             |
| flagellated     | Flagellated        |
| glucose-util    | Glucose-utilizing  |
| glucose-ferment | Glucose-fermenting |


You can also choose `all` to see the complete list of predicted values:

```bash
python predict.py all 1120941.3.faa.tsv
```

You will get the prediction (true or false) for each of the trait together with a confidence score. The output should look like this:

```
gram-positive: True (98.63%)
spore-forming: False (96.82%)
aerobic: False (98.6%)
anaerobic: True (73.14%)
thermophile: False (98.87%)
halophile: False (80.14%)
motile: False (91.49%)
flagellated: False (96.85%)
glucose-util: True (91.09%)
glucose-ferment: True (90.49%)
```


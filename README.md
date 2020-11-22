# Classification algorithm for Congenital Zika Syndrome: characterizations, diagnosis and validation

## Table of contents
* [General info](#general-info)
* [Compilation](#compilation)
* [Input data](#Input-data)
* [Files](#files)
* [References](#references)

## General info
In this directory, we present the code to construct a Classification algorithm for Congenital Zika Syndrome (CZS)

The code originated from the project described in the paper [1]. The purpose of this algorithm is to be able to identify cases of CZS automatically based on electronic records, serogy and imaging reports.

## Compilation
We performed our statistical analysis using Python version 3.6.5.  We computer classification evaluation using Jupyter Notebook.
Necessary packages:
* [scikit-learn](https://scikit-learn.org)
* [matplotlib](https://matplotlib.org)
* [spacy](https://spacy.io)

## Input data

we use the Brazilian electronic records [RESP (Public Health Event Record)](http://www.resp.saude.gov.br) linked with [SINASC (Live Birth Information System)](sinasc.saude.gov.br).
We use results obtained by the classification performed by a group of specialists described in the article [2] for training.

Data from cranial circonferencing standards according to gender and week of development was obtained from [InterGrowth standards](https://intergrowth21.tghn.org)

## Files
 * circumference.csv : Data from cranial circonferencing standards.
 * gerateData_RuleClass.py : this script organize database and applied rule classification.
 * classifier_1.py: this script create a classify for group 1
 * classifier_2.py: this script create a classify for group 2
 * runClass1.py: this script performs group 1 classification
 * runClass2.py: this script performs group 2 classification
 * evaliation.ipynb : this script contains the analyses performed for the article

## References 
[1] Classification algorithm for Congenital Zika Syndrome: characterizations, diagnosis and validation. (submited to Scientific Reports)

[2] França, Giovanny VA, et al. "Congenital Zika virus syndrome in Brazil: a case series of the first 1501 livebirths with complete investigation." The lancet 388.10047 (2016): 891-897.

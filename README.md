# Classification algorithm of Congenital Zika Syndrome: characterizations, diagnosis and validation

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

we use the Brazilian electronic records {RESP (Public Health Event Record)](http://www.resp.saude.gov.br) linked with [SINASC (Live Birth Information System)](sinasc.saude.gov.br).
We use results obtained by the classification performed by a group of specialists described in the article [2] for training.

## Files

To perform the study of time series analyses we collected the confirmed and discarded reported cases of each arbovirus per epidemiological week in Brazil, from 2015 to 2017.

## References 
[1] Classification algorithm of Congenital Zika Syndrome: characterizations, diagnosis and validation. (submited to Scientific Reports)

[2] 

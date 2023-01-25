# House price prediction in Lyon

## Overview

This is a house price prediction app that uses a Random Forest Regressor to the predict the price of houses in the French city of Lyon. The model was trained on a dataset of 44000+ properties from ["Demandes de valeurs foncières géolocalisées](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/) and has a r2 score of 0.7029.

![overview of the app](./images/overview.PNG)

## Install & Run

1. Clone the repository
```sh
git clone https://github.com/MiTiX1/house-price-prediction.git
```
2. Install the required packages
```sh
pip install -r requirements.txt
```
3. Run
```sh
streamlit run main.py
```

## LICENSE

MIT License

Copyright (c) 2023 Bastien Boulet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

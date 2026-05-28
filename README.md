# Sona Power Predict – 2026

## College Name

Knowledge Institute Of Technology

## Team Name

TriLogic

---

## Team Members

| Name     | Year     | Department |
| -------- | -------- | ---------- |
| Jeeva P | 2nd Year | CSE        |
| Mouneesh S | 2nd Year | CSE        |
| Mohammed Hasith K | 2nd Year | CSE        |
| Inbhatamizhan V | 2nd Year | CSE        |

---

## Libraries Used

* pandas

---

## Project Overview

This project focuses on predicting IPL powerplay scores using a feature-engineered prediction model.

The model estimates first six over scores by combining:

* Venue scoring conditions
* Batting aggression ratings
* Bowling strength
* Innings and dew impact
* Match context

The solution is implemented using Python and pandas.

---

## Methodology

### 1. Venue Intelligence

Different stadium aliases are mapped correctly to identify scoring environments such as:

* Wankhede
* Chinnaswamy
* Eden Gardens
* Ekana
* Mohali
* Ahmedabad
* Chennai

### 2. Batting Intent Modeling

Teams are assigned attack ratings based on recent powerplay scoring patterns.

### 3. Bowling Strength Analysis

Bowling pressure ratings are used to estimate scoring difficulty during powerplays.

### 4. Innings & Dew Effect

Second innings predictions include dew-based adjustments on batting-friendly venues.

### 5. Prediction Normalization

Predictions are normalized within realistic IPL powerplay score ranges to reduce extreme outputs.

---

## Model Type

Feature-Engineered Predictive Model

---

## Output

The model generates predicted IPL powerplay scores for match inputs provided through CSV files.


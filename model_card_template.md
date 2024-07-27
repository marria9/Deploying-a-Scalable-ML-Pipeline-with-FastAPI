# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This Model was created by Mario Arriaga on July 26, 2024. It utilizes the LogisticRegression Model from the Scikit-Learn library.
This is part of a Machine Learning DevOps Project for the Udacity Nanodegree Program.

## Intended Use
The goal of this model was to aid in predicting the probability of individuals who earn over $50k annually based on information learned from past U.S. Census data

## Training Data
The training data was composed of 80% of the US Census Data that was preprocessed with one-hot encoding of the categorical features as well as binarization of the labels.

## Evaluation Data
The evaluation data was composed of the remaining 20% of the US Census Data that was not used for training. This portion also went through the same preprocessing steps as the training data which included one-hot encoding of the categorical features as well as binarization of the labels.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The following metrics were used: Precision: 0.7285 | Recall: 0.2699 | F1: 0.3939. Additional metrics for each individual slice are contained in the slice_output.txt file.

## Ethical Considerations
The US Census dataset does contain values for Gender and Race which if not handled properly could lead to biases forming. Any user of the model should be aware of this to ensure that care is taken when using the model not to improperly empose bias on specific genders and/or races not able to make over $50k annually just on those factors.

## Caveats and Recommendations
The US Census dataset utilized is from a past year and not from the current year. This means as changes in the value of money occur with circumstances just as inflation, the model not always determine current individuals who are making over 50k annually today.

For that reason, it is recommended to continually to train and evaluate on the latest US Census data that is available throughout the years.
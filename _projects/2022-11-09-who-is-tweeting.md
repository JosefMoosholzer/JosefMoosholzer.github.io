---
title: 'Trump or Biden: Who is tweeting?'
subtitle: 'with Python: gensim, scikit-learn and matplotlib.'
date: 2022-11-09 00:00:00
description: I used Natural Language Processing to train a model to differentiate between Donald J. Trump and Joe Biden tweets. Various models were used to see which fits the best.
featured_image: /images/WhoIsTweeting/Trump_vs_Biden.png
---
# An NLP analysis on the tweets by the two major candidates of the 46th presidential election in the U.S.
## Preparation
Before starting this project I had some rough knowledge on the concept of bag-of-words for the vectorization of text-documents, as I had to reconstruct Google's algorithm on identifying article-simlarity for one of my courses in my Information Systems program. In that course I also learned about tf-idf (term frequency, inverse document frequency), which is a model where each word is given a weight that increases with the frequency of that word in that specific text (tweet) but decreases in importance if that word is encountered in most texts. Hence, overall rare words, though frequently present in a specific text characterize that text the most.

The concept of NLP was, however, fairly new to me. So I took an <a href='https://app.datacamp.com/learn/courses/introduction-to-natural-language-processing-in-python'>introductory course</a> in Datacamp.

## Data Extraction
For everyone living under a rock, Donald J. Trump was suspended from Twitter following the election results. His last tweet dates back to the 8th of January 2021. Luckily, there is a website called <a href="https://www.thetrumparchive.com/">The Trump Archive</a> where I was able to download all tweets.

For Joe Biden, I found a dataset on <a href="https://www.kaggle.com/datasets/rohanrao/joe-biden-tweets?resource=download">Kaggle</a>. However, they did not include tweets from November 2020 onwards. Hence, I accessed the Twitter-API, which luckily gave me tweets reaching further back, than the other dataset's last entry. On my [*GitHub*](https://github.com/JosefMoosholzer/JosefMoosholzer.github.io/blob/main/downloads/IndeedScraper.py) you can see the code created in order to retrieve the tweets from the Twitter-API.

## Transformation & loading
The full transformation can be seen in the [DeepNote project](https://deepnote.com/@my-projects-jm/Biden-vs-Trump-Who-tweeted-6acfb9ee-5808-4be9-af50-2e63ffd088a4).
As a quick summary, Joe Biden's tweets had to be checked for duplicates, but both datasets included the Tweet-ID, so that was no problem. Tweets only including a Twitter link were removed, and Twitter links were removed in general.
Both datasets were then labelled before being appended.
For the upcoming NLP, I trimmed the dataset to the timespan where both were active (Biden restarted tweeting in 2018) and then took a sample of Trump's tweets to match the amount of Biden's. I did this so that the model was not overfitting for Trump, which would sacrifice the performance for the classification of Biden's tweets.

## Vectorization and fitting
As mentioned before, a tf-idf vectorization might be a good approach for NLP. However, tweets can follow their own rules of grammar and structure, as there is a limit to the number of characters used, thus, consisting mostly of key words. Therefore, a classic count vector might be just as good in this case.

In NLP it is also common to exclude stop words that do not give any insight on the texts topic. However, as we only have two different authors which supposedly should address the same topics in public, it might be possible that differentiating the tweets according to key words might turn out to be quite difficult. On the other hand, there could be a significant difference in the use of the English language between the two, see <a href="https://tiffanymarkman.medium.com/an-analysis-of-president-donald-trumps-use-of-language-74a76c3d062b">here</a>. For that reason, I also used a simple count vectorization to compare it to the tf-idf vectorization.

## Models
For the models I took a Naive Bayes approach to see which vectorization is the most appropriate and a Linear Support Vector Classifier to later graph the key words that are the most related to each U.S. President.

## Results
| descriptive statistic | tf-idf | tf-idf no stop words | count |
| --------------------- | ------ | -------------------- | ----- |
| Mean                  | 0.7746 | 0.6808 | 0.7746 |
| Std                   | 0.01   | 0.036  | 0.01   |
| Min                   | 0.7548 | 0.6307 | 0.7457 |
| 25-percentile         | 0.7669 | 0.6443 | 0.7669 |
| Median                | 0.7749 | 0.7024 | 0.7744 |
| 75-percentile         | 0.7832 | 0.7137 | 0.7823 |
| Max                   | 0.8002 | 0.7302 | 0.7937 |

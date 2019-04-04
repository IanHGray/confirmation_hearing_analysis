# confirmation_hearing_analysis
Text analysis repository designed to work with the R Street Institute's "Confirmation Hearings" dataset.

The current script pre-processes the raw text data from the "Statements" column, then calculates and plots the most frequently occurring words for a given hearing. Specific speakers (such as a Senator or the nominee themselves) can be optionally selected.

This analysis is *very* basic, but should serve as a solid starting point for this dataset. An important next step would be to determine stopwords (or junk words that adds no value to the analysis) that are specific to these types of hearings. I've added "confirmation_hearing_stopwords.py" as a repository for these terms. 

Kudos to the RSI team for putting this data together!

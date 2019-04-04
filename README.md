# confirmation_hearing_analysis
Text analysis repository designed to work with the R Street Institute's "Confirmation Hearings" dataset.

The current script pre-processes the raw text data from the "Statements" column, then calculates and plots the most frequently occurring words for a given hearing. Specific speakers (such as a Senator or the nominee themselves) can be optionally selected.

This analysis is *very* basic, but should serve as a solid starting point for this dataset. Some key next steps:

   Identify stopwords (or junk terms that add no analytical value) that are specific to these types of hearings. I've added              "confirmation_hearing_stopwords.py" as a repository for these terms.

   Named Entity Recognition: Programatically identify key people, organizations, or concepts that are being discussed during       the hearings, and track how they change over time, how they are treated by the two parties, etc.

  Sentiment analysis: What is the tone associated with each hearing? Can we identify any long term trends here? 
  
  Cluster Analysis: What are the key points, from a statistical standpoint, in each hearing? What subjects have the greatest weight?

If you have any thoughts or ideas, please email me at gray.ian.hunter@gmail.com.

Kudos to the RSI team for putting this data together!

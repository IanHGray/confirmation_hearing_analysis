# confirmation_hearing_analysis
Text analysis repository designed to work with the R Street Institute's "Confirmation Hearings" dataset. A link to this data can be found here: https://www.rstreet.org/2019/04/04/supreme-court-confirmation-hearing-transcripts-as-data/

This repository includes a Jupyter notebook ("hearing_analysis.ipynb") that serves as a starting point for pre-processing the data and performing some summary-level analysis of the text. This includes word count over time by party, sentiment over time by party, word count over time by hearing role, most verbose senators per hearing, and a wordcloud generator for a given senator in a given hearing.

A second notebook ("confirmation_hearing_entities.ipynb") dives into some more advanced analysis, utilizing Named Entity Recognition to extract key topics, people, and organizations from the hearings. This could serve as a useful starting point for research projects, particularly those concerned with how different issues evolve in importance over time.

A key next step for this dataset would be to develop a more tailored and robust list of stopwords (or junk words that provide no analytical value) that is specific to the confirmation hearing process. Additionally, it might be interesting to perform a network analysis of named entities to determine which Senators discuss which subjects in what context.

If you have any thoughts or ideas, please email me at gray.ian.hunter@gmail.com.

Kudos to the RSI team for putting this data together!

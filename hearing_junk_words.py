"""The following words are being removed from the analysis, as they
are both numerous and obvious, providing no additional insight.
This specific set of stopwords is geared towards the Gorsuch hearing."""

hearing_junk_words = [
'america', 'american', 'americans', 'laughter',\
'obama', 'trump', 'gorsuch', 'graham', 'grassley',\
'democrat', 'democrats', 'democratic', 'republican',\
'republicans', 'casey', 'mr', 'scalia', 'president', \
'constitution', 'bush', 'mrs', 'ginsburg', 'donald trump',\
'donald', 'Roberts', 'Alito', 'john roberts', 'samuel alito',\
'clinton', 'reagan', 'nixon', 'nation', 'government', 'kagan',\
'justice', 'committee', 'hearing', 'senate', 'state', 'court',\
 'supreme court', 'congress', 'steven breyer', 'breyer', 'o\' connor',\
 'rehnqist', 'supreme', 'department', 'agency', 'federal', 'bork',\
 'thank', 'house', 'MS', 'U S']
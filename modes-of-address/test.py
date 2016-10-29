import nltk
#nltk.download()

from nltk.book import *

##A concordance permits us to see words in context.
##Similar will help determine what other words appear in a similar range of common_contexts
##The term common_contexts allows us to examine just the contexts that are shared by two or more words.

#print("--concordance")
#text1.concordance("monstrous")
#print("--similar")
#text1.similar("monstrous")
#print("--context")
#text2.common_contexts(["monstrous", "very"])

## Creates a plot that determines when text are used within a text

#import matplotlib
#from nltk.draw.dispersion import dispersion_plot
#dispersion_plot(text4, ["citizens", "democracy"])

## Determine the frequency of words within a text
#fdist = FreqDist(text1)
#print(fdist.most_common(50))

##A collocation is a sequence of words that uccur together unusually often.
##Thus red wine is a collocation, where as the wine is not.
text4.collocations()

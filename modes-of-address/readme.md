# Modes of address
This folder gathers the first steps in a project that aims to analyse the use of different modes of address across software tools and how they influence the access knowledge necessary for the tool, and access to boundary knowledge.

## Project one liner:

Research project to take account and analyse the *modes of address* used in software to understand how and which ones enable user *individuation*.

#### Fast definitions:

* modes of address / addressing mode / manor of address: the way in which we address another, the way in which we are addressed by others or their intermediaries.

* individuation: (drawing from Stiegler, who draws from Simondon) The capactity that I have to individuate myself, to become more individual, to develop my own skills.

* parts of speech: categorisation of language into it's gramatical functions: nouns, verbs, adverbs, etc

(## Calling it the 4th wall?)

## first prototype

The first step I took towards gaining understanding of what modes of address are used in software was a litteral one.

I took the language translation files from Inkscape, (type of file that lets a software be recompiled in different languages, while being developped in one core one) and isolated the english text. Processing english in NLTK had many options to explore but my initial interest is semantic, so I took a look at *parts of speech*. This function basically outputs the source text back in a counted list of all the different parts of speech that the (trained library) toolkit knows about.

To make sense of this list, I had to see what the function would do on a different type of text, one that I knew had a different mode of address, but also in the realm of using a tool; I used the vimtutor text second. Much more of a tutorial attitude, different type of program.

I list the results in [compare_results.html](compare_results.html)

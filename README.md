# peptidr - Predicting Signal Peptides
As part of this project for the course Applied Bioinformatics (DD2404) at KTH Royal Institute of Technology, we investigate several Machine Learning techniques to build a peptide signal classifier using python based scikit-learn library.

In this project, we implement various algorithms to classify which protein sequences start with signal peptide sequence and find that random forest classifier works the best amongst the contemporary classification algorithms with an classification
accuracy of 86% on validation dataset including both transmembrane and non-transmembrane sequences. Further, the trained classifier is tested on two BioMart datasets of human and mouse proteomes for signal peptide prediction.In Homo Sapiens(human), proteome sequences 48% were predicted to have signal peptides and in Mus(mouse) sequences 44% were predicted to have signal peptides. According to [1] 15% of all proteins in a genenome contain a signal peptide and [2] suggests about 20000 proteins in the human proteome have signal peptides this seems to imply that our classifiers are biased upwards. We believe this is because of the bias in the training data used.

[1] http://www.computersinbiologyandmedicine.com/article/S0010-4825(13)00346-6/pdf
[2] http://www.proteinatlas.org/humanproteome/secretome

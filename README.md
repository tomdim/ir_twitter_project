# Sentiment Analysis - twitter

Η εργασία είναι υλοποιημένη στη γλώσσα **Python 2.7**.

## Αρχεία
>• Αρχεία εκτελέσιμου κώδικα (.py)
>>    1. **config.py**: αρχείο κωδικών για το Twitter oAuth και για τη Βάση Δεδομένων – οι κωδικοί δεν είναι μέσα στο αρχείο.
>>    2. **stemming.py**: κώδικας του Αλέξανδρου Καλαπόδη για το stemming των ελληνικών λέξεων.
>>    3. **GetTweets.py**: κώδικας για την λήψη των Tweets.
>>    4. **ClassifyTweets.py**: κώδικας για την κατηγοριοποίηση των tweets σε θετικά, αρνητικά ή ουδέτερα.
>>    5. **DataVisualization.py**: κώδικας για την οπτικοποίηση των αποτελεσμάτων της κατηγοριοποίησης – αποτελέσματα εβδομάδας.
>>    6. **Analysis.py**: κώδικας για p-nearest terms.
    
>• Αρχεία excel (.xls, .xlsx)
>>    1. **PosLex.xls**: λεξικό θετικών όρων.
>>    2. **NegLex.xls**: λεξικό αρνητικών όρων.
>>    3. **results.xlsx**: αρχείο αποθήκευσης αποτελεσμάτων κατηγοριοποίησης και χρησιμοποιείται για την οπτικοποίηση των αποτελεσμάτων (αρχείο 5 αρχείων εκτελέσιμου κώδικα).
    
>• Φάκελοι και αρχεία .txt
>>    1. **greekstopwords.txt**: χρησιμοποιείται στην διαδικασία προεπεξεργασίας των κειμένων-tweets.
>>    2. **Φάκελος tweets**: περιέχει τους υποφακέλους TweetsMitsotakis, TweetsNeaDimokratia, TweetsSyriza, TweetsTsipras, οι οποίοι υποφάκελοι περιέχουν τα txt αρχεία με τα tweets(clean text) για κάθε αντίστοιχη ημέρα συλλογής τους.
>>    3. **Φάκελος results_week1**: τα οπτικοποιημένα αποτελέσματα της 1ης εβδομάδας για την κάθε κατηγορία tweets σε φωτογραφίες και ένα αρχείο txt με τα tweets όλων των κατηγοριών που συλλέχθηκαν την 1η εβδομάδα για τα μέρη 6-9 της εκφώνησης.
>>    4. **Φάκελος results_week2**: αντίστοιχα πράγματα με τον φάκελο results_week1 αλλά για την 2η εβδομάδα.
>>    5. **Φάκελος ext1**: περιέχει τους υποφακέλους 1, 2, 4, 5, 10 (p nearest terms, όπου p = {1, 2, 4, 5, 10}), οι οποίοι περιέχουν αρχεία txt με τα ExtPos(ti) και τα ExtNeg(ti), όπως αναφέρει το μέρος 6 της εκφώνησης, για τα tweets της 1ης εβδομάδας.
>>    6. **Φάκελος ext2**: αντίστοιχα πράγματα με τον φάκελο ext1 αλλά για τα tweets της 2ης εβδομάδας.


## Χρονικό διάστημα συλλογής tweets
>Έχει γίνει συλλογή tweets για 15 ημέρες (2 ολόκληρες εβδομάδες) από 2017-01-02 έως 2017-01-08 (1η εβδομάδα) και 2017-01-09 έως 2017-01-15 (2η εβδομάδα).

## Προεπεξεργασία κειμένων – tweets
>tweet.text → clean_text = sel f.clean_text(tweet.text).upper()
>>αφαίρεση http links, όλων των χαρακτήρων πλην αυτών του ελληνικού αλφαβήτου(u'[^Α-Ωα-ωΆ-Ώά-ώ]), αφαίρεση τόνων και διαλυτικών (''.join(c for c in unicodedata.normalize('NFD', tmp3) if unicodedata.category(c) != 'Mn')) και όλοι οι χαρακτήρες σε κεφαλαία(upper())

> clean_text → clean_text_without_stopwords = self.remove_stopwords(clean_text, stopwords)
>>αφαίρεση όλων των τετριμμένων λέξεων που περιγράφονται στο αρχείο greekstopwords.txt

> clean_text_without_stopwords → stemmed_text_without_stopwords = sel f.stem(clean_text_without_stopwords)
>>αποκοπή καταλήξεων με βάση τον αλγόριθμο που υλοποιείται στο αρχείο stemming.py

Αρχικά, τα αποθήκευα σε βάση δεδομένων αλλά για την υπόλοιπη
εργασία τα έκανα export από τη βάση σε txt αρχεία.

## Κατηγοριοποίηση κειμένων – tweets
>• Tokenization με βάση το κενό ‘ ’ του κάθε κειμένου-tweet.<br />
>• Σύκριση του κάθε token-όρου με τις λίστες των θετικών και αρνητικών λέξεων (PosLex.xls, NegLex.xls).<br />
>• Όταν ένας όρος ανήκει στη λίστα του θετικού λεξικού, τότε θεωρείται θετικός. Αν πάλι ανήκει στη λίστα του αρνητικού λεξικού, αρνητικός.<br />
>• Αν ο αριθμός των θετικών όρων σε ένα tweet είναι μεγαλύτερος των αρνητικών τότε το tweet θεωρείται θετικό. Σε αντίθετη
περίπτωση, αρνητικό. Αν ο αριθμός των θετικών όρων ισούται με τον αριθμό των αρνητικών θεωρείται ουδέτερο το tweet.<br />
>• Αποθήκευση των αποτελεσμάτων κάθε ημέρας στο αρχείo results.xlsx<br />

## Οπτικοποίηση εβδομαδιαίων αποτελεσμάτων
>• Χρήση της βιβλιοθήκης matplotlib.pyplot για την οπτικοποίηση των αποτελεσμάτων.

>• Παίρνει ως input το αρχείο results.xlsx και βγάζει σαν έξοδο 8 διαδοχικά παράθυρα με τα αποτελέσματα για την κάθε
κατηγορία tweets και για τις 2 εβδομάδες.

>• Παράδειγμα
![alt tag](https://github.com/tomdim/ir_twitter_project/blob/master/results_week2/figure_tsipras.png)

>Η περίληψη της εβδομάδας περιλαμβάνει:<br />
>>**Total Tweets**: ο συνολικός αριθμός tweets της κατηγορίας (π.χ.@atsipras) της εβδομάδας<br />
>>**Positive**: ο αριθμός των θετικών tweets της εβδομάδας<br />
>>**Negative**: ο αριθμός των αρνητικών tweets της εβδομάδας<br />
>>**Neutral**: ο αριθμός των ουδέτερων tweets της εβδομάδας<br />
>>**Avg Pos**: μέσος όρος των θετικών tweets ανά ημέρα της εβδομάδας<br />
>>**Avg Neg**: μέσος όρος των αρνητικών tweets ανά ημέρα της εβδομάδας<br />
>>**St. Deviation Pos**: τυπική απόκλιση των θετικών tweets της εβδομάδας<br />
>>**St. Deviation Neg**: τυπική απόκλιση των αρνητικών tweets της εβδομάδας<br />

## Ανάλυση εβδομαδιαίων tweets (term x document, svd ανάλυση, ευκλείδια απόσταση μεταξύ terms, p nearest terms)
>• Δημιουργία του term X document:<br />
>>[[ 1. 0. 0. ..., 0. 0. 0.]<br />
>>[ 1. 0. 0. ..., 0. 0. 0.]<br />
>>[ 1. 0. 0. ..., 0. 0. 0.]<br />
>>...,<br />
>>[ 0. 0. 0. ..., 1. 0. 0.]<br />
>>[ 0. 0. 0. ..., 0. 1. 0.]<br />
>>[ 0. 0. 0. ..., 0. 0. 1.]], όπου 1 σημαίνει ότι υπάρχει ο όρος(term) στο document. Κρατάμε τα μοναδικά terms, αποφεύγουμε τα διπλότυπα.<br />
>• Αφαίρεση των γραμμών που κάνουν άθροισμα μικρότερο του 2. Κρατάμε τους όρους(terms) που βρίσκονται τουλάχιστον σε 2 κείμενα(documents).<br />
>• SVD ανάλυση μέσω της εντολής <br />
>>U, S, V = np.linalg.svd(X, full_matrices=True)<br />
>>και κρατάμε τις πρώτες 100 στήλες (k = 100) του πίνακα U (αναπαράσταση των όρων) μεγέθους πλέον (t x 100)<br />
>• Προϋπολογίζουμε την euclidean distance μεταξύ των vectors των όρων και τα τις αποθηκεύουμε αυτές τις αποστάσεις σε έναν πίνακα distances μεγέθους (t x t), όπου η κεντρική διαγώνιος είναι 0 (αφού όταν i=j σημαίνει ότι είναι ο ίδιος όρος)<br />
>• Εύρεση των p πλησιέστερων όρων για p = 1, 2, 4, 5, 10, των όρων που ανήκουν σε καποια από τα 2 λεξικά (PosLex, NegLex).<br />
>>Ουσιαστικά, βρίσκουμε τις 1, 2, 4, 5, 10 μικρότερες αποστάσεις στον πίνακα distances από τον κάθε παραπάνω όρο που ικανοποιεί τη συνθήκη και τα θεωρούμε ως πλησιέστεροι όροι.<br />
>>Αν ο όρος του οποίου ψάχνουμε τους πλησιέστερους όρους είναι θετικός, τότε και οι πλησιέστεροί του όροι θεωρούνται θετικοί και αποθηκεύονται σε αρχείο ExtPos(t).txt στο filepath extW/p (όπου W = {1, 2} για την εβδομάδα και p = {1, 2, 4, 5, 10} για το p.<br />
>>Αντίστοιχα, όταν είναι αρνητικός, τότε και οι πλησιέστεροί του όροι θεωρούνται αρνητικοί και αποθηκεύονται σε αρχείο ExtNeg(t).txt στο filepath extW/p.<br />
>• Τέλος, υπολογίζεται ο μέσος όρος των p πλησιέστερων όρων που ανήκουν σε κάποιο από τα δύο λεξικά και εκτυπώνονται τα σύνολα των ExtPost, ExtNeg που δεν άνηκαν σε κάποιο από τα δύο λεξικά. <br />

Στο filepath ext1/result_of_analysis.txt υπάρχουν τα αποτελέσματα που βγάζει στο output o κώδικας του Analysis.py για τα tweets της 1ης εβδομάδας και αντίστοιχα στο ext2/result_of_analysis.txt για τα tweets της 2ης.

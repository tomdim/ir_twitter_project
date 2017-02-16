# -*- coding: cp1253 -*-

##Ελληνικό Ανοιχτό Πανεπιστήμιο - Πρόγραμμα Σπουδών Πληροφορικής
##Πτυχιακή Εργασία: HOU-CS-UGP-2013-18
##"Αλγόριθμοι Αποδοτικής Επιλογής Χαρακτηριστικών για Κατηγοριοποίηση Κειμένου στην Ελληνική Γλώσσα"
##Αλέξανδρος Καλαπόδης
##Επιβλέπων Καθηγητής: Σπύρος Λυκοθανάσης, Τμήμα Μηχανικών Η/Υ & Πληροφορικής, Πανεπιστήμιο Πάτρας

##Implementation in Python of the greek stemmer presented by Giorgios Ntais during his master thesis with title
##"Development of a Stemmer for the Greek Language" in the Department of Computer and Systems Sciences
##at Stockholm's University / Royal Institute of Technology.

##The system takes as input a word and removes its inflexional suffix according to a rule based algorithm.
##The algorithm follows the known Porter algorithm for the English language and it is developed according to the
##grammatical rules of the Modern Greek language.

VOWELS = [u'Α', u'Ε', u'Η', u'Ι', u'Ο', u'Υ', u'Ω', u'Ά', u'Έ', u'Ή', u'Ί', u'Ό', u'Ύ', u'Ώ', u'Ϊ', u'Ϋ']

def ends_with(word, suffix):
    return word[len(word) - len(suffix):] == suffix

def stem(word):
    initial = word
    done = len(word) <= 3
    
    ##rule-set  1
    ##ΓΙΑΓΙΑΔΕΣ->ΓΙΑΓ, ΟΜΑΔΕΣ->ΟΜΑΔ
    if not done:
        for suffix in [u'ΙΑΔΕΣ', u'ΑΔΕΣ', u'ΑΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                remaining_part_does_not_end_on = True
                for s in [u'ΟΚ', u'ΜΑΜ', u'ΜΑΝ', u'ΜΠΑΜΠ', u'ΠΑΤΕΡ', u'ΓΙΑΓ', u'ΝΤΑΝΤ', u'ΚΥΡ', u'ΘΕΙ', u'ΠΕΘΕΡ']:
                    if ends_with(word, s):
                        remaining_part_does_not_end_on = False
                        break
                if remaining_part_does_not_end_on:
                    word = word + u'ΑΔ'
                done = True
                break

    ##rule-set  2
    ##ΚΑΦΕΔΕΣ->ΚΑΦ, ΓΗΠΕΔΩΝ->ΓΗΠΕΔ
    if not done:
        for suffix in [u'ΕΔΕΣ', u'ΕΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in [u'ΟΠ', u'ΙΠ', u'ΕΜΠ', u'ΥΠ', u'ΓΗΠ', u'ΔΑΠ', u'ΚΡΑΣΠ', u'ΜΙΛ']:
                    if ends_with(word, s):
                        word = word + u'ΕΔ'
                        break
                done = True
                break

    ##rule-set  3
    ##ΠΑΠΠΟΥΔΩΝ->ΠΑΠΠ, ΑΡΚΟΥΔΕΣ->ΑΡΚΟΥΔ
    if not done:
        for suffix in [u'ΟΥΔΕΣ', u'ΟΥΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in [u'ΑΡΚ', u'ΚΑΛΙΑΚ', u'ΠΕΤΑΛ', u'ΛΙΧ', u'ΠΛΕΞ', u'ΣΚ', u'Σ', u'ΦΛ', u'ΦΡ', u'ΒΕΛ', u'ΛΟΥΛ', u'ΧΝ', u'ΣΠ', u'ΤΡΑΓ', u'ΦΕ']:
                    if ends_with(word, s):
                        word = word + u'ΟΥΔ'
                        break
                done = True
                break

    ##rule-set  4
    ##ΥΠΟΘΕΣΕΩΣ->ΥΠΟΘΕΣ, ΘΕΩΝ->ΘΕ
    if not done:
        for suffix in [u'ΕΩΣ', u'ΕΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in [u'Θ', u'Δ', u'ΕΛ', u'ΓΑΛ', u'Ν', u'Π', u'ΙΔ', u'ΠΑΡ']:
                    if ends_with(word, s):
                        word = word + u'Ε'
                        break
                done = True
                break

    ##rule-set  5
    ##ΠΑΙΔΙΑ->ΠΑΙΔ, ΤΕΛΕΙΟΥ->ΤΕΛΕΙ
    if not done:
        for suffix in [u'ΙΑ', u'ΙΟΥ', u'ΙΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + u'Ι'
                        break
                done = True
                break

    ##rule-set  6
    ##ΖΗΛΙΑΡΙΚΟ->ΖΗΛΙΑΡ, ΑΓΡΟΙΚΟΣ->ΑΓΡΟΙΚ
    if not done:
        for suffix in [u'ΙΚΑ', u'ΙΚΟΥ', u'ΙΚΩΝ', u'ΙΚΟΣ', u'ΙΚΟ', u'ΙΚΗ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΑΛ', u'ΑΔ', u'ΕΝΔ', u'ΑΜΑΝ', u'ΑΜΜΟΧΑΛ', u'ΗΘ', u'ΑΝΗΘ', u'ΑΝΤΙΔ', u'ΦΥΣ', u'ΒΡΩΜ', u'ΓΕΡ', u'ΕΞΩΔ', u'ΚΑΛΠ',
                            u'ΚΑΛΛΙΝ', u'ΚΑΤΑΔ', u'ΜΟΥΛ', u'ΜΠΑΝ', u'ΜΠΑΓΙΑΤ', u'ΜΠΟΛ', u'ΜΠΟΣ', u'ΝΙΤ', u'ΞΙΚ', u'ΣΥΝΟΜΗΛ', u'ΠΕΤΣ', u'ΠΙΤΣ',
                            u'ΠΙΚΑΝΤ', u'ΠΛΙΑΤΣ', u'ΠΟΝΤ', u'ΠΟΣΤΕΛΝ', u'ΠΡΩΤΟΔ', u'ΣΕΡΤ', u'ΣΥΝΑΔ', u'ΤΣΑΜ', u'ΥΠΟΔ', u'ΦΙΛΟΝ', u'ΦΥΛΟΔ',
                            u'ΧΑΣ']:
                    word = word + u'ΙΚ'
                else:
                    for s in VOWELS:
                        if ends_with(word, s):
                            word = word + u'ΙΚ'
                            break
                done = True
                break

    ##rule-set  7
    ##ΑΓΑΠΑΓΑΜΕ->ΑΓΑΠ, ΑΝΑΠΑΜΕ->ΑΝΑΠΑΜ
    if not done:
        if word == u'ΑΓΑΜΕ': word = 2*word
        for suffix in [u'ΗΘΗΚΑΜΕ', u'ΑΓΑΜΕ', u'ΗΣΑΜΕ', u'ΟΥΣΑΜΕ', u'ΗΚΑΜΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'Φ']:
                    word = word + u'ΑΓΑΜ'
                done = True
                break
        if not done and ends_with(word, u'ΑΜΕ'):
            word = word[:len(word) - len(u'ΑΜΕ')]
            if word in [u'ΑΝΑΠ', u'ΑΠΟΘ', u'ΑΠΟΚ', u'ΑΠΟΣΤ', u'ΒΟΥΒ', u'ΞΕΘ', u'ΟΥΛ', u'ΠΕΘ', u'ΠΙΚΡ', u'ΠΟΤ', u'ΣΙΧ', u'Χ']:
                word = word + u'ΑΜ'
            done = True

    ##rule-set  8
    ##ΑΓΑΠΗΣΑΜΕ->ΑΓΑΠ, ΤΡΑΓΑΝΕ->ΤΡΑΓΑΝ
    if not done:
        for suffix in [u'ΙΟΥΝΤΑΝΕ', u'ΙΟΝΤΑΝΕ', u'ΟΥΝΤΑΝΕ', u'ΗΘΗΚΑΝΕ', u'ΟΥΣΑΝΕ', u'ΙΟΤΑΝΕ', u'ΟΝΤΑΝΕ', u'ΑΓΑΝΕ', u'ΗΣΑΝΕ',
                       u'ΟΤΑΝΕ', u'ΗΚΑΝΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΤΡ', u'ΤΣ', u'Φ']:
                    word = word + u'ΑΓΑΝ'
                done = True
                break
        if not done and ends_with(word, u'ΑΝΕ'):
            word = word[:len(word) - len(u'ΑΜΕ')]
            if word in [u'ΒΕΤΕΡ', u'ΒΟΥΛΚ', u'ΒΡΑΧΜ', u'Γ', u'ΔΡΑΔΟΥΜ', u'Θ', u'ΚΑΛΠΟΥΖ', u'ΚΑΣΤΕΛ', u'ΚΟΡΜΟΡ', u'ΛΑΟΠΛ', u'ΜΩΑΜΕΘ', u'Μ',
                        u'ΜΟΥΣΟΥΛΜ', u'Ν', u'ΟΥΛ', u'Π', u'ΠΕΛΕΚ', u'ΠΛ', u'ΠΟΛΙΣ', u'ΠΟΡΤΟΛ', u'ΣΑΡΑΚΑΤΣ', u'ΣΟΥΛΤ', u'ΤΣΑΡΛΑΤ', u'ΟΡΦ',
                        u'ΤΣΙΓΓ', u'ΤΣΟΠ', u'ΦΩΤΟΣΤΕΦ', u'Χ', u'ΨΥΧΟΠΛ', u'ΑΓ', u'ΟΡΦ', u'ΓΑΛ', u'ΓΕΡ', u'ΔΕΚ', u'ΔΙΠΛ', u'ΑΜΕΡΙΚΑΝ', u'ΟΥΡ',
                        u'ΠΙΘ', u'ΠΟΥΡΙΤ', u'Σ', u'ΖΩΝΤ', u'ΙΚ', u'ΚΑΣΤ', u'ΚΟΠ', u'ΛΙΧ', u'ΛΟΥΘΗΡ', u'ΜΑΙΝΤ', u'ΜΕΛ', u'ΣΙΓ', u'ΣΠ', u'ΣΤΕΓ',
                        u'ΤΡΑΓ', u'ΤΣΑΓ', u'Φ', u'ΕΡ', u'ΑΔΑΠ', u'ΑΘΙΓΓ', u'ΑΜΗΧ', u'ΑΝΙΚ', u'ΑΝΟΡΓ', u'ΑΠΗΓ', u'ΑΠΙΘ', u'ΑΤΣΙΓΓ', u'ΒΑΣ',
                        u'ΒΑΣΚ', u'ΒΑΘΥΓΑΛ', u'ΒΙΟΜΗΧ', u'ΒΡΑΧΥΚ', u'ΔΙΑΤ', u'ΔΙΑΦ', u'ΕΝΟΡΓ', u'ΘΥΣ', u'ΚΑΠΝΟΒΙΟΜΗΧ', u'ΚΑΤΑΓΑΛ', u'ΚΛΙΒ',
                        u'ΚΟΙΛΑΡΦ', u'ΛΙΒ', u'ΜΕΓΛΟΒΙΟΜΗΧ', u'ΜΙΚΡΟΒΙΟΜΗΧ', u'ΝΤΑΒ', u'ΞΗΡΟΚΛΙΒ', u'ΟΛΙΓΟΔΑΜ', u'ΟΛΟΓΑΛ', u'ΠΕΝΤΑΡΦ',
                        u'ΠΕΡΗΦ', u'ΠΕΡΙΤΡ', u'ΠΛΑΤ', u'ΠΟΛΥΔΑΠ', u'ΠΟΛΥΜΗΧ', u'ΣΤΕΦ', u'ΤΑΒ', u'ΤΕΤ', u'ΥΠΕΡΗΦ', u'ΥΠΟΚΟΠ', u'ΧΑΜΗΛΟΔΑΠ',
                        u'ΨΗΛΟΤΑΒ']:
                word = word + u'ΑΝ'
            else:
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + u'ΑΝ'
                        break
            done = True

    ##rule-set  9
    ##ΑΓΑΠΗΣΕΤΕ->ΑΓΑΠ, ΒΕΝΕΤΕ->ΒΕΝΕΤ
    if not done:
        if ends_with(word, u'ΗΣΕΤΕ'):
            word = word[:len(word) - len(u'ΗΣΕΤΕ')]
            done = True
        elif ends_with(word, u'ΕΤΕ'):
            word = word[:len(word) - len(u'ΕΤΕ')]
            if word in [u'ΑΒΑΡ', u'ΒΕΝ', u'ΕΝΑΡ', u'ΑΒΡ', u'ΑΔ', u'ΑΘ', u'ΑΝ', u'ΑΠΛ', u'ΒΑΡΟΝ', u'ΝΤΡ', u'ΣΚ', u'ΚΟΠ', u'ΜΠΟΡ', u'ΝΙΦ', u'ΠΑΓ',
                        u'ΠΑΡΑΚΑΛ', u'ΣΕΡΠ', u'ΣΚΕΛ', u'ΣΥΡΦ', u'ΤΟΚ', u'Υ', u'Δ', u'ΕΜ', u'ΘΑΡΡ', u'Θ']:
                word = word + u'ΕΤ'
            else:
                for s in [u'ΟΔ', u'ΑΙΡ', u'ΦΟΡ', u'ΤΑΘ', u'ΔΙΑΘ', u'ΣΧ', u'ΕΝΔ', u'ΕΥΡ', u'ΤΙΘ', u'ΥΠΕΡΘ', u'ΡΑΘ', u'ΕΝΘ', u'ΡΟΘ', u'ΣΘ', u'ΠΥΡ',
                          u'ΑΙΝ', u'ΣΥΝΔ', u'ΣΥΝ', u'ΣΥΝΘ', u'ΧΩΡ', u'ΠΟΝ', u'ΒΡ', u'ΚΑΘ', u'ΕΥΘ', u'ΕΚΘ', u'ΝΕΤ', u'ΡΟΝ', u'ΑΡΚ', u'ΒΑΡ', u'ΒΟΛ',
                          u'ΩΦΕΛ'] + VOWELS:
                    if ends_with(word, s):
                        word = word + u'ΕΤ'
                        break
            done = True

    ##rule-set 10
    ##ΑΓΑΠΩΝΤΑΣ->ΑΓΑΠ, ΞΕΝΟΦΩΝΤΑΣ->ΞΕΝΟΦΩΝ
    if not done:
        for suffix in [u'ΟΝΤΑΣ', u'ΩΝΤΑΣ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΑΡΧ']:
                    word = word + u'ΟΝΤ'
                elif word in [u'ΞΕΝΟΦ', u'ΚΡΕ']:
                    word = word + u'ΩΝΤ'
                done = True
                break

    ##rule-set 11
    ##ΑΓΑΠΙΟΜΑΣΤΕ->ΑΓΑΠ, ΟΝΟΜΑΣΤΕ->ΟΝΟΜΑΣΤ
    if not done:
        for suffix in [u'ΙΟΜΑΣΤΕ', u'ΟΜΑΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΟΝ']:
                    word = word + u'ΟΜΑΣΤ'
                done = True
                break

    ##rule-set 12
    ##ΑΓΑΠΙΕΣΤΕ->ΑΓΑΠ, ΠΙΕΣΤΕ->ΠΙΕΣΤ
    if not done:
        for suffix in [u'ΙΕΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'Π', u'ΑΠ', u'ΣΥΜΠ', u'ΑΣΥΜΠ', u'ΚΑΤΑΠ', u'ΜΕΤΑΜΦ']:
                    word = word + u'ΙΕΣΤ'
                done = True
                break
    if not done:
        for suffix in [u'ΕΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΑΛ', u'ΑΡ', u'ΕΚΤΕΛ', u'Ζ', u'Μ', u'Ξ', u'ΠΑΡΑΚΑΛ', u'ΑΡ', u'ΠΡΟ', u'ΝΙΣ']:
                    word = word + u'ΕΣΤ'
                done = True
                break

    ##rule-set 13
    ##ΧΤΙΣΤΗΚΕ->ΧΤΙΣΤ, ΔΙΑΘΗΚΕΣ->ΔΙΑΘΗΚ
    if not done:
        for suffix in [u'ΗΘΗΚΑ', u'ΗΘΗΚΕΣ', u'ΗΘΗΚΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                done = True
                break
    if not done:
        for suffix in [u'ΗΚΑ', u'ΗΚΕΣ', u'ΗΚΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΔΙΑΘ', u'Θ', u'ΠΑΡΑΚΑΤΑΘ', u'ΠΡΟΣΘ', u'ΣΥΝΘ']:
                    word = word + u'ΗΚ'
                else:
                    for suffix in [u'ΣΚΩΛ', u'ΣΚΟΥΛ', u'ΝΑΡΘ', u'ΣΦ', u'ΟΘ', u'ΠΙΘ']:
                        if ends_with(word, suffix):
                            word = word + u'ΗΚ'
                            break
                done = True
                break
            
    ##rule-set 14
    ##ΧΤΥΠΟΥΣΕΣ->ΧΤΥΠ, ΜΕΔΟΥΣΕΣ->ΜΕΔΟΥΣ
    if not done:
        for suffix in [u'ΟΥΣΑ', u'ΟΥΣΕΣ', u'ΟΥΣΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΦΑΡΜΑΚ', u'ΧΑΔ', u'ΑΓΚ', u'ΑΝΑΡΡ', u'ΒΡΟΜ', u'ΕΚΛΙΠ', u'ΛΑΜΠΙΔ', u'ΛΕΧ', u'Μ', u'ΠΑΤ', u'Ρ', u'Λ', u'ΜΕΔ', u'ΜΕΣΑΖ',
                            u'ΥΠΟΤΕΙΝ', u'ΑΜ', u'ΑΙΘ', u'ΑΝΗΚ', u'ΔΕΣΠΟΖ', u'ΕΝΔΙΑΦΕΡ', u'ΔΕ', u'ΔΕΥΤΕΡΕΥ', u'ΚΑΘΑΡΕΥ', u'ΠΛΕ', u'ΤΣΑ']:
                    word = word + u'ΟΥΣ'
                else:
                    for s in [u'ΠΟΔΑΡ', u'ΒΛΕΠ', u'ΠΑΝΤΑΧ', u'ΦΡΥΔ', u'ΜΑΝΤΙΛ', u'ΜΑΛΛ', u'ΚΥΜΑΤ', u'ΛΑΧ', u'ΛΗΓ', u'ΦΑΓ', u'ΟΜ', u'ΠΡΩΤ'] + VOWELS:
                        if ends_with(word, s):
                            word = word + u'ΟΥΣ'
                            break
                done = True
                break

    ##rule-set 15
    #ΚΟΛΛΑΓΕΣ->ΚΟΛΛ, ΑΒΑΣΤΑΓΑ->ΑΒΑΣΤ
    if not done:
        for suffix in [u'ΑΓΑ', u'ΑΓΕΣ', u'ΑΓΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΑΒΑΣΤ', u'ΠΟΛΥΦ', u'ΑΔΗΦ', u'ΠΑΜΦ', u'Ρ', u'ΑΣΠ', u'ΑΦ', u'ΑΜΑΛ', u'ΑΜΑΛΛΙ', u'ΑΝΥΣΤ', u'ΑΠΕΡ', u'ΑΣΠΑΡ', u'ΑΧΑΡ',
                            u'ΔΕΡΒΕΝ', u'ΔΡΟΣΟΠ', u'ΞΕΦ', u'ΝΕΟΠ', u'ΝΟΜΟΤ', u'ΟΛΟΠ', u'ΟΜΟΤ', u'ΠΡΟΣΤ', u'ΠΡΟΣΩΠΟΠ', u'ΣΥΜΠ', u'ΣΥΝΤ', u'Τ',
                            u'ΥΠΟΤ', u'ΧΑΡ', u'ΑΕΙΠ', u'ΑΙΜΟΣΤ', u'ΑΝΥΠ', u'ΑΠΟΤ', u'ΑΡΤΙΠ', u'ΔΙΑΤ', u'ΕΝ', u'ΕΠΙΤ', u'ΚΡΟΚΑΛΟΠ', u'ΣΙΔΗΡΟΠ',
                            u'Λ', u'ΝΑΥ', u'ΟΥΛΑΜ', u'ΟΥΡ', u'Π', u'ΤΡ', u'Μ']:
                    word = word + u'ΑΓ'
                else:
                    for s in [u'ΟΦ', u'ΠΕΛ', u'ΧΟΡΤ', u'ΣΦ', u'ΡΠ', u'ΦΡ', u'ΠΡ', u'ΛΟΧ', u'ΣΜΗΝ']:
                        # ΑΦΑΙΡΕΘΗΚΕ: 'ΛΛ'
                        if ends_with(word, s):
                            if not word in [u'ΨΟΦ', u'ΝΑΥΛΟΧ']:
                                word = word + u'ΑΓ'
                            break
                done = True
                break

    ##rule-set 16
    ##ΑΓΑΠΗΣΕ->ΑΓΑΠ, ΝΗΣΟΥ->ΝΗΣ
    if not done:
        for suffix in [u'ΗΣΕ', u'ΗΣΟΥ', u'ΗΣΑ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'Ν', u'ΧΕΡΣΟΝ', u'ΔΩΔΕΚΑΝ', u'ΕΡΗΜΟΝ', u'ΜΕΓΑΛΟΝ', u'ΕΠΤΑΝ', u'ΑΓΑΘΟΝ']:
                    word = word + u'ΗΣ'
                done = True
                break
            
    ##rule-set 17
    ##ΑΓΑΠΗΣΤΕ->ΑΓΑΠ, ΣΒΗΣΤΕ->ΣΒΗΣΤ
    if not done:
        for suffix in [u'ΗΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΑΣΒ', u'ΣΒ', u'ΑΧΡ', u'ΧΡ', u'ΑΠΛ', u'ΑΕΙΜΝ', u'ΔΥΣΧΡ', u'ΕΥΧΡ', u'ΚΟΙΝΟΧΡ', u'ΠΑΛΙΜΨ']:
                    word = word + u'ΗΣΤ'
                done = True
                break
            
    ##rule-set 18
    ##ΑΓΑΠΟΥΝΕ->ΑΓΑΠ, ΣΠΙΟΥΝΕ->ΣΠΙΟΥΝ
    if not done:
        for suffix in [u'ΟΥΝΕ', u'ΗΣΟΥΝΕ', u'ΗΘΟΥΝΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'Ν', u'Ρ', u'ΣΠΙ', u'ΣΤΡΑΒΟΜΟΥΤΣ', u'ΚΑΚΟΜΟΥΤΣ', u'ΕΞΩΝ']:
                    word = word + u'OYN'
                done = True
                break
            
    ##rule-set 19
    ##ΑΓΑΠΟΥΜΕ->ΑΓΑΠ, ΦΟΥΜΕ->ΦΟΥΜ
    if not done:
        for suffix in [u'ΟΥΜΕ', u'ΗΣΟΥΜΕ', u'ΗΘΟΥΜΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in [u'ΠΑΡΑΣΟΥΣ', u'Φ', u'Χ', u'ΩΡΙΟΠΛ', u'ΑΖ', u'ΑΛΛΟΣΟΥΣ', u'ΑΣΟΥΣ']:
                    word = word + u'ΟΥΜ'
                done = True
                break
            
    ##rule-set 20
    ##ΚΥΜΑΤΑ->ΚΥΜ, ΧΩΡΑΤΟ->ΧΩΡΑΤ
    if not done:
        for suffix in [u'ΜΑΤΑ', u'ΜΑΤΩΝ', u'ΜΑΤΟΣ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                word = word + u'Μ'
                done = True
                break
            
    ##rule-set 21
    if not done:
        for suffix in [u'ΙΟΝΤΟΥΣΑΝ', u'ΙΟΥΜΑΣΤΕ', u'ΙΟΜΑΣΤΑΝ', u'ΙΟΣΑΣΤΑΝ', u'ΟΝΤΟΥΣΑΝ', u'ΙΟΣΑΣΤΕ', u'ΙΕΜΑΣΤΕ', u'ΙΕΣΑΣΤΕ', u'ΙΟΜΟΥΝΑ',
                       u'ΙΟΣΟΥΝΑ', u'ΙΟΥΝΤΑΙ', u'ΙΟΥΝΤΑΝ', u'ΗΘΗΚΑΤΕ', u'ΟΜΑΣΤΑΝ', u'ΟΣΑΣΤΑΝ', u'ΟΥΜΑΣΤΕ', u'ΙΟΜΟΥΝ', u'ΙΟΝΤΑΝ', u'ΙΟΣΟΥΝ',
                       u'ΗΘΕΙΤΕ', u'ΗΘΗΚΑΝ', u'ΟΜΟΥΝΑ', u'ΟΣΑΣΤΕ', u'ΟΣΟΥΝΑ', u'ΟΥΝΤΑΙ', u'ΟΥΝΤΑΝ', u'ΟΥΣΑΤΕ', u'ΑΓΑΤΕ', u'ΕΙΤΑΙ', u'ΙΕΜΑΙ',
                       u'ΙΕΤΑΙ', u'ΙΕΣΑΙ', u'ΙΟΤΑΝ', u'ΙΟΥΜΑ', u'ΗΘΕΙΣ', u'ΗΘΟΥΝ', u'ΗΚΑΤΕ', u'ΗΣΑΤΕ', u'ΗΣΟΥΝ', u'ΟΜΟΥΝ', u'ΟΝΤΑΙ',
                       u'ΟΝΤΑΝ', u'ΟΣΟΥΝ', u'ΟΥΜΑΙ', u'ΟΥΣΑΝ', u'ΑΓΑΝ', u'ΑΜΑΙ', u'ΑΣΑΙ', u'ΑΤΑΙ', u'ΕΙΤΕ', u'ΕΣΑΙ', u'ΕΤΑΙ', u'ΗΔΕΣ',
                       u'ΗΔΩΝ', u'ΗΘΕΙ', u'ΗΚΑΝ', u'ΗΣΑΝ', u'ΗΣΕΙ', u'ΗΣΕΣ', u'ΟΜΑΙ', u'ΟΤΑΝ', u'ΑΕΙ', u'ΕΙΣ', u'ΗΘΩ', u'ΗΣΩ', u'ΟΥΝ',
                       u'ΟΥΣ', u'ΑΝ', u'ΑΣ', u'ΑΩ', u'ΕΙ', u'ΕΣ', u'ΗΣ', u'ΟΙ', u'ΟΝ', u'ΟΣ', u'ΟΥ', u'ΥΣ', u'ΩΝ', u'ΩΣ', u'Α', u'Ε', u'Ι', u'Η',
                       u'Ο', u'Υ', u'Ω']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                break

    ##rule-set 22
    ##ΠΛΗΣΙΕΣΤΑΤΟΣ->ΠΛΥΣΙ, ΜΕΓΑΛΥΤΕΡΗ->ΜΕΓΑΛ, ΚΟΝΤΟΤΕΡΟ->ΚΟΝΤ
    if not done:
        for suffix in [u'ΕΣΤΕΡ', u'ΕΣΤΑΤ', u'ΟΤΕΡ', u'ΟΤΑΤ', u'ΥΤΕΡ', u'ΥΤΑΤ', u'ΩΤΕΡ', u'ΩΤΑΤ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                break

    return word


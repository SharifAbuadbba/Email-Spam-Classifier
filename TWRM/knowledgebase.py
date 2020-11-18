from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import math


class Build_Knowledgebase:

    def getsplit_individually(self, data,datatype, split):
        _class_type = [ ]
        _embody = [ ]
        for iteminsex in range(len(data)):
            if datatype[ iteminsex ] == split:
                _class_type.append ( [ datatype[ iteminsex ] ] )
                _embody.append ( [ data[ iteminsex ] ] )
        return _class_type, _embody


    def get_vector_train_words_rank(self, data,spamdata,hamdata):
        word_ranking = [ ]
        #data
        aggregation_1_data = Build_Knowledgebase.get_all_in_one ( self,data )
        clear_sparcelist_data = Build_Knowledgebase.remove_special_character ( self,aggregation_1_data )
        list_vocabulary_terms_data = list ( set ( clear_sparcelist_data ) )
        #spam
        aggregation_1_spam = Build_Knowledgebase.get_all_in_one ( self,spamdata )
        clear_sparcelist_spam = Build_Knowledgebase.remove_special_character ( self,aggregation_1_spam )
        list_vocabulary_terms_spam = list ( set ( clear_sparcelist_spam ) )
        #spamnorm=1-len(spamdata)/len(data)
        #ham
        aggregation_1_ham = Build_Knowledgebase.get_all_in_one ( self,hamdata )
        clear_sparcelist_ham = Build_Knowledgebase.remove_special_character ( self,aggregation_1_ham )
        list_vocabulary_terms_ham = list ( set ( clear_sparcelist_ham ) )
        #hamnorm=1-len(hamdata)/len(data)
        wordslist=[]
        for words in list_vocabulary_terms_data:
            n_ward_in_spam = [ i for i in range ( len ( list_vocabulary_terms_spam ) ) if list_vocabulary_terms_spam[ i ] == words ]
            n_ward_in_ham= [ i for i in range ( len ( list_vocabulary_terms_ham ) ) if list_vocabulary_terms_ham[ i ] == words ]
            a_spam = len ( n_ward_in_spam )
            a_ham = len(n_ward_in_ham)
            b=a_spam+a_ham
            if b>0:
                rank_ward_in_spam =math.degrees (math.acos (b/math.sqrt(a_spam*a_spam+b*b)))
                rank_ward_in_ham=math.degrees (math.acos (b/math.sqrt(a_ham*a_ham+b*b)))
                word_ranking.append ( [rank_ward_in_spam,rank_ward_in_ham] )
                wordslist.extend([words])
        return word_ranking,wordslist


    def get_all_in_one(self, data):
        data2singleton = [ ]
        for item in data:
            data2singleton.extend ( item )
        return data2singleton


    def remove_special_character(self, Text):
        # text is list
        e_string = ' '.join ( [ str ( elem ) for elem in Text ] ).lower ()
        stop_words = set ( stopwords.words ( 'english' ) )
        word_tokens = word_tokenize ( e_string )
        filtered_sentence = [ w for w in word_tokens if not w in stop_words ]
        filtered_sentence = ' '.join ( [ str ( elem ) for elem in filtered_sentence ] )
        filtered_sentence = re.sub ( '\W+', ' ', filtered_sentence )
        filtered_sentence = filtered_sentence.split ()
        for item in filtered_sentence:
            if len(item) == 1:
                filtered_sentence.remove ( item )
        # filtered_sentence example [ali,hake,ali,hussain]
        return filtered_sentence


    def emailrank_class(self, data, wordranking, wordlist):
        predecit_class = [ ]
        # n=1
        for emailindex in range (len(data)):
            e_clear = Build_Knowledgebase.remove_special_character ( self,data[emailindex] )
            spam_theta=0
            ham_theta=0
            if len(e_clear)<9:
                predecit_class.extend ( [ 'ham' ] )
            else:
                for word in e_clear:
                    word_index = wordlist.index ( word ) if word in wordlist else [ ]
                    if word_index:
                        spam_theta += wordranking[ word_index ][ 0 ]
                        ham_theta += wordranking[ word_index ][ 1 ]
                if spam_theta >= ham_theta:
                    predecit_class.extend ( [ 'spam' ] )
                else:
                    predecit_class.extend ( [ 'ham' ] )
        return predecit_class





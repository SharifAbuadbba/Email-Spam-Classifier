import knowledgebase
from sklearn import metrics

class TWRM:
    def __init__(self, train=None, test=None, trainclass=None, testclass=None):
        self.train=train
        self.test=test
        self.trainclass=trainclass
        self.testclass=testclass

    def TWRM_system(self):
        return TWRM.evaluation(self,TWRM.predict(self))


    def TWRM_trainsystem(self):
        #find SPAM and HAM emails
        print('[START] train TWRM')
        spamemailtype, spamemailcontent = knowledgebase.Build_Knowledgebase().\
            getsplit_individually ( self.train,self.trainclass,'spam' )
        hamemailtype, hamemailcontent = knowledgebase.Build_Knowledgebase ().\
            getsplit_individually ( self.train,self.trainclass,'ham' )
        wordsranking, wordslist = knowledgebase.Build_Knowledgebase ().\
            get_vector_train_words_rank ( self.train, spamemailcontent, hamemailcontent )
        print('[END]')
        return  wordsranking, wordslist

    def predict(self):
        wordsranking, wordslist=TWRM.TWRM_trainsystem(self)
        return knowledgebase.Build_Knowledgebase ()\
            .emailrank_class ( self.test, wordsranking, wordslist )


    def evaluation(self,predict):
        print('Evalution TWRM')
        Accuracy = metrics.accuracy_score ( self.testclass, predict ) * 100
        prscion = metrics.precision_score ( self.testclass, predict, average='macro' ) * 100
        Recall = metrics.recall_score ( self.testclass, predict, average='macro' ) * 100
        f1scor = 2 * (prscion * Recall) / (prscion + Recall)
        Confusion_Matrix = metrics.confusion_matrix ( self.testclass, predict )
        print('Accurance = ',Accuracy)
        print ( 'precision =',prscion)
        print ( 'Recall',Recall )
        print ( 'f1score=',f1scor )
        Performance = ['Accurance = ',Accuracy,'Recall',Recall,'precision =',prscion,'f1score=',f1scor,'Confusion_Matrix',Confusion_Matrix]
        return Performance







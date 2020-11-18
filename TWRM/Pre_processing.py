from sklearn.model_selection import train_test_split

class Data_Analysis_Processing:
    def splitdata(self,data,classdata,sizetest=0.60,RND=0):
        train, test, classtrain, classtest = \
            train_test_split ( data, classdata, test_size=sizetest, random_state=RND )
        print('random state = ' ,RND)
        print('Train data =',len(train) ,'  --',(1-sizetest)*100,'% of dataset')
        print ( 'Test data =', len ( test ) , '  --',(sizetest)*100,'% of dataset' )
        return train, test, classtrain, classtest


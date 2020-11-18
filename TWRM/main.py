import ReadData
import Pre_processing
import TWRM

if __name__ == '__main__':
    path_dataset="F:\Codes Collection\TWRM\SMSSpamCollection.csv"
    emailtype,emails,emaildata=ReadData.Read(path_dataset).csv2list()
    train,test,trainclass,testclass=Pre_processing.Data_Analysis_Processing().\
        splitdata(emails,emailtype)
    systemPerformance = TWRM.TWRM(train,test,trainclass,testclass).TWRM_system()




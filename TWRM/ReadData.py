import csv


class Read:
    def __init__(self,path):
        self.data_email_withcalss = []
        self.emails = []
        self.emailtype = []
        self.newline = ""
        self.emtype_poison = 0
        self.embody_position = 1
        self.path=path

    def csv2list(self):
        """
        Fit a model given data.
           :param filpath: a path of d file name )
        """
        print("the system reads data from path: ",self.path)
        csvfileload = open ( self.path, newline=self.newline )
        csvreaderdata = csv.reader ( csvfileload )
        header = next ( csvreaderdata )
        # print ( header )
        for row in csvreaderdata:
            _emailclass = row[ self.emtype_poison ]
            _emailbody = row[ self.embody_position]
            self.data_email_withcalss.append ( [ _emailclass, _emailbody ] )
            self.emailtype.extend([_emailclass] )
            self.emails.append ( [ _emailbody ] )
        return self.emailtype,self.emails,self.data_email_withcalss
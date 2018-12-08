class SavePass:
    def __init__(self,i,p):
        self.file_ = open("pass/pass.txt",'a')

        self.file_.write(i+"\t"+p+"\n")
        self.file_.close()
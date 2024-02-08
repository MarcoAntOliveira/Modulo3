class Log:
    def log(self, msg):
        raise NotImplementedError("implemente o metodo log")
    
class LogFilemixin(Log):
    def log(self, msg):
        print(msg)
class PrintFileMixin(Log):
    ...
        
if __name__ == '__main__':    
    l = Log()
    l.log("qualquer coisa")
   
import sys
# Gives us the error message
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="There is an error in the python script name [{0}] Line number [{1}] Message [{3}]".format(
         filename,exc_tb.tb_lineno,str(error)

    )

class Customexception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_detail=error_detail)

    def __str__(self):
        return self.error_message



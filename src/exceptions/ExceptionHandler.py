class ClientException:
    def __init__(self, exception: Exception):
        self.exception = exception
    
    def get_exception_message(self):
        return str(self.exception)
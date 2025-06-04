import sys

class AppException(Exception):
    """
    Custom exception class for detailed error reporting.
    Captures filename, line number, and the actual error message.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(str(error_message))
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error: Exception, error_detail: sys) -> str:
        """
        Returns detailed error message including file name and line number.
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
        
        return (f"Error occurred in script [{file_name}], "
                f"line [{line_number}]: {error}")

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.error_message}')"

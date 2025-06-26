import sys
import traceback
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""

    def __init__(self, error_msg: str, exc_tb):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        error = """

        An error occurred in the network security module.
        Please check the details below:
        
        """
        return f"{error}Error Message: {self.error_msg}\n        File: {self.file_name}\n        Line: {self.line_number}"


# if __name__ == "__main__":
#     try:
#         logger.info("Starting network security exception handling.")

#         # Simulate a low-level error
#         x = 1 / 0  # This will raise ZeroDivisionError

#     except Exception as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         custom_exception = NetworkSecurityException(str(e), exc_tb)
#         logger.error(custom_exception)
#         print(custom_exception)
#         sys.exit(1)

#     finally:
#         logger.info("Network security exception handling completed.")



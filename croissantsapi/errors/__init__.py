from fastapi import HTTPException


class ApiException(HTTPException):
    def __init__(self, status_code: int, error: dict):
        super().__init__(status_code, {"error": type(self).__name__, **error})

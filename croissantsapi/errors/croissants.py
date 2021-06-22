from croissantsapi.errors import ApiException


class UnknownCroissantRequest(ApiException):
    def __init__(self, id: str):
        super().__init__(
            404,
            {
                "message": f"Croissant request with id '{id}' does not exists",
                "id": id,
            },
        )

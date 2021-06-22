from croissantsapi.errors import ApiException


class UnknownBuilding(ApiException):
    def __init__(self, id: str):
        super().__init__(
            404,
            {
                "message": f"Building with id '{id}' does not exists",
                "id": id,
            },
        )


class BuildingFloorOverflow(ApiException):
    def __init__(self, id: str, floor: int, max_floors: int):
        super().__init__(
            400,
            {
                "message": f"Building with id '{id}' has less than the required {floor} floors (max floor = {max_floors})",
                "id": id,
                "floor": floor,
                "max_floors": max_floors,
            },
        )

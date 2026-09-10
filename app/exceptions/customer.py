class AppException(Exception):
    status_code = 500


class CustomerAlreadyExistsException(AppException):
    status_code = 409

    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Customer with email '{email}' already exists")


class CustomerNotFoundException(AppException):
    status_code = 404

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"Customer with id '{customer_id}' not found")
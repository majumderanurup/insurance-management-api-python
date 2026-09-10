from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def get_customers(self):
        return self.repository.get_all()
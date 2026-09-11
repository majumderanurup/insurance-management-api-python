import logging
from decimal import Decimal

from sqlalchemy.orm import Session

from app.exceptions.product import ProductBusinessRuleException
from app.models.product import Product, ProductType
from app.repositories.product_repository import ProductRepository


logger = logging.getLogger(__name__)


class ProductService:

    def __init__(
        self,
        repository: ProductRepository,
        db: Session,
    ):
        self.repository = repository
        self.db = db

    def _validate_product_rules(
        self,
        min_entry_age: int,
        max_entry_age: int,
        min_sum_assured: Decimal,
        max_sum_assured: Decimal,
    ) -> None:

        if min_entry_age > max_entry_age:
            raise ProductBusinessRuleException(
                "Minimum entry age cannot be greater than maximum entry age"
            )

        if min_sum_assured > max_sum_assured:
            raise ProductBusinessRuleException(
                "Minimum sum assured cannot be greater than maximum sum assured"
            )

    def get_products(self) -> list[Product]:
        logger.info("Fetching all products")

        return self.repository.get_all()

    def get_product(self, product_id: int) -> Product | None:
        logger.info(
            "Fetching product with id: %s",
            product_id,
        )

        return self.repository.get_by_id(product_id)

    def create_product(
        self,
        name: str,
        description: str,
        product_type: ProductType,
        min_entry_age: int,
        max_entry_age: int,
        min_sum_assured: Decimal,
        max_sum_assured: Decimal,
        active: bool,
    ) -> Product:

        logger.info("Creating product: %s", name)

        self._validate_product_rules(
            min_entry_age=min_entry_age,
            max_entry_age=max_entry_age,
            min_sum_assured=min_sum_assured,
            max_sum_assured=max_sum_assured,
        )

        product = Product(
            name=name,
            description=description,
            type=product_type,
            min_entry_age=min_entry_age,
            max_entry_age=max_entry_age,
            min_sum_assured=min_sum_assured,
            max_sum_assured=max_sum_assured,
            active=active,
        )

        try:
            product = self.repository.create(product)

            self.db.commit()
            self.db.refresh(product)

            logger.info(
                "Product created successfully with id: %s",
                product.id,
            )

            return product

        except Exception:
            self.db.rollback()

            logger.exception(
                "Failed to create product: %s",
                name,
            )

            raise

    def update_product(
        self,
        product_id: int,
        name: str,
        description: str,
        product_type: ProductType,
        min_entry_age: int,
        max_entry_age: int,
        min_sum_assured: Decimal,
        max_sum_assured: Decimal,
        active: bool,
    ) -> Product | None:

        logger.info(
            "Updating product with id: %s",
            product_id,
        )

        product = self.repository.get_by_id(product_id)

        if product is None:
            return None

        self._validate_product_rules(
            min_entry_age=min_entry_age,
            max_entry_age=max_entry_age,
            min_sum_assured=min_sum_assured,
            max_sum_assured=max_sum_assured,
        )

        product.name = name
        product.description = description
        product.type = product_type
        product.min_entry_age = min_entry_age
        product.max_entry_age = max_entry_age
        product.min_sum_assured = min_sum_assured
        product.max_sum_assured = max_sum_assured
        product.active = active

        try:
            self.repository.update(product)

            self.db.commit()
            self.db.refresh(product)

            logger.info(
                "Product updated successfully with id: %s",
                product_id,
            )

            return product

        except Exception:
            self.db.rollback()

            logger.exception(
                "Failed to update product with id: %s",
                product_id,
            )

            raise

    def delete_product(self, product_id: int) -> bool:

        logger.info(
            "Deleting product with id: %s",
            product_id,
        )

        product = self.repository.get_by_id(product_id)

        if product is None:
            return False

        try:
            self.repository.delete(product)

            self.db.commit()

            logger.info(
                "Product deleted successfully with id: %s",
                product_id,
            )

            return True

        except Exception:
            self.db.rollback()

            logger.exception(
                "Failed to delete product with id: %s",
                product_id,
            )

            raise
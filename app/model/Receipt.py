from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, INTEGER, TIMESTAMP
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db

class Receipt(db.Model):
    __tablename__ = 'Receipt'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'extend_existing': True
    }

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
    )

    storeName = db.Column(
        VARCHAR(128)
    )

    price = db.Column(
        INTEGER(10)
    )

    paymentDate = db.Column(
        TIMESTAMP
    )

    user = db.Column(
        VARCHAR(128)
    )

    categoryId = db.Column(
        BIGINT(20, unsigned=True),
        ForeignKey("Category.id")
    )

    categoryRow = relationship("Category", lazy="joined")
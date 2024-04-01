from typing import List

from sqlalchemy.orm import mapped_column, Mapped, as_declarative, declared_attr, relationship
from sqlalchemy import MetaData, String, Boolean

from currency_and_interaction import ExchangeHistory


@as_declarative()
class AbstractModel:
    metadata = MetaData

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class User(AbstractModel):
    __tablename__ = 'users'
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(30), nullable=False)
    first_name: Mapped[str | None] = mapped_column(String(30))
    last_name: Mapped[str | None] = mapped_column(String(30))
    lang_code: Mapped[str]    # user language code
    timezone: Mapped[int]
    is_bot: Mapped[bool] = mapped_column(Boolean, nullable=False)

    exchange_history: Mapped[List['ExchangeHistory']] = relationship(back_populates='user')

    def __str__(self):
        return f'User: {self.user_name}'

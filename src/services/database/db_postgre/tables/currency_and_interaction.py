import datetime

from sqlalchemy import VARCHAR, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from user import AbstractModel, User


class Currency(AbstractModel):
    __tablename__ = 'currency'
    currency_code: Mapped[str] = mapped_column(VARCHAR, unique=True, nullable=False)
    currency_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(insert_default=func.now)
    # timestamp: Mapped[datetime] = mapped_column(insert_default=text("TIMEZONE('utc', now())"))

    exchange_history: Mapped['ExchangeHistory'] = relationship(back_populates='currency')


class ExchangeHistory(AbstractModel):
    __tablename__ = 'history'
    count_currency1: Mapped[float] = mapped_column(nullable=False)
    currency_1: Mapped[str] = mapped_column(nullable=False)
    exchange_amount: Mapped[float] = mapped_column(nullable=False)
    currency_2: Mapped[str] = mapped_column(nullable=False)
    user_id_fk: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped["User"] = relationship(back_populates='exchange_history', uselist=False, lazy='joined')
    currency: Mapped["Currency"] = relationship(back_populates='exchange_history')

    def __str__(self) -> str:
        return f"ID: {self.id}, Amount: {self.exchange_amount}," \
               f" Currency 1: {self.currency_1}, Currency 2: {self.currency_2}"

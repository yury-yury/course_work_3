from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Operation:
    date: datetime
    amount: float
    currency: str
    description: str
    from_: Optional[str]
    to: str

    def __repr__(self) -> str:
        res = f"""{self.date.strftime('%d.%m.%Y')} {self.description}
{self.account_number_masking(self.from_)} -> {self.account_number_masking(self.to)}
{self.amount} {self.currency} \n"""
        return res

    @staticmethod
    def account_number_masking(value: Optional[str]) -> str:
        if value is None:
            return ''
        else:
            value_list = value.split()
            number = value_list.pop()
            result = ' '.join(value_list) + ' '
            if result == 'Счет ':
                result += '**' + number[-4:]
            else:
                result += number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
            return result
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Operation:
    """
    The Opertion class represents the data model for the operation of the application.
    Contains the necessary methods and description of data types for filling fields.
    """
    date: datetime
    amount: float
    currency: str
    description: str
    from_: Optional[str]
    to: str

    def __repr__(self) -> str:
        """
        The __repr__ function overrides the base class method Object.
        Returns its own data model instance as a formatted string when called.
        """
        res = f"""{self.date.strftime('%d.%m.%Y')} {self.description}
{self.account_number_masking(self.from_)} -> {self.account_number_masking(self.to)}
{self.amount} {self.currency} \n"""
        return res

    @staticmethod
    def account_number_masking(value: Optional[str]) -> str:
        """
        The account_number_masking function defines a static class method. It takes a string as a parameter,
        performs data parsing and returns the term with modified data that does not allow the full identification
        of personal data.
        """
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
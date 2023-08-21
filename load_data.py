import json
from datetime import datetime
from typing import List, Dict, Any

from models import Operation


def load_data(path_datafile: str) -> List[Operation]:
    with open(path_datafile, 'r', encoding='utf-8') as file:
        data_list: List[Dict[str, Any]] = json.load(file)

    result: list = []
    format = '%Y-%m-%dT%H:%M:%S.%f'

    for item in data_list:
        if item != {} and item['state'] == 'EXECUTED':
            result.append(Operation(date=datetime.strptime(item['date'], format),
                                    amount=item['operationAmount']['amount'],
                                    currency=item['operationAmount']['currency']['name'],
                                    description=item['description'],
                                    from_=item.get('from', None),
                                    to=item['to']
                                    ))
    return result

import json
from datetime import datetime
from typing import List, Dict, Any

from models import Operation


def load_data(path_datafile: str) -> List[Operation]:
    """
    The load_data function takes as a parameter the path to a JSON file as a string. When called,
    it opens a file and reads data from its contents. Forms instances of the data model from the received data
    and returns them as a list.
    """
    try:
        with open(path_datafile, 'r', encoding='utf-8') as file:
            data_list: List[Dict[str, Any]] = json.load(file)

    except FileNotFoundError:
        print(f'No such file or directory: {path_datafile}')
        data_list = []

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

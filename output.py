from typing import List, Optional

from models import Operation


def out_result(instance_list: List[Operation]) -> None:
    """
    The out_result function takes as a parameter a list of instances of the data model class.
    It sorts them and outputs the first five instances to the console.
    """
    instance_list.sort(key=lambda x: x.date, reverse=True)
    for item in instance_list[:5]:
        print(item)

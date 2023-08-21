from typing import List, Optional

# from models import Operation


def out_result(instance_list) -> None:
    instance_list.sort(key=lambda x: x.date, reverse=True)
    for item in instance_list[:5]:
        print(item)

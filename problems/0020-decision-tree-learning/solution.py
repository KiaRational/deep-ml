import math
from collections import Counter
from typing import List, Dict, Union

import math
from collections import Counter

def counter(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    attr_dict = {'attr': {}, 'target_attr': {'Yes': 0, 'No': 0}}

    for attribute in attributes:
        attr_dict['attr'][attribute] = {}

    for example in examples:
        label = example[target_attr]
        attr_dict['target_attr'][label] += 1

        for attribute in attributes:
            value = example[attribute]
            if value not in attr_dict['attr'][attribute]:
                attr_dict['attr'][attribute][value] = {'num': 0, 'Yes': 0, 'No': 0}
            attr_dict['attr'][attribute][value]['num'] += 1
            attr_dict['attr'][attribute][value][label] += 1

    return attr_dict

def entropy_calc(target_attr_dict):
    total = target_attr_dict['Yes'] + target_attr_dict['No']
    if total == 0:
        return 0.0
    entropy = 0.0
    for label in targ
import json

import pandas as pd
from pandas import DataFrame
from pydantic import ValidationError
from typing import Optional

from pydantic._internal._model_construction import ModelMetaclass


def read_excel(file_path: str, sel_rows: Optional[list] = None) -> DataFrame:
    df = pd.read_excel(file_path).fillna(" ")
    if sel_rows:
        return df[sel_rows]
    return df


def pricelist_to_json(data_frame: DataFrame, schema: ModelMetaclass) -> list:
    content = []
    count_errors = 0

    for i in range(len(data_frame) - 1):
        row = json.dumps(data_frame.loc[i].to_dict())

        try:
            data = schema.model_validate_json(row).model_dump()
            content.append(data)
        except ValidationError:
            count_errors += 1
            pass

    print(f'Выгружено {len(content)} товаров')
    print(f'Ошибок {count_errors}')

    return content

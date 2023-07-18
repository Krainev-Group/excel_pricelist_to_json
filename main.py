import json
import pandas as pd
from pandas import DataFrame
from schemas import SItem
from pydantic import ValidationError

"""
[
    {
     "Images":{"Link":"STR","Width":X,"Height":Y},
     "Dimensions":{"Width":X,"Height":Y,"Depth":Z}, 
     "Category":STR,
     "Warranty":INT,
     "UPC":STR,
     "Vendor":STR,
     "Name":STR,
     "Article":STR,
     "Description":STR,
     "Price":FLOAT
    }
]
"""


def pricelist_to_json(data_frame: DataFrame,) -> list:
    content = []
    count_errors = 0

    for i in range(len(data_frame) - 1):
        row = json.dumps(data_frame.loc[i].to_dict())

        try:
            data = SItem.model_validate_json(row).model_dump()
            content.append(data)
        except ValidationError as e:
            count_errors += 1
            pass

    print(f'Выгружено {len(content)} товаров')
    print(f'Ошибок {count_errors}')

    return content


if __name__ == "__main__":
    excel_file = 'excel/price.xlsx'

    df = pd.read_excel(excel_file).fillna(' ')[[
        'Номер товара', 'Каталог',
        'Код товара', 'Наименование',
        'Гарантия', 'Наличие', 'Дилер3'
    ]]

    with open('price.json', 'w', encoding='utf8') as f:
        json.dump(pricelist_to_json(df), f, ensure_ascii=False, indent=1)

import json

from service import read_excel, pricelist_to_json

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


if __name__ == "__main__":

    excel_file = 'excel/price.xlsx'
    data = read_excel(
        file_path=excel_file,
        sel_rows=[
            # 'Номер товара', 'Каталог',
            # 'Код товара', 'Наименование',
            # 'Гарантия', 'Наличие', 'Дилер3'
        ],
    )

    with open('price.json', 'w', encoding='utf8') as f:
        json.dump(pricelist_to_json(data), f, ensure_ascii=False, indent=1, separators='.')

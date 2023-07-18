from pydantic import BaseModel, Field
from typing import Optional, Literal

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


class SItem(BaseModel):
    Images: Optional[dict] = Field(
        alias="Фото",
        default={"Link": " ", "Width": 0, "Height": 0, }
    )
    Dimensions: Optional[dict] = Field(
        alias="Габариты",
        default={"Width": 0, "Height": 0, "Depth": 0, }
    )
    Category: Optional[str] = Field(alias="Каталог", default='')
    Warranty: Optional[str] = Field(alias='Гарантия', default='')
    UPC: Optional[str] = Field(alias='ШК', default='')
    Vendor: Optional[str] = Field(alias='Вендор', default='')
    Name: str = Field(alias="Наименование")
    Article: str = Field(alias="Код товара")
    Description: Optional[str] = Field(alias='Описание', default='')
    Stock: Optional[int] = Field(alias='Наличие', default=0)
    Price: Optional[float] = Field(alias='Дилер3', default=0)


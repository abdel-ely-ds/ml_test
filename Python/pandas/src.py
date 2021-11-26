import pandas as pd
from typing import List, Tuple, Dict
from constants import (
    CATEGORY,
    PRODUCT_ID,
    PRODUCT_ID_DATA_IMPACT,
    PRICE,
    PATH_2,
    PATH1_2,
    PATH1_1,
)


def pre_process_category(s: pd.Series) -> pd.Series:
    return s.str.replace("Promotions", "promo")


def read_file(path: str, sep: str = ";") -> pd.DataFrame:
    return pd.read_csv(path, compression="gzip", sep=sep)


def import_raw_data(
    path1_1: str = PATH1_1, path1_2: str = PATH1_2, path2: str = PATH_2
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    # read the files
    df1_1 = read_file(path1_1)
    df1_2 = read_file(path1_2)
    df2 = read_file(path2, sep=",")

    # pre process
    df1_1[CATEGORY] = pre_process_category(df1_1[CATEGORY])
    df1_2[CATEGORY] = pre_process_category(df1_2[CATEGORY])
    df2.rename(columns={"pe_ref_in_enseigne": PRODUCT_ID}, inplace=True)

    # cast type (some ids in df2 contain --)
    df1_1[PRODUCT_ID] = df1_1[PRODUCT_ID].astype(str)
    df1_2[PRODUCT_ID] = df1_2[PRODUCT_ID].astype(str)

    return df1_1.merge(df2, on=PRODUCT_ID), df1_2.merge(df2, on=PRODUCT_ID)


def average_prices(df_1: pd.DataFrame, df_2: pd.DataFrame) -> Dict[str, float]:
    df_all = pd.concat([df_1, df_2])

    return df_all.groupby(PRODUCT_ID_DATA_IMPACT)[PRICE].mean().round(2).to_dict()


def list_unique_products_by_categories_by_df(df: pd.DataFrame) -> Dict[str, List[str]]:
    return df.groupby(CATEGORY)[PRODUCT_ID_DATA_IMPACT].unique().to_dict()

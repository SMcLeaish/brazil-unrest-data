import unicodedata
import polars as pl

def strip_accents(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(c)
    )

def clean_column(df: pl.DataFrame, col: str, alias: str|None) -> pl.DataFrame:
        alias = alias or col
        return df.with_columns(
            pl.col(col).map_elements(
            strip_accents,
            return_dtype=pl.Utf8)
            .str.strip_chars()
            .str.to_lowercase()
            .alias(alias))
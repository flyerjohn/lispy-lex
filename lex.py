import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    token_lexemas = [
        ("STRING", r"\".*\""),
        ("NUMBER", r"(\+|\-|)\d+(\.\d*)?"),
        ("NAME", r"([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*"),
        ("CHAR", r"#\\[a-zA-Z]*"),
        ("QUOTE", r"\'"),
        ("LPAR", r"\("),
        ("RPAR", r"\)"),
        ("BOOL", r"#[t|f]")
    ]
    

    return [Token('INVALIDA', 'valor inválido')]
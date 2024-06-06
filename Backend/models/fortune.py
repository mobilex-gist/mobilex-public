from typing import Literal

from pydantic import BaseModel, Field

MAX_LENGTH = 20


class InputModel(BaseModel):
    word: str = Field(
        alias='word',
        description='태어난 날짜를 입력해주세요!',
        default='2000.10.30',
        max_length=MAX_LENGTH
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='사주팔자 결과물',
    )

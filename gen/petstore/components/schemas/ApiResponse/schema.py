# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class ApiResponse(lapidary.runtime.ModelBase):
    code: typing.Union[None, int] = None

    type: typing.Union[None, str] = None

    message: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
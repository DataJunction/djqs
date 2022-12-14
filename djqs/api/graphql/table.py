"""
Models for tables.
"""

# pylint: disable=too-few-public-methods

from typing import TYPE_CHECKING, List

import strawberry
from typing_extensions import Annotated

from djqs.api.graphql.column import Column
from djqs.api.graphql.node import Node
from djqs.models.table import Table as Table_
from djqs.models.table import TableColumns as TableColumns_


@strawberry.experimental.pydantic.type(model=TableColumns_, all_fields=True)
class TableColumns:
    """
    Join table for table columns.
    """


if TYPE_CHECKING:
    from djqs.api.graphql.database import Database


@strawberry.experimental.pydantic.type(
    model=Table_,
    fields=["id", "node_id", "database_id"],
)
class Table:
    """
    A table with data.

    Nodes can store data in multiple tables, in different databases.
    """

    node: Node
    database: Annotated["Database", strawberry.lazy("djqs.api.graphql.database")]
    columns: List[Column]

from typing import TypeAlias, Protocol

from airtask.entities import Task

ParamKey: TypeAlias = str
ParamValue: TypeAlias = str | int | float | bool
ProtocolName: TypeAlias = str
ProtocolImplName: TypeAlias = str
DependentTaskName: TypeAlias = str
ProtocolCollection = dict[type[Protocol], list[type[Task]]]

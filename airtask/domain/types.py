from typing import TypeAlias, Protocol

from airtask.domain.entities import Task

ParamKey: TypeAlias = str
ParamValue: TypeAlias = str | int | float | bool
ProtocolName: TypeAlias = str
ProtocolImplName: TypeAlias = str
DependentTaskName: TypeAlias = str
ProtocolCollection = dict[type[Protocol], dict[ProtocolImplName, type[Task]]]

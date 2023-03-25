from typing import TypeAlias, Protocol

from airtask.domain.models import Task

ParamKey: TypeAlias = str
ParamValue: TypeAlias = str | int | float | bool
ProtocolName: TypeAlias = str
TaskName: TypeAlias = str
DependentTaskName: TypeAlias = str
ProtocolCollection = dict[type[Protocol], dict[TaskName, type[Task]]]

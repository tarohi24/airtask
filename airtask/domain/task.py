from airtask.domain.entities import TaskImplConfig, TaskGraph
from airtask.domain.exceptions import ProtocolNotFound, ProtocolImplNotFound
from airtask.domain.types import ProtocolName, ProtocolCollection


def generate_task_graph(
    root_protocol_name: ProtocolName,
    root_config: TaskImplConfig,
    task_collection: ProtocolCollection,
) -> TaskGraph:
    try:
        root_task_protocol = task_collection[root_protocol_name]
    except KeyError:
        raise ProtocolNotFound(f"Protocol {root_protocol_name} is not found.")
    try:
        root_impl_class = root_task_protocol[root_config.impl_name]
    except KeyError:
        raise ProtocolImplNotFound(
            f"Protocol {root_protocol_name} does not have implementation {root_config.impl_name}."
        )

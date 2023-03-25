import datetime
from dataclasses import dataclass

from airflow import DAG
from airflow.utils.state import DagRunState
from airflow.utils.types import DagRunType

from airtask.domain.logics import TaskFlowManager, TaskFlow
from airtask.domain.models import TaskImplConfig, Task


@dataclass
class AirflowTask(Task):

    def run(self) -> None:
        pass


@dataclass
class AirflowTaskFlow(TaskFlow):
    dag: DAG
    exec_start_datetime: datetime.datetime

    def execute(self) -> None:
        self.dag.create_dagrun(
            state=DagRunState.RUNNING,
            execution_date=self.exec_start_datetime,
            run_type=DagRunType.MANUAL,
        )


class AirflowTaskFlowManager(TaskFlowManager):
    def generate_flow(self, root_config: TaskImplConfig) -> TaskFlow:
        pass
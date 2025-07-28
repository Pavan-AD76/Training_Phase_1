from airflow.models.baseoperator import BaseOperator
from airflow.plugins_manager import AirflowPlugin

class GreetOperator(BaseOperator):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        print(f"Hello from your custom operator, {self.name}!")

class GreetPlugin(AirflowPlugin):
    name = "greet_plugin"
    operators = [GreetOperator]

from dataclasses import dataclass
from datetime import datetime
from typing import Callable

@dataclass
class TextTaskData:
    body: str
    current_state: str | None = None
    time: datetime = datetime.utcnow()

def make_text_task(make_prompt: Callable[[TextTaskData], str]):
    def text_task(task_data: TextTaskData, )
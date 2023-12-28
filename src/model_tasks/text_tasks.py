from dataclasses import dataclass
from datetime import datetime
from typing import Callable

@dataclass
class TextTaskData:
    body: str
    current_state: str | None = None
    time: datetime = datetime.utcnow()

@dataclass
class TextModel:
    model_name: str
    max_tokens: int

def make_text_task(make_prompt: Callable[[TextTaskData], str], text_model):
    def text_task(task_data: TextTaskData, ):
        prompt = make_prompt(task_data)
        

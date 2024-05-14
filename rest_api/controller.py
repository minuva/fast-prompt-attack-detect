import logging

from typing import Dict, Union
from fastapi import APIRouter
from rest_api.schema import TaskInput
from rest_api.attacks import get_user_agent_attack


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/conversation_prompt_attack_plugin", response_model=Dict[str, Union[str, int, float]])
async def task_attacks(request: TaskInput):
    return get_user_agent_attack(request.llm_input, request.llm_output)

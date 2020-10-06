from fastapi import Header, HTTPException
from core.config import get_settings
from resources import strings

settings = get_settings()


async def has_permission(x_requester_id: str = Header(...)):
    if x_requester_id not in settings.valid_requestor_ids:
        raise HTTPException(status_code=400, detail=strings.INVALID_REQUESTER_ID)

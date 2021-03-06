from typing import Optional

from fastapi import HTTPException, Security

from resources import strings
from fastapi.security.api_key import APIKeyHeader

from core import settings

key_header_requester_id = APIKeyHeader(name="requester-id", scheme_name="Requestor-Id")
key_head_correlation_id = APIKeyHeader(name="correlation_id", scheme_name="Correlation-Id", auto_error=False)
key_header_root_correlation_id = APIKeyHeader(name="root_correlation_id", scheme_name="Root-Correlation-Id",
                                              auto_error=False)


class CatalogAPIBasePermission:
    _white_list = [
        settings.REQUESTER_ID_TEST,
    ]
    perms = []

    def __call__(self, requester_id: str = Security(key_header_requester_id),
                 correlation_id: Optional[str] = Security(key_head_correlation_id),
                 root_correlation_id: Optional[str] = Security(key_header_root_correlation_id)):
        if settings.DEBUG is True and requester_id not in self._white_list:
            raise HTTPException(status_code=403, detail=strings.INVALID_REQUESTER_ID)
        elif settings.DEBUG is False and requester_id not in self.perms:
            raise HTTPException(status_code=403, detail=strings.INVALID_REQUESTER_ID)

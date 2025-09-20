import logging
import traceback
from urllib.request import Request

from config.logger.request_log import RequestInfo, RequestLog, ErrorLog

logger = logging.getLogger(__name__)

def log_request(request: Request):
    request_info = RequestInfo(request)
    request_log = RequestLog(
        req_id=request.state.request_id,
        method=request_info.method,
        route=request_info.route,
        ip=request_info.ip,
        url=request_info.url,
        host=request_info.host,
        body=request_info.body,
        headers=request_info.headers,
    )

    logger.info(request_log.model_dump())

def log_error(uuid: str, response_body: dict):
    error_log = ErrorLog(
        req_id= uuid,
        error_message=response_body["error_message"],
    )
    # logger.info("log fields")
    logger.error(error_log.model_dump())
    return error_log.model_dump()
    # logger.info(traceback.format_exc())
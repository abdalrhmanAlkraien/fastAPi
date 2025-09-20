import json
import time
import traceback
import uuid

from fastapi import HTTPException, FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from config.logger.log import log_request, log_error
import logging

def setup_middlewares(app: FastAPI):

    @app.middleware("http")
    async def log_middleware(request:Request, call_next):

        logging.info("log_middleware_app")
        req_id = str(uuid.uuid4())
        start_time = time.time()
        try:
            request.state.request_id = req_id
            request.state.body = json.loads(await request.body() or "{}")
        except Exception as ex:
            logging.error(ex)
            request.state.body = "{}"
        log_request(request)
        try:
            response = await call_next(request)
            status_code = response.status_code

            if hasattr(response, "body_iterator"):
                body_content = [chunk async for chunk in response.body_iterator]
                body_byte = b"".join(body_content).decode("utf-8")

                try:
                    body_content = json.loads(body_byte)
                except json.JSONDecodeError:
                    logging.error("Failed to decode body content in response")
                    body_content = body_byte
            else:
                body_content = response.body.decode("utf-8") if hasattr(response, "body") else None

            response = {
                "statusCode": "success" if status_code < 400 else "error",
                "time": time.time() - start_time,
                "body": body_content,
            }
            return JSONResponse(status_code=status_code, content=response)
            # if response.headers.get("content-type") == "application/json":
            #     log.debug(response)
            #     response_body = [chunk async for chunk in response.body]
            #     response.body_iterator = iterate_in_threadpool(iter(response_body))
        except HTTPException as e:
            logging.error(e)
            log_error(req_id, {"error_message": e.detail})
            raise e
        except Exception as e:
            logging.error(traceback.format_exc())
            response = log_error(req_id, {"error_message": e.__str__()})
            return JSONResponse(status_code=500, content=response)

    @app.exception_handler(HTTPException)
    async def handle_http_exception(request: Request, exc: HTTPException):
        req_id = getattr(request.state, "request_id", "unknown")
        response = log_error(req_id, {"error_message": exc.__str__()})
        return JSONResponse(status_code=exc.status_code, content=response)


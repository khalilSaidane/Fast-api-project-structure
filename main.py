import uvicorn
from fastapi import FastAPI, Depends
from core.config import get_settings
from api.routers.api import api_router
settings = get_settings()


def get_application():
    application = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version=settings.version,
    )

    # application.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=ALLOWED_HOSTS or ["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    #
    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))
    #
    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.include_router(api_router, prefix=settings.prefix)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

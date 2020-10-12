import uvicorn
from fastapi import FastAPI
from api.routers.api import api_router
from core import settings


def get_application():
    application = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
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
    application.include_router(api_router, prefix=settings.PREFIX)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

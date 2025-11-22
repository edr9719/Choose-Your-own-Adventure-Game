# FastAPI definition
from core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Initializes a FastAPI application instance. ASGI application (Asynchronous Server Gateway Interface).
app = FastAPI(
    title="Choose Your own Adventure Game API",
    description="API to generate cool stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
# “Add CORS headers to every response so browsers don’t block cross-origin requests.”
app.add_middleware(
    CORSMiddleware,  # CORS allows us to access FastAPI from different locations
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Only run this code when the file is launched directly, not when it’s imported as a module.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

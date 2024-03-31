from fastapi import Request , Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from authentication import get_current_user, translate_method_to_action, has_permission
import json

# loading fake data
data = json.load(open('data.json'))

# For this path authorization not needed
EXCLUDED_PATHS = data['excluded_paths']

# Define a custom Middleware for handling RBAC
class ResourceBaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_method = str(request.method).upper()
        action = translate_method_to_action(request_method)
        resource = request.url.path[1:]
        if resource not in EXCLUDED_PATHS:
            # Extract user role from token
            token = request.headers.get("Authorization").split(" ")[1]
            user = await get_current_user(token)
            if user is None:
                return JSONResponse(content={"error": "Invalid token"}, status_code=401)
            user_role = user['role']
            if not has_permission(user_role, resource, action):
                return JSONResponse(content={"error": "Insufficient permissions"}, status_code=403)
        response = await call_next(request)
        return response
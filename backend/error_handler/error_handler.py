BAD_REQUEST_MSG = "General error pls refresh the page"
TOKEN_ERROR_MSG = "Invalid token"
ORGANIZATION_NAME = "Invalid organization name"
VCS_TYPE = "Invalid version system control type"

def post_request(client_data: dict):
    if client_data == None:
        raise ValueError(BAD_REQUEST_MSG)
    if not isinstance(client_data["token"], str):
        raise TypeError(TOKEN_ERROR_MSG)
    if not isinstance(client_data["organization"], str):
        raise TypeError(ORGANIZATION_NAME)
    if not isinstance(client_data["vcs_type"], str):
        raise TypeError(VCS_TYPE)

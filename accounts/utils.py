
def jwt_response_payload_handler(token, user=None, request=None):
    print('ssssssssssssssssss')
    return{
        'token': token,
        'user': user.username,
    }

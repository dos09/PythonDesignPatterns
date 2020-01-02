"""
Chain of handlers, each doing something (processing request), 
if ok pass to next handler, else stop processing (break the chain)

Example:
    Client makes request to view file. Handlers used:
    1. Check if the client logged in
    2. Check if the client has permissions
    3. Validate request
    4. Get requested file 
    (1 -> 2 -> 3 -> 4)
"""


class User:

    def __init__(self, name, logged_in=False, permission_level=1):
        self.name = name
        self.logged_in = logged_in
        self.permission_level = permission_level


class Request:

    def __init__(self, file_name, permission_level):
        self.file_name = file_name
        self.permission_level = permission_level


class Response:

    def __init__(self, err_msg=None, data=None):
        self.err_msg = err_msg
        self.data = data

    def __str__(self):
        return 'ERR: %s, DATA: %s' % (self.err_msg, self.data)


class Handler:

    def __init__(self):
        self.next_handler = None

    def handle(self, user, request):
        raise NotImplementedError()


class LogChecker(Handler):

    def handle(self, user, request):
        if user.logged_in:
            return self.next_handler.handle(user, request)

        return Response(err_msg='User "%s" is not logged in' % user.name)


class PermissionsChecker(Handler):

    def handle(self, user, request):
        if user.permission_level >= request.permission_level:
            return self.next_handler.handle(user, request)

        return Response(
            err_msg=('User "%s" does not have permissions to view this file' %
                     user.name)
        )


class RequestValidator(Handler):

    def handle(self, user, request):
        if self._file_exists(request.file_name):
            return self.next_handler.handle(user, request)

        return Response(err_msg='File "%s" not found' % request.file_name)

    def _file_exists(self, file_name):
        return 'fake' not in file_name


class FileGetter(Handler):

    def handle(self, user, request):
        return Response(data=request.file_name)


def _get_request_handler():
    log_checker = LogChecker()
    perm_checker = PermissionsChecker()
    request_validator = RequestValidator()
    file_getter = FileGetter()

    log_checker.next_handler = perm_checker
    perm_checker.next_handler = request_validator
    request_validator.next_handler = file_getter

    return log_checker


def run():
    user_x = User(name='user X', logged_in=False)
    user_no_perm = User(name='user no perm', logged_in=True)
    user_fake_file = User(name='user fake file', logged_in=True,
                          permission_level=3)
    user_ok = User(name='user ok', logged_in=True, permission_level=3)
    request_fake = Request(file_name='fake file', permission_level=2)
    request_ok = Request(file_name='banana.txt', permission_level=2)

    request_handler = _get_request_handler()
    print(request_handler.handle(user_x, request_fake))
    print(request_handler.handle(user_no_perm, request_fake))
    print(request_handler.handle(user_fake_file, request_fake))
    print(request_handler.handle(user_ok, request_ok))


if __name__ == '__main__':
    run()

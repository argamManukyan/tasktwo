class MethodNotAllowedException(Exception):
    """ We handled the exception which is response from given endpoint,when i did sent call"""
    pass


class JSONDecodeCustomError(Exception):
    """ This exception we get when called client.send api  """
    pass

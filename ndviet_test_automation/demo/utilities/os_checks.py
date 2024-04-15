import platform


def get_os_name():
    return platform.system()


def assert_os_name(expected_os_name):
    os_name = get_os_name()
    assert (os_name == expected_os_name)


def get_os_version():
    return platform.version()


def get_os_release():
    return platform.release()


def get_os_architecture():
    return platform.architecture()


def get_os_machine():
    return platform.machine()


def get_os_processor():
    return platform.processor()


def get_os_platform():
    return platform.platform()


def get_os_uname():
    return platform.uname()


def get_os_system():
    return platform.system()


def get_os_node():
    return platform.node()

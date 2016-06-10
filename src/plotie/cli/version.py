import pkg_resources

_top_level_module = __package__.split(".")[0]


def get_version():
    """Get the version number of this application.

    :rtype: str
    """
    return pkg_resources.get_distribution(_top_level_module).version or "0.0.0"

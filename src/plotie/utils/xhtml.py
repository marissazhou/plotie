from lxml.html import XHTMLParser, XHTML_NAMESPACE

xhtml_parser = XHTMLParser(resolve_entities=False)


def get_content_by_xpath(element, query, prefix="x", *args, **kwargs):
    """
    Get document elements by xpath.

    The xpath query should use the appropriate prefix, e.g.

        >>> asset = Statutecomponent.objects.all()[0]
        >>> asset.xpath("/x:html/x:body")
        [<Element {http://www.w3.org/1999/xhtml}body at 0x2b3df4be2878>]

    :param element: a document Element
    :param path: the XPath query statement
    :param prefix: the namespace prefix
    :param args: additional arguments to pass to the element's xpath method
    :param kwargs: additional keyword-arguments to pass to the element's
        xpath method
    :returns: a list of matching elements
    :rtype: list
    """
    kwargs.setdefault("namespaces", dict([(prefix, XHTML_NAMESPACE)]))
    return element.xpath(query, *args, **kwargs)


def replace_amp(stream):
    # namedentities does not convert the ampersand intentionally, so we
    # do it manually (SSR-1185)
    return stream.replace("&amp;", "&#38;")

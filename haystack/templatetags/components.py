from typing import Any

from django.contrib.messages.storage.base import BaseStorage
from django.template import Library, TemplateSyntaxError
from django.template.base import Parser, Token, Node, NodeList
from django.contrib.messages.constants import DEFAULT_LEVELS

register = Library()


@register.tag(name='capture')
def capture(parser: Parser, token: Token):
    bits = token.contents.split()
    if len(bits) > 2:
        raise TemplateSyntaxError(f"'capture' tag got unexpected arguments {bits[2:]!r}")
    name: str = bits[1]
    if "'" in name or '"' in name:
        raise TypeError(f"'capture' tag got a quoted name {name}. use a name without quotes")
    nodelist = parser.parse(parse_until=['endcapture'])
    parser.delete_first_token()
    return CaptureNode(name=name, nodelist=nodelist)


class CaptureNode(Node):
    def __init__(self, *, name: str, nodelist: NodeList):
        self.name = name
        self.nodelist = nodelist

    def render(self, context):
        context[self.name] = self.nodelist.render(context)
        return ''


@register.inclusion_tag('components/flash_messages.html', name='flash_messages')
def flash_messages_component(*, messages: BaseStorage) -> dict[str, Any]:
    return dict(
        messages=messages,
        DEFAULT_MESSAGE_LEVELS=DEFAULT_LEVELS,
    )
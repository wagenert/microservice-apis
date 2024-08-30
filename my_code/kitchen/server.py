import random
import string

from ariadne import make_executable_schema, QueryType
from ariadne.asgi import GraphQL

query = QueryType()


@query.field('hello')
def resolve_hello(*_):
    return ''.join(
        random.choice(string.ascii_letters) for _ in range(10)
    )


schema = '''
    type Query {
        hello: String
    }
'''

server = GraphQL(make_executable_schema(schema), debug=True)

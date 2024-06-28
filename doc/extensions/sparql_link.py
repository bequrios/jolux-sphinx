from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import nested_parse_with_titles
import urllib.parse

class SparqlQueryNode(nodes.General, nodes.Element):
    pass

def visit_sparql_query_node_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='sparql-query'))
    self.body.append('<pre><code>')

def depart_sparql_query_node_html(self, node):
    self.body.append('</code></pre>')
    query = node['query'].replace('\n', ' ').strip()
    endpoint = 'https://fedlex.data.admin.ch/sparql'
    
    url_params = {
        'query': query,
        'contentTypeConstruct': 'text/turtle',
        'contentTypeSelect': 'application/sparql-results+json',
        'endpoint': '/sparqlendpoint',
        'requestMethod': 'POST',
        'tabTitle': 'Query',
        'headers': '{}',
        'outputFormat': 'table'
    }
    
    url = f"{endpoint}#{urllib.parse.urlencode(url_params)}"
    
    link_html = f'<a href="{url}" target="_blank">Execute Query</a>'
    self.body.append(link_html)
    self.body.append('</div>')

class SparqlQueryDirective(SphinxDirective):
    has_content = True

    def run(self):
        query = '\n'.join(self.content)
        node = SparqlQueryNode(query=query)
        self.add_name(node)
        nested_parse_with_titles(self.state, self.content, node)
        return [node]

def setup(app):
    app.add_node(SparqlQueryNode, html=(visit_sparql_query_node_html, depart_sparql_query_node_html))
    app.add_directive('sparql-query', SparqlQueryDirective)

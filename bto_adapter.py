import os
import json
from rdflib import Graph
from rdflib.namespace import RDF, RDFS, OWL


class BTOAdapter:
    def __init__(self, write_properties=False, add_provenance=False, filepath=None):
        self.write_properties = write_properties
        self.add_provenance = add_provenance
        self.filepath = filepath
        self.graph = Graph()

        if filepath:
            self.load_graph_from_owl(filepath)

    def load_graph_from_owl(self, filepath):
        self.graph.parse(filepath, format='xml')

    def get_nodes(self):
        for s, p, o in self.graph.triples((None, RDF.type, OWL.Class)):
            yield {
                'id': str(s),
                'name': str(self.graph.value(s, RDFS.label)),
                'properties': {str(p): str(o) for p, o in
                               self.graph.predicate_objects(s)} if self.write_properties else {}
            }

    def get_edges(self):
        for s, p, o in self.graph.triples((None, None, None)):
            if isinstance(o, (Graph,)):
                continue
            yield {
                'source': str(s),
                'predicate': str(p),
                'target': str(o)
            }

    def write_output(self, nodes, edges):
        with open('nodes.metta', 'w') as node_file:
            for node in nodes:
                node_file.write(f'({node["id"]} {node["name"]} {json.dumps(node["properties"])})\n')

        with open('edges.metta', 'w') as edge_file:
            for edge in edges:
                edge_file.write(f'({edge["source"]} {edge["predicate"]} {edge["target"]})\n')


# Sample usage
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    adapter = BTOAdapter(write_properties=True, add_provenance=True, filepath='BTO.owl')
    nodes = list(adapter.get_nodes())
    edges = list(adapter.get_edges())
    adapter.write_output(nodes, edges)

    print("Nodes and edges have been written to nodes.metta and edges.metta")

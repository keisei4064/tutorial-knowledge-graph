from pathlib import Path

from rdflib import Dataset
from rdflib.namespace import RDF

g = Dataset()
g.parse(Path(__file__).parent / "multi_graphs_example.trig")

for s, p, o, ng in g.quads((None, RDF.type, None, None)):
    print(s, " | ", ng)

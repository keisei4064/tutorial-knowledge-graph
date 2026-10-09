from pathlib import Path

from rdflib import Graph

g = Graph()
g.parse("http://www.w3.org/People/Berners-Lee/card")
g.serialize(destination=Path(__file__).parent / "tbl.ttl")

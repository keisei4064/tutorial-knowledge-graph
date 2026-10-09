from rdflib import Graph
from rdflib.query import ResultRow

# Create a Graph, parse in Internet data
g = Graph().parse("http://www.w3.org/People/Berners-Lee/card")

# Query the data in g using SPARQL
# This query returns the 'name' of all `foaf:Person` instances
q = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT ?name
    WHERE {
        ?p rdf:type foaf:Person .

        ?p foaf:name ?name .
    }
"""

# Apply the query to the graph and iterate through results
for r in g.query(q):
    print(r)
    
    # print(r["name"])  # 動くが、RDFLib の型定義では文字列キーの添字アクセスが認識されず Pylance 警告になる
    if isinstance(r, ResultRow):
        print(r[0])

# prints: Timothy Berners-Lee

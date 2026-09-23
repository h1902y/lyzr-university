# Build a Knowledge Graph

*Lesson 02 · Ground in Knowledge — Studio: Knowledge Graph & Semantic Model*

## What you'll learn

- Set up a Neo4j Aura Graph Database instance and extract its connection credentials (URI, username, password).
- Connect a Neo4j Graph Database to Lyzr Studio under Data Connections.
- Create a new Knowledge Graph in Studio and ingest unstructured text documents to automatically extract entities and relationships.
- Test knowledge graph retrieval and visualize the compiled graph directly inside the Studio interface.
- Configure retrieval strategies like basic similarity, MMR (Maximal Marginal Relevance), or Hyde (Hypothetical Document Embeddings).

## Key concepts

**A Knowledge Graph in Studio requires a connected graph database like Neo4j.** Under the hood, Lyzr writes structural graph data to Neo4j. Users can bring their own hosted databases, such as Neo4j Aura (which has a free tier), to store these graphs.

**Lyzr automates entity and relationship extraction during document ingestion.** When a document is added to a Knowledge Graph, Lyzr reads the text, extracts key entities (things) and relationships (how they connect), and constructs the Neo4j graph nodes and edges automatically.

**The graph database is an overlay, not a replacement for traditional RAG.** A Knowledge Graph still supports passage retrieval for standard queries. The graph exists as an extra intelligence layer to answer connection-heavy questions.

**Visualizing the graph helps verify the relationships extracted from your documents.** The "Visualize Knowledge Graph" option in Studio renders your knowledge as a cluster map, letting you see dots (entities) and lines (relationships) that were parsed from the raw text.

**Retrieval behavior can be customized using different retrieval algorithms.** You can stick to defaults or toggle between similarity search, MMR (for diverse result sets), and Hyde (for generating hypothetical query-answers first).

## In Studio

Studio feature: **Connections → Data Connections** and **Build → Knowledge → Knowledge Graph**. Here's how to build, connect, and visualize a knowledge graph:

1. Go to **Connections**, click **Data Connections**, and choose **Add Connection**. Select **Neo4j**, paste your connection URI, username, and password, and save.
2. Go to **Build** and open the **Knowledge** screen. Click the **Knowledge Graph** tab.
3. Click **New Graph**, name it, choose your connected Neo4j database, and click **Create**.
4. Inside your new graph, click **Add Document** and upload a text file. Wait for the graph builder to read, parse, and write nodes to Neo4j (takes 1–2 minutes).
5. Open the retrieval tester drawer on the right to run test queries. Adjust search behaviors (Similarity, MMR, Hyde) under **Configure** if needed.
6. Click **Visualize Knowledge Graph** to open the interactive node-and-link map.

## Try this

1. Create a free Neo4j AuraDB instance, save the credentials, and hook it up to Lyzr Studio.
2. Upload a simple policy text document into your new Knowledge Graph in Studio. Open **Visualize Knowledge Graph** and trace the connection between two concepts (e.g., a warranty and its exclusion rules).
3. Try toggling between Similarity, MMR, and Hyde in the configuration drawer. Run the same test query and compare the retrieved passages.

## Transcript

Some of the most valuable knowledge isn't in the words, it's in the connections. Which return condition gets which refund? Which product falls under which warranty? Today we build a knowledge graph in Lyzr on a real graph database, and then we look at it, literally. First, the prerequisite. A knowledge graph needs a graph database, and here you bring your own. Neo4j's cloud service, Aura, has a free tier that's perfect for trying this. I create an instance and grab three things: the connection URI, the username, and the password. Here in Lyzr under connections and data connections, I add a Neo4j GraphDB credential and paste those details in. This is a one-time setup. Every knowledge graph I build can now write to that database. Now the graph itself. On the knowledge page, I hit new, and instead of a basic knowledge base, I pick graph. I name it, point it at the Neo4j connection, and create. And here's the part that matters. When I add a document, Lyzr doesn't just chunk it into passages. It reads it, pulls out the entities, the things in your world, and the relationships between them, and then it writes that whole structure into Neo4j. This takes a minute or two because it's genuinely building a graph and not just indexing text. While we're here, the drawer has a built-in retrieval tester. I ask about the return policy for open items, and it comes back with the exact passage from the help doc that answers it. So everything a normal knowledge base does still works. The graph is a layer on top, not a trade-off. Under configure, you can also tune how retrieval behaves: basic similarity search, MMR if you want more diverse results, or Hyde, which generates a hypothetical answer first and searches with that. Defaults are fine for us. And here's the button this whole video builds toward: Visualize Knowledge Graph. Notice it wasn't there when the graph was empty. It opens once your documents are in. And here it is, your knowledge as a map. Every dot is an entity the system extracted on its own, and every line is a relationship it found. You can see the clusters from around the concept in the document: Warranty coverage over here with the exclusions connected right next to it, express shipping with its conditions, even recovery requests for lost packages. Nobody modeled this by hand. It came out of one text file, and this picture is why graphs exist. A flat pile of chunks simply cannot show you this. So knowledge bases find the right passage. Knowledge graphs map how things connect. Next up, the third shape of knowledge: real tables, real numbers, and an agent that queries them. I'm Felipe. I'll see you there.

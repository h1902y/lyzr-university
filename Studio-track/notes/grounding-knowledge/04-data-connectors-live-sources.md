# Data Connectors as live sources

*Lesson 04 · Knowledge & RAG*

## What you'll learn

- Decide between three grounding patterns — a plain upload, a live source, and a data connector — based on how your data behaves
- Point an agent at your own infrastructure (Qdrant, Weaviate, PostgreSQL, Neo4j, MySQL) so the data never leaves your systems
- Set up a live source from a website, Google Drive, or SharePoint so the knowledge base re-syncs itself when the content changes
- Recognise why a hand-uploaded document is a frozen snapshot, and when that becomes a liability

## Key concepts

**A plain upload is a snapshot — frozen the moment you add it — so it only fits content that never changes.** Everything you've put into a knowledge base so far was uploaded by hand, which is perfectly fine for documents that stay still. The limitation shows the instant the underlying content moves on: the agent keeps answering from the version you happened to upload, not the current one.

**Data connectors let Lyzr read from your own stores and databases instead of moving the data into Lyzr.** Many teams already run their own infrastructure and want their data to stay in it. The Connections page lets you link your own vector store — Qdrant, Weaviate, PostgreSQL, or Neo4j — or connect a database directly such as PostgreSQL or MySQL. The point is control: your data stays in your systems, on your terms, and Lyzr reads from it.

**Connecting a data source is just a credential form — your host, your keys, and you're linked.** There's no data migration and no copying; you supply connection details and Lyzr reaches into the store you already own. Treat those credentials with care, since the whole connection rides on them.

**A live source stays connected, so when the underlying content changes your knowledge base updates itself in the background.** This is the opposite of a frozen upload. Because the source re-syncs on its own, your agent is always answering from the current version without anyone re-uploading anything. The available live-source options are a website, Google Drive, and SharePoint.

**Match the grounding method to the data: plain upload for fixed documents, live source for content that changes, connector when the data should stay in your own systems.** That single rule covers the whole spectrum — a knowledge base you maintain by hand versus one that maintains itself versus one that never leaves your infrastructure. Choosing well up front saves you from stale answers and unnecessary data movement later.

## In Studio

Primary surface: **Connections → Data Connectors**, alongside the live-source options on a knowledge base.

1. Open **Connections** and go to the **Data Connectors** page — this is where you bring your own stores and databases.
2. To connect your own **vector store**, choose your provider: **Qdrant**, **Weaviate**, **PostgreSQL**, or **Neo4j**.
3. To connect a **database** directly, choose **PostgreSQL**, **MySQL**, or another supported engine.
4. Fill in the **credential form** — your **host** and your **keys**. Once saved, Lyzr is linked to the store and reads from it; the data stays in your systems.
5. For self-maintaining knowledge, add a **live source** instead of a manual upload. Pick from **Website**, **Google Drive**, or **SharePoint**.
6. With a live source connected, the knowledge base re-syncs in the background whenever the underlying content changes — no manual re-upload needed.

## Try this

1. Take one document you'd normally upload by hand and decide which pattern actually fits it — plain upload, live source, or connector. Write one sentence justifying the choice based on how often the content changes and where it should live.
2. Add a **live source** to a knowledge base using a **website** or **Google Drive** folder you control, then change the source content and confirm the agent answers from the updated version.
3. Open the **Data Connectors** page and walk through the credential form for a store you'd connect (e.g. PostgreSQL) — note exactly which fields (host, keys) it asks for, without entering real credentials, so you know what you'd need before a production setup.

## Transcript

Everything we've put into a knowledge base so far we uploaded by hand. That's fine for documents that don't change. But two things take this further: connecting your own data systems and keeping knowledge live. Let's look at both. First, data connectors. So far, we've let Lyzr handle where your data lives, but a lot of teams already run their own infrastructure, and they want their data to stay in it. That's what this page is for. You can connect your own vector store, Qdrant, Weaviate, PostgreSQL, or even Neo4j, or connect a database directly, PostgreSQL, MySQL, et cetera, the point is control. Your data stays in your systems on your terms, and Lyzr reads from it. Connecting is just a credential form. Your host, your keys, and you're linked. I won't put real credentials on screen, but that's the whole flow. Now the second idea, and it's a good one. Live sources. A normal upload is a snapshot, frozen the moment you add it. A live source stays connected, so when the underlying content changes, your knowledge base updates itself in the background, and your agent is always answering from the current version. You've got a few options here, a website, Google Drive, and SharePoint. That's the difference between a knowledge base you maintain by hand and one that maintains itself. So data connectors let you bring your own stores and databases, and live sources keep your knowledge current without manual re-uploads. Use a plain upload for fixed documents, a live source for content that changes, and a connector when the data should stay in your own systems.

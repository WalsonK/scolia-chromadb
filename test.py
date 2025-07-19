#!/usr/bin/env python3
"""
Test rapide de ChromaDB - Version minimaliste
"""

import chromadb


def quick_test():
    # Connexion
    client = chromadb.HttpClient(host='localhost', port=8000)
    print(f"✅ Connecté à ChromaDB v{client.get_version()}")

    # Créer/récupérer une collection
    collection = client.get_or_create_collection("test_simple")

    # Ajouter quelques documents
    collection.add(
        documents=[
            "Les chats sont des animaux domestiques",
            "Python est un langage de programmation",
            "Docker facilite le déploiement d'applications"
        ],
        ids=["chat", "python", "docker"]
    )
    print("✅ Documents ajoutés")

    # Faire une recherche
    results = collection.query(
        query_texts=["animaux"],
        n_results=1
    )

    print(f"\n🔍 Recherche 'animaux':")
    for doc in results['documents'][0]:
        print(f"  • {doc}")

    print(f"\n📊 Total documents: {collection.count()}")


if __name__ == "__main__":
    quick_test()
from airflow.sdk import dag, task, Asset

COLLECTION_NAME = "Books"
EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"

@dag(
    schedule=[Asset("my_book_vector_data")],
    params={"query_str": "A philosophical book"},
)
def query_data():

    @task
    def search_vector_db_for_a_book(**context):
        from airflow.providers.weaviate.hooks.weaviate import WeaviateHook
        from fastembed import TextEmbedding

        query_str = context["params"]["query_str"]

        hook = WeaviateHook("my_weaviate_conn")
        client = hook.get_conn()

        embedding_model = TextEmbedding(EMBEDDING_MODEL_NAME)
        collection = client.collections.get(COLLECTION_NAME)

        query_emb = list(embedding_model.embed([query_str]))[0]

        results = collection.query.near_vector(
            near_vector=query_emb,
            limit=1,
        )
        for result in results.objects:
            book_info = {
                "title": result.properties["title"],
                "author": result.properties["author"],
                "description": result.properties["description"],
            }
            print(f"You should read: {book_info['title']} by {book_info['author']}")
            print("Description:")
            print(result.properties["description"])
            return book_info

    @task.llm(
        model="gpt-4o-mini",
        output_type=str,
        system_prompt="You are a helpful book expert. You will receive information about a book including its title, author, and description. Provide a concise, engaging summary of the book based on this information.",
    )
    def get_book_summary(book_info: dict) -> str:
        return f"Please provide a summary for the following book:\n\nTitle: {book_info['title']}\nAuthor: {book_info['author']}\nDescription: {book_info['description']}"

    get_book_summary(search_vector_db_for_a_book())

query_data()
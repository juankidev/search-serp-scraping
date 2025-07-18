import requests

def buscar_productos(query):
    params = {
        "engine": "google_shopping",
        "q": query,
        "api_key": "5ddeeff637bc395e3c56e3d7bba732cd9035e3a15fdbe462a165e99a94da72c4",  # ← Cámbiala por tu clave real
        "gl": "co",
        "hl": "es",
        "device": "desktop"
    }

    res = requests.get("https://serpapi.com/search.json", params=params)
    data = res.json()

    productos = []

    # 🛒 Extraer resultados de Google Shopping si están disponibles
    if "shopping_results" in data:
        for producto in data["shopping_results"]:
            productos.append({
                "titulo": producto.get("title"),
                "precio": producto.get("price"),
                "rating": producto.get("rating"),
                "reviews": producto.get("reviews"),
                "fuente": producto.get("source"),
                "link": producto.get("link"),
                "imagen": producto.get("thumbnail")
            })

    # 🔗 También podrías combinar con organic_results
    if "organic_results" in data:
        for item in data["organic_results"]:
            productos.append({
                "titulo": item.get("title"),
                "descripcion": item.get("snippet"),
                "link": item.get("link"),
                "fuente": item.get("displayed_link")
            })

    return productos
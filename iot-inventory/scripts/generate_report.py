from my_inventory.shopping import ShoppingList, Query

default_queries = [
    Query("pão"),
    Query("cerveja", required=["super bock"], blacklist=["sagres", "sem alcool"]),
    Query("café", required=["cápsulas"], blacklist=["máquina"]),
    Query("bolachas", required=["chocolate"], blacklist=["branco", "digestiv"]),
    Query("leite"),
    Query("bife de peru", required=["bife", "peru"]),
    Query("bife de frango", required=["bife", "frango"],
          blacklist=["nuggets", "hamburguer", "pate", "tempero para ", "racao "]),
    Query("frango inteiro", required=["inteiro"],
          blacklist=["bife", "nuggets", "hamburguer", "pate", "tempero para ", "racao "]),
    Query("nuggets de frango", required=["nuggets"]),
    Query("douradinhos"),
    Query("leite"),
    Query("arroz", blacklist=["caldo"]),
    Query("salsichas"),
    Query("queijo", blacklist=["pizza"]),
    Query("fiambre", blacklist=["pizza"]),
    Query("atum"),
    Query("alheira"),
    Query("bife de vaca", required=["bife"], blacklist=["frango", "peru", "pimenta", "soja"]),
    Query("manteiga", blacklist=["feijao"]),
    Query("cereais de chocolate", blacklist=["tablete", "barra"]),
    Query("almondegas"),
    Query("hamburger"),
    Query("pizza", blacklist=["mini "]),
    Query("papel higienico"),
    Query("pasta dos dentes"),
    Query("sabão barra", required=["barra"]),
    Query("detergente maquina da roupa", required=["roupa"]),
    Query("detergente maquina da loiça", required=["loiça"]),
    Query("lixivia"),
    Query("lava tudo"),
    Query("ovos", blacklist=["codorniz"]),
    Query("papel higienico"),
    Query("refrigerantes"),
    Query("coca cola"),
    Query("redbull"),
    Query("comida humida para cão", blacklist=["gato", "raçao"]),
    Query("comida humida para gato", blacklist=["cão", "raçao"]),
    Query("comida para cão", blacklist=["gato", "humida"]),
    Query("comida para gato", blacklist=["cão", "humida"]),
    Query("azeite"),
    Query("oleo alimentar"),
    Query("cebola"),
    Query("ervilhas"),
    Query("feijão"),
    Query("espinafres"),
    Query("alho", blacklist=["knorr"]),
    Query("couve"),
    Query("sopa"),
    Query("cenoura", blacklist=["sumo", "nectar", "refrigerante", "bebida"]),
    Query("maça", blacklist=["sumo", "nectar", "refrigerante", "bebida"]),
    Query("banana", blacklist=["sumo", "iogurte", "nectar", "refrigerante", "bebida"]),
    Query("batatas", blacklist=["frita", "pacote", "pure", "onduladas"]),
    Query("batatas pre-fritas", required=["pre", "frita"], blacklist=["pacote", "onduladas"]),
    Query("batatas fritas de pacote", required=["frita"], blacklist=["pre frita", "pre-frita"]),
]

if __name__ == "__main__":

    import datetime

    report = f"""
    Price Report - {datetime.datetime.now()}

    """
    shop = ShoppingList()
    for q in default_queries:
        report += "\n\n# " + q.query.title()
        suggestions = shop.search(q)
        for s in suggestions:
            report += f"\n- {s.name} - {s.price}€ {s.url}"

    with open("report.txt", "w") as f:
        f.write(report)

    print(report)

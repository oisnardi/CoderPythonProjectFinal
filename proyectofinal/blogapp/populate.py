import random
import models

def main():
    for i in range(20):
        category = random.choice(["Tecnología", "Cultura", "Deporte", "Salud", "Viajes"])
        title = "Cómo [tema] con [herramienta]" if category == "Tecnología" else "Un análisis de [tema]" if category == "Cultura" else "Las últimas noticias sobre [tema]" if category == "Deporte" else "Consejos para [tema]" if category == "Salud" else "Los mejores lugares para [tema]"
        content = "En este artículo, te mostraré cómo [tema] con [herramienta]. Primero, [paso 1]. Luego, [paso 2]. Finalmente, [paso 3]." if category == "Tecnología" else "En este artículo, analizaré [tema]. Primero, [punto 1]. Luego, [punto 2]. Finalmente, [punto 3]." if category == "Cultura" else "En este artículo, te contaré las últimas noticias sobre [tema]. Primero, [noticia 1]. Luego, [noticia 2]. Finalmente, [noticia 3]." if category == "Deporte" else "En este artículo, te daré consejos para [tema]. Primero, [consejo 1]. Luego, [consejo 2]. Finalmente, [consejo 3]." if category == "Salud" else "En este artículo, te recomendaré los mejores lugares para [tema]. Primero, [lugar 1]. Luego, [lugar 2]. Finalmente, [lugar 3]."
        image = "/static/img/page_{}.jpg".format(i)
        published_date = random.datetime.now()

        page = models.Page(title=title, content=content, image=image, published_date=published_date)
        page.save()

if __name__ == "__main__":
    main()
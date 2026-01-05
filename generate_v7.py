# ==================================================
# ГЕНЕРАТОР САЙТА-ВИЗИТКИ САКСОФОНИСТА
# Запуск: python generate.py
# ==================================================


# =========================
# ОСНОВНАЯ ИНФОРМАЦИЯ
# =========================

name = "Иван Моисеенко"
subtitle = "Саксофонист • Живая музыка для мероприятий"
location = "Санкт-Петербург и Ленинградская область"

phone = "+79818536540"
instagram = "https://instagram.com/ivan_moiseenko"
vk = "https://vk.com/id200818221"
telegram = "https://t.me/moisey_3"
avito = "https://www.avito.ru/your_profile_link"


# =========================
# УСЛУГИ
# =========================

services = [
    {
        "title": "Корпоративы / банкеты / рестораны",
        "description": "Живое саксофонное сопровождение для мероприятий любого формата. Создаю атмосферу, которая подчёркивает статус события и комфорт гостей.",
        "price": "от … ₽ / час",
        "image": "images/corporate.jpg",
        "position": "center"
    },
    {
        "title": "Свадебная церемония и первый танец",
        "description": "Музыкальное оформление ключевых свадебных моментов — выхода, церемонии и первого танца. Тонко, эмоционально и со вкусом.",
        "price": "от … ₽",
        "image": "images/wedding.jpg",
        "position": "center top"
    },
    {
        "title": "Музыкальный сюрприз",
        "description": "Эффектное короткое выступление как запоминающееся музыкальное поздравление.",
        "price": "от … ₽",
        "image": "images/surprise.jpg",
        "position": "center"
    },
    {
        "title": "Особые моменты",
        "description": "Музыка для предложений руки и сердца, годовщин, выписок из роддома и других личных событий.",
        "price": "от … ₽",
        "image": "images/moments.jpg",
        "position": "center"
    },
    {
        "title": "Индивидуальный заказ композиции",
        "description": "Исполнение выбранной композиции под конкретное событие. Формат и детали обсуждаются индивидуально.",
        "price": "по договорённости",
        "image": "images/custom.jpg",
        "position": "center"
    }
]


# =========================
# ВИДЕО
# =========================

videos = [
    {
        "title": "Свадебная церемония",
        "url": "https://vk.com/video_ext.php?oid=200818221&id=456239386"
    },
    {
        "title": "Корпоративное выступление",
        "url": "https://vk.com/video_ext.php?oid=200818221&id=456239389"
    }
]


# =========================
# ОТЗЫВЫ
# =========================

reviews = [
    {
        "name": "Анна",
        "event": "Свадьба",
        "text": "Очень атмосферно и красиво. Иван создал настроение всего вечера.",
        "photo": "images/reviews/anna.jpg"
    },
    {
        "name": "Дмитрий",
        "event": "Корпоратив",
        "text": "Профессионально, ненавязчиво и со вкусом.",
        "photo": "images/reviews/dmitry.jpg"
    },
    {
        "name": "Екатерина",
        "event": "Музыкальный сюрприз",
        "text": "Сюрприз получился невероятно трогательным.",
        "photo": "images/reviews/ekaterina.jpg"
    }
]


# ==================================================
# ГЕНЕРАЦИЯ HTML-БЛОКОВ
# ==================================================

services_html = ""
for i, s in enumerate(services):
    reverse = "reverse" if i % 2 == 1 else ""
    services_html += f"""
    <div class="service {reverse}">
        <img src="{s['image']}" style="object-position:{s['position']};">
        <div class="service-text">
            <h3>{s['title']}</h3>
            <p>{s['description']}</p>
            <p class="service-price">{s['price']}</p>
        </div>
    </div>
    """

videos_html = ""
for v in videos:
    videos_html += f"""
    <div class="video-item">
        <iframe src="{v['url']}" allowfullscreen></iframe>
        <div class="video-title">{v['title']}</div>
    </div>
    """

reviews_html = ""
for r in reviews:
    reviews_html += f"""
    <div class="review">
        <img src="{r['photo']}">
        <p class="review-text">“{r['text']}”</p>
        <p class="review-author">{r['name']} • {r['event']}</p>
    </div>
    """


# =========================
# ФИНАЛЬНЫЙ HTML
# =========================

html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>{name} — саксофонист</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(180deg, #f1efe9, #f7f7f7);
    color: #222;
}}

.container {{
    max-width: 1100px;
    margin: 0 auto;
    padding: 24px;
}}

/* ЛЕВЫЕ КОНТАКТЫ */
.side-contacts {{
    position: fixed;
    left: 20px;
    top: 50%;
    transform: translateY(-50%) rotate(-90deg);
    display: flex;
    gap: 28px;
    z-index: 1000;
}}

.side-contacts a {{
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #222;
    opacity: 0.7;
}}

.side-contacts a:hover {{ opacity: 1; }}

@media (max-width: 900px) {{
    .side-contacts {{ display: none; }}
}}

/* HERO */
.hero {{
    background: white;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 70px;
}}

.hero img {{
    width:100%;
    height:420px;
    object-fit:cover;
    object-position:center top;
    border-radius:28px;
}}

.hero-text {{
    padding: 36px;
    text-align: center;
}}

h2 {{
    text-align: center;
    margin: 80px 0 40px;
}}

/* УСЛУГИ */
.service {{
    display: flex;
    gap: 40px;
    background: white;
    border-radius: 28px;
    padding: 36px;
    margin-bottom: 50px;
}}

.service.reverse {{ flex-direction: row-reverse; }}

.service img {{
    width: 520px;
    height: 340px;
    object-fit: cover;
    border-radius: 24px;
}}

.service-price {{
    margin-top: 16px;
    font-size: 18px;
    font-weight: 600;
}}

/* ВИДЕО — ВЕРТИКАЛЬНЫЕ, БЕЗ ЧЁРНЫХ ПОЛЕЙ */
.video-block {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
}}

.video-item {{
    position: relative;
    padding-top: 177%;
    background: #000;
    border-radius: 20px;
    overflow: hidden;
}}

.video-item iframe {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    border: none;
}}

.video-title {{
    position: absolute;
    bottom: 12px;
    left: 12px;
    color: #fff;
    font-size: 14px;
    opacity: 0.85;
}}

@media (max-width: 800px) {{
    .video-block {{
        grid-template-columns: 1fr;
    }}
}}

/* ОТЗЫВЫ */
.reviews-carousel {{
    background: white;
    border-radius: 28px;
    padding: 36px;
    max-width: 700px;
    margin: 0 auto;
}}

.review {{
    display: none;
    text-align: center;
}}

.review.active {{ display: block; }}

.review img {{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 16px;
}}
</style>
</head>

<body>

<div class="side-contacts">
    <a href="{vk}" target="_blank">VK</a>
    <a href="{instagram}" target="_blank">INSTAGRAM</a>
    <a href="{telegram}" target="_blank">TELEGRAM</a>
</div>

<div class="container">

<div class="hero">
    <img src="images/hero.jpg">
    <div class="hero-text">
        <h1>{name}</h1>
        <p>{subtitle}</p>
        <p>{location}</p>
    </div>
</div>

<h2>Услуги</h2>
{services_html}

<h2>Видео</h2>
<div class="video-block">
{videos_html}
</div>

<h2>Отзывы</h2>
<div class="reviews-carousel">
{reviews_html}
</div>

<p style="text-align:center; opacity:0.6; margin-top:20px;">
    Больше отзывов —
    <a href="{avito}" target="_blank" style="color:inherit;">на платформе Avito</a>
</p>

</div>

<script>
const reviews = document.querySelectorAll('.review');
let i = 0;
function showReview(n) {{
    reviews.forEach(r => r.classList.remove('active'));
    reviews[n].classList.add('active');
}}
showReview(0);
setInterval(() => {{
    i = (i + 1) % reviews.length;
    showReview(i);
}}, 5000);
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html создан")

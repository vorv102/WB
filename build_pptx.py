"""Генератор презентации проекта «АвтоСервис Мотор» (10 слайдов)."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BG = RGBColor(0x0B, 0x11, 0x20)
CARD = RGBColor(0x16, 0x20, 0x36)
LINE = RGBColor(0x2A, 0x37, 0x52)
WHITE = RGBColor(0xE8, 0xEE, 0xF8)
MUTED = RGBColor(0xA8, 0xB7, 0xCE)
AMBER = RGBColor(0xFB, 0xBF, 0x24)
SKY = RGBColor(0x38, 0xBD, 0xF8)
GREEN = RGBColor(0x34, 0xD3, 0x99)
RED = RGBColor(0xFB, 0x71, 0x85)
VIOLET = RGBColor(0xA7, 0x8B, 0xFA)
FONT = "Segoe UI"
MONO = "Consolas"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def rect(slide, x, y, w, h, fill=CARD, line=None, rounded=True):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line:
        shape.line.color.rgb = line
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    if rounded:
        try:
            shape.adjustments[0] = 0.08
        except Exception:
            pass
    return shape


def text(slide, x, y, w, h, content, size=14, color=WHITE, bold=False,
         align=PP_ALIGN.LEFT, font=FONT, valign=MSO_ANCHOR.TOP, spacing=1.0):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.02)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = valign
    lines = content.split("\n")
    for n, line in enumerate(lines):
        p = tf.paragraphs[0] if n == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(4)
        p.line_spacing = spacing
        r = p.add_run()
        r.text = line
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color
        r.font.name = font
    return box


def base(title, eyebrow, idx):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    rect(s, 0, 0, 13.333, 0.06, AMBER, rounded=False)
    rect(s, 0, 0, 13.333 * idx / 10, 0.06, AMBER, rounded=False)
    text(s, 0.85, 0.35, 11.8, 0.3, eyebrow.upper(), 11, AMBER, True)
    text(s, 0.85, 0.7, 11.8, 0.65, title, 33, WHITE, True)
    text(s, 0.85, 7.05, 8, 0.25, "АвтоСервис «Мотор» · презентация проекта", 10, MUTED)
    text(s, 11.6, 7.05, 0.9, 0.25, f"{idx:02d} / 10", 10, MUTED, align=PP_ALIGN.RIGHT)
    return s


def card(s, x, y, w, h, tag, heading, body, accent=AMBER, body_size=12.5):
    rect(s, x, y, w, h, CARD, LINE)
    rect(s, x + 0.2, y + 0.2, 0.85, 0.3, accent)
    text(s, x + 0.28, y + 0.225, 0.8, 0.25, tag, 9, BG, True)
    text(s, x + 0.2, y + 0.6, w - 0.4, 0.7, heading, 15.5, WHITE, True)
    text(s, x + 0.2, y + 1.28, w - 0.4, h - 1.42, body, body_size, MUTED, spacing=1.05)


def bullet_lines(items, mark="•  "):
    return "\n".join(mark + i for i in items)


# 1 — титул
s = prs.slides.add_slide(BLANK)
s.background.fill.solid()
s.background.fill.fore_color.rgb = BG
rect(s, 0, 0, 13.333, 0.07, AMBER, rounded=False)
rect(s, 0.85, 1.5, 2.4, 0.36, AMBER)
text(s, 1.0, 1.55, 2.3, 0.26, "УЧЕБНЫЙ ПРОЕКТ", 11, BG, True)
text(s, 0.85, 2.15, 11.6, 1.1, "АвтоСервис «Мотор»", 52, WHITE, True)
text(s, 0.85, 3.35, 11.5, 0.8,
     "Сайт для онлайн-записи на ремонт автомобилей: услуги, цены, мастера, заявки и отзывы.", 21, SKY)
text(s, 0.85, 4.35, 11, 0.7,
     "Как я придумал, спроектировал, написал и отлаживал приложение — за 10 слайдов.", 16, MUTED)
chips = ["Python 3.11", "Django 5.2.17", "SQLite", "HTML5 / CSS3", "Pillow", "Git + GitHub"]
x = 0.85
for c in chips:
    w = 0.28 * len(c) + 0.5
    rect(s, x, 5.4, w, 0.42, CARD, LINE)
    text(s, x + 0.1, 5.5, w - 0.2, 0.25, c, 11, WHITE, align=PP_ALIGN.CENTER)
    x += w + 0.16
text(s, 0.85, 6.5, 11.6, 0.4, "github.com/vorv102/WB", 17, AMBER, True)

# 2 — проблема и цель
s = base("Проблема и цель проекта", "Зачем нужен сайт", 2)
card(s, 0.85, 1.65, 5.6, 4.2, "БЫЛО", "Проблемы клиента и сервиса", bullet_lines([
    "Нельзя быстро узнать цены и сроки — приходится звонить.",
    "Не видно мастеров, их опыт и специализацию.",
    "Запись по телефону: заявки легко потерять, нет истории.",
]), RED, 14)
card(s, 6.85, 1.65, 5.6, 4.2, "СТАЛО", "Что даёт сайт", bullet_lines([
    "Каталог услуг с ценой и длительностью работ.",
    "Страница мастеров с фото, должностью и стажем.",
    "Онлайн-заявка, кабинет, отзывы и админка.",
]), GREEN, 14)
rect(s, 0.85, 6.1, 11.6, 0.6, CARD, LINE)
text(s, 1.1, 6.25, 11.1, 0.3, "Цель: сделать запись простой, а информацию об услугах — прозрачной.", 15, AMBER, True)

# 3 — возможности
s = base("7 страниц + панель управления", "Обзор возможностей", 3)
pages = [
    ("01", "Главная", "Герой-блок, преимущества и 6 популярных услуг с ценами."),
    ("02", "Услуги", "Каталог по категориям: цена, время и кнопка «Записаться»."),
    ("03", "Мастера", "Карточки с фото, должностью, опытом и описанием."),
    ("04", "Запись", "Форма: имя, телефон, авто, услуга, мастер, дата, комментарий."),
    ("05", "Контакты", "Адрес, телефон, e-mail, режим работы и карта Яндекса."),
    ("06", "Вход", "Регистрация, логин и logout на встроенных формах Django."),
    ("07", "Кабинет", "Мои заявки, отзывы с оценкой 1–5 и лента отзывов."),
    ("+", "Админка", "/admin/: категории, услуги, мастера и заявки."),
]
for n, (tag, head, body) in enumerate(pages):
    col, row = n % 4, n // 4
    card(s, 0.85 + col * 3.0, 1.6 + row * 2.55, 2.8, 2.35,
         tag, head, body, AMBER if n != 7 else GREEN, 12)

# 4 — сценарии
s = base("Два сценария: клиент и администратор", "Как пользователь ходит по сайту", 4)
rect(s, 0.85, 1.6, 11.6, 2.35, CARD, LINE)
rect(s, 1.05, 1.8, 1.3, 0.32, SKY)
text(s, 1.15, 1.855, 1.25, 0.24, "КЛИЕНТ", 9, BG, True)
text(s, 1.05, 2.35, 11.2, 0.75,
     "Главная  →  Услуги и цены  →  Выбор мастера  →  Форма записи  →  Кабинет  →  Отзыв ⭐",
     17, WHITE, True)
text(s, 1.05, 3.28, 11.2, 0.5,
     "Кнопка «Записаться» передаёт ID услуги через URL: ?service=5 — форма открывается с выбранной услугой.", 12.5, MUTED)
rect(s, 0.85, 4.2, 11.6, 2.35, CARD, LINE)
rect(s, 1.05, 4.4, 2.5, 0.32, VIOLET)
text(s, 1.15, 4.455, 2.4, 0.24, "АДМИНИСТРАТОР", 9, BG, True)
text(s, 1.05, 4.95, 11.2, 0.75,
     "/admin/  →  Категории и услуги  →  Мастера  →  Заявки  →  Смена статуса", 17, WHITE, True)
text(s, 1.05, 5.9, 11.2, 0.5,
     "Статусы заявки: Новая → Подтверждена → Выполнена или Отменена.", 12.5, MUTED)

# 5 — стек
s = base("Технологический стек", "Из чего собрано приложение", 5)
card(s, 0.85, 1.6, 2.8, 3.6, "ОСНОВА", "Python 3.11\nDjango 5.2.17",
     "Архитектура MVT. Встроенные auth, admin, messages и CSRF-защита.", AMBER, 13)
card(s, 3.85, 1.6, 2.8, 3.6, "ДАННЫЕ", "SQLite",
     "Файл db.sqlite3, миграции. Хороший выбор для учебного проекта.", SKY, 13)
card(s, 6.85, 1.6, 2.8, 3.6, "ИНТЕРФЕЙС", "HTML5 + CSS3",
     "Свой style.css, шаблоны с наследованием от base.html, адаптивные сетки.", GREEN, 13)
card(s, 9.85, 1.6, 2.8, 3.6, "ДОПОЛНЕНИЯ", "Pillow · Яндекс.Карты",
     "Фото мастеров и карта через iframe без внешних зависимостей.", VIOLET, 13)
rect(s, 0.85, 5.55, 11.6, 1.0, CARD, LINE)
text(s, 1.1, 5.72, 11.2, 0.7,
     "requirements.txt → Django==5.2.17 · pillow==12.3.0\nconfig/settings.py → LANGUAGE_CODE='ru-ru', TIME_ZONE='Europe/Moscow'",
     13, SKY, font=MONO)

# 6 — архитектура
s = base("Архитектура проекта", "Организация кода", 6)
rect(s, 0.85, 1.55, 5.6, 4.95, CARD, LINE)
tree = """WB/
├─ manage.py          запуск и команды
├─ requirements.txt   зависимости
├─ db.sqlite3         база данных
├─ config/            проект
│  ├─ settings.py     настройки
│  ├─ urls.py         маршруты + login/logout
│  ├─ templates/      base.html, home, services...
│  └─ static/css/style.css
└─ main/              приложение
   ├─ models.py       таблицы БД
   ├─ views.py        логика страниц
   ├─ forms.py        ModelForm
   ├─ urls.py         маршруты приложения
   ├─ admin.py        панель управления
   └─ migrations/     история БД"""
text(s, 1.05, 1.8, 5.3, 4.6, tree, 11.5, WHITE, font=MONO, spacing=1.0)
card(s, 6.85, 1.55, 5.6, 2.15, "MVT", "Поток запроса",
     "URL → view → model / БД → template → HTML-ответ", AMBER, 14)
card(s, 6.85, 3.95, 5.6, 2.55, "НАСТРОЙКИ", "Ключевые параметры", bullet_lines([
    "DIRS подключает config/templates.",
    "STATICFILES_DIRS и MEDIA для стилей и фото.",
    "LOGIN_REDIRECT_URL = '/profile/'.",
]), SKY, 13)

# 7 — модели
s = base("На чём хранится информация", "Модели данных", 7)
card(s, 0.85, 1.6, 3.7, 4.3, "КАТАЛОГ", "ServiceCategory\nService",
     "Категория: name.\nУслуга: category → FK, name, description, price, duration, is_active.", AMBER, 13.5)
card(s, 4.8, 1.6, 3.7, 4.3, "ЛЮДИ", "Master\nUser (Django)",
     "Мастер: ФИО, должность, опыт, фото, описание, is_active.\nПользователь — встроенная модель авторизации.", SKY, 13.5)
card(s, 8.75, 1.6, 3.7, 4.3, "СОБЫТИЯ", "Appointment\nReview",
     "Заявка: имя, телефон, авто, услуга, мастер, дата, комментарий, статус.\nОтзыв: user → FK, текст, оценка 1–5.", GREEN, 13.5)
rect(s, 0.85, 6.1, 11.6, 0.65, CARD, LINE)
text(s, 1.05, 6.25, 11.2, 0.35,
     "Связи: CASCADE для категории и пользователя, SET_NULL для услуги и мастера в заявке.", 13, AMBER)

# 8 — этапы
s = base("Как я это делал — 7 шагов", "Процесс работы", 8)
steps = [
    ("Каркас", "django-admin startproject + startapp main"),
    ("Настройки", "приложение, шаблоны, static/media, ru и Москва"),
    ("Модели", "5 таблиц, makemigrations и migrate"),
    ("Интерфейс", "base.html + страницы, единый CSS"),
    ("Логика", "views, ModelForm, POST → redirect"),
    ("Аккаунты", "регистрация, вход, кабинет"),
    ("Финал", "админка, отладка, 3 коммита на GitHub"),
]
for n, (head, body) in enumerate(steps):
    row, col = divmod(n, 4)
    x = 0.85 + col * 3.0
    y = 1.6 + row * 2.25
    rect(s, x, y, 2.8, 2.05, CARD, LINE)
    rect(s, x + 0.18, y + 0.18, 0.42, 0.42, AMBER, rounded=False)
    text(s, x + 0.18, y + 0.22, 0.42, 0.3, str(n + 1), 13, BG, True, PP_ALIGN.CENTER)
    text(s, x + 0.18, y + 0.75, 2.45, 0.4, head, 15, WHITE, True)
    text(s, x + 0.18, y + 1.2, 2.45, 0.75, body, 11.5, MUTED)
text(s, 0.85, 6.35, 11.6, 0.4,
     "Модель Review появилась второй миграцией 0002_review.py — так выглядит эволюция базы.", 12.5, SKY)

# 9 — витрина интерфейса
s = base("Как выглядит сайт: три ключевых экрана", "Витрина проекта", 9)

def win(x, url):
    rect(s, x, 1.55, 3.6, 4.45, CARD, LINE)
    rect(s, x + 0.1, 1.65, 3.4, 0.3, RGBColor(0x1B, 0x27, 0x40), rounded=False)
    for k, c in enumerate([RED, AMBER, GREEN]):
        rect(s, x + 0.23 + k * 0.16, 1.755, 0.09, 0.09, c)
    text(s, x + 0.8, 1.73, 2.6, 0.2, url, 8, MUTED, font=MONO)
    return x + 0.2, 2.08

# экран 1 — главная
bx, by = win(0.85, "localhost:8000/")
rect(s, bx, by, 3.2, 1.2, RGBColor(0x24, 0x2E, 0x47))
text(s, bx + 0.12, by + 0.12, 2.95, 0.55, "Ремонт автомобилей\nлюбой сложности", 12, WHITE, True)
text(s, bx + 0.12, by + 0.72, 2.95, 0.25, "Мастера, честные цены, гарантия", 8.5, MUTED)
rect(s, bx + 0.12, by + 0.97, 1.55, 0.18, AMBER)
text(s, bx + 0.16, by + 0.985, 1.5, 0.15, "Записаться на ремонт", 7.5, BG, True)
mini = [("Оборудование", "Стенды и диагностика"), ("Гарантия", "1 год на работы"),
        ("Диагностика", "от 1 500 ₽"), ("ТО", "от 3 000 ₽"), ("Ремонт", "по факту"), ("Подвеска", "от 2 500 ₽")]
for k, (h, b) in enumerate(mini):
    col, row = k % 3, k // 3
    mx, my = bx + col * 1.09, 3.42 + row * 0.8
    rect(s, mx, my, 1.01, 0.7, RGBColor(0x13, 0x1D, 0x33), LINE)
    text(s, mx + 0.07, my + 0.08, 0.9, 0.2, h, 9, AMBER, True)
    text(s, mx + 0.07, my + 0.33, 0.9, 0.3, b, 8, MUTED)
text(s, 0.85, 6.12, 3.6, 0.3, "Главная  /", 13, WHITE, True)

# экран 2 — услуги
bx, by = win(4.85, "localhost:8000/services/")
text(s, bx, by, 3.1, 0.35, "Наши услуги", 14, WHITE, True)
rect(s, bx, 2.52, 3.2, 0.3, RGBColor(0x24, 0x2E, 0x47), rounded=False)
text(s, bx + 0.08, 2.575, 1.9, 0.2, "УСЛУГА", 8, AMBER, True)
text(s, bx + 2.0, 2.575, 1.1, 0.2, "ВРЕМЯ · ЦЕНА", 8, AMBER, True)
rows = [("Диагностика", "60 мин · 1 500 ₽"), ("Замена масла", "30 мин · 1 200 ₽"),
        ("Тормоза", "120 мин · 4 500 ₽"), ("Подвеска", "90 мин · 3 000 ₽"),
        ("Кондиционер", "60 мин · 2 200 ₽")]
for k, (a, b) in enumerate(rows):
    y = 2.86 + k * 0.47
    rect(s, bx, y, 3.2, 0.42, RGBColor(0x11, 0x1B, 0x30), rounded=False)
    text(s, bx + 0.08, y + 0.1, 1.9, 0.22, a, 9, WHITE)
    text(s, bx + 2.0, y + 0.1, 1.1, 0.22, b, 8.5, GREEN)
rect(s, bx + 2.05, 5.5, 1.15, 0.28, AMBER)
text(s, bx + 2.1, 5.55, 1.1, 0.2, "Записаться", 8, BG, True, PP_ALIGN.CENTER)
text(s, 4.85, 6.12, 3.6, 0.3, "Каталог услуг  /services/", 13, WHITE, True)

# экран 3 — форма записи
bx, by = win(8.85, "localhost:8000/appointment/")
text(s, bx, by, 3.1, 0.35, "Записаться на ремонт", 14, WHITE, True)
fields = ["Имя клиента", "Телефон", "Автомобиль", "Услуга ▾   Мастер ▾", "Желаемая дата", "Комментарий"]
for k, f in enumerate(fields):
    y = 2.5 + k * 0.47
    rect(s, bx, y, 3.2, 0.38, RGBColor(0x13, 0x1D, 0x33), LINE)
    text(s, bx + 0.12, y + 0.09, 2.9, 0.22, f, 9.5, MUTED)
rect(s, bx, 5.5, 2.0, 0.3, AMBER)
text(s, bx + 0.08, 5.56, 1.9, 0.2, "Отправить заявку", 9, BG, True, PP_ALIGN.CENTER)
text(s, 8.85, 6.12, 3.6, 0.3, "Форма записи  /appointment/", 13, WHITE, True)

text(s, 0.85, 6.62, 11.6, 0.3,
     "Все экраны наследуют base.html и styling из config/static/css/style.css; данные подставляет Django.", 11, MUTED)

# 10 — итог
s = base("Что получилось и что дальше", "Итог", 10)
card(s, 0.85, 1.6, 5.6, 3.7, "ГОТОВО", "Результат", bullet_lines([
    "Сайт с каталогом, записью, кабинетом и отзывами.",
    "Данные меняются через админку; всё работает локально.",
    "Код лежит в открытом репозитории на GitHub.",
]), GREEN, 14)
card(s, 6.85, 1.6, 5.6, 3.7, "ПЛАНЫ", "Развитие проекта", bullet_lines([
    "Календарь и проверка занятости мастеров.",
    "Уведомления и загрузка фотографий.",
    "Тесты, продакшен-настройки и деплой.",
]), SKY, 14)
text(s, 0.85, 5.6, 11.6, 0.45, "github.com/vorv102/WB", 20, AMBER, True, PP_ALIGN.CENTER)
text(s, 0.85, 6.2, 11.6, 0.55, "Спасибо за внимание! Вопросы?", 25, WHITE, True, PP_ALIGN.CENTER)

out = r"C:\Users\PC\Documents\Проект по умолчанию\presentation\WB_presentation.pptx"
prs.save(out)
print("Saved:", out, "slides:", len(prs.slides.__iter__.__self__._sldIdLst))

import streamlit as st
from html import escape


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Painel de Gestão Pessoal",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# LINKS
# =========================================================
# Para adicionar novos links, basta incluir um novo item
# nesta lista seguindo o mesmo padrão.

LINKS = [
    {
        "titulo": "Jeito Barsi de Investir",
        "descricao": "Curso de investimentos da AGF",
        "url": (
            "https://agf.com.br/jeito-barsi-de-investir"
            "?utm_medium=1791293203631_17912934294085"
            "&uid_mh=1791293203631_17912934294085"
        ),
        "categoria": "Investimentos",
        "icone": "📈",
        "destaque": "CURSO",
    },
    {
        "titulo": "Projeto Construção Imóvel",
        "descricao": "Projeto Praia do Forte no Notion",
        "url": (
            "https://app.notion.com/p/"
            "Praia-do-Forte-6177f7a69cdb48b8925e8f6f665c363b"
            "?source=copy_link"
        ),
        "categoria": "Organização",
        "icone": "🏠",
        "destaque": "NOTION",
    },
    {
        "titulo": "Agenda Pessoal",
        "descricao": "Acessar Google Calendar",
        "url": "https://calendar.google.com/calendar/u/0/r/week",
        "categoria": "Organização",
        "icone": "📅",
        "destaque": "CALENDAR",
    },
    {
        "titulo": "E-mail",
        "descricao": "Acessar caixa de entrada do Outlook",
        "url": "https://outlook.live.com/mail/",
        "categoria": "Organização",
        "icone": "✉️",
        "destaque": "OUTLOOK",
    },
    {
        "titulo": "Gestão de Senhas",
        "descricao": "Gerenciador de senhas do Google",
        "url": "https://passwords.google.com/?hl=pt-br&pli=1",
        "categoria": "Utilidades",
        "icone": "🔐",
        "destaque": "GOOGLE",
    },

    # EXEMPLOS PARA ADICIONAR DEPOIS:
    # {
    #     "titulo": "BTG",
    #     "descricao": "Investimentos e conta",
    #     "url": "COLOQUE_O_LINK_AQUI",
    #     "categoria": "Finanças",
    #     "icone": "💰",
    #     "destaque": "FINANÇAS",
    # },
    # {
    #     "titulo": "Caixa",
    #     "descricao": "Internet Banking",
    #     "url": "COLOQUE_O_LINK_AQUI",
    #     "categoria": "Finanças",
    #     "icone": "🏦",
    #     "destaque": "BANCO",
    # },
]


# =========================================================
# CSS
# =========================================================

st.html(
    r"""
<style>
    :root {
        --bg: #07111f;
        --bg-secondary: #0a1627;
        --card: rgba(15, 32, 53, 0.88);
        --card-hover: rgba(21, 48, 79, 0.98);
        --border: rgba(120, 169, 255, 0.16);
        --border-hover: rgba(70, 145, 255, 0.60);
        --blue: #3b82f6;
        --blue-light: #60a5fa;
        --blue-dark: #2563eb;
        --text: #f4f7fb;
        --text-secondary: #9aaabd;
        --text-muted: #64748b;
    }

    html,
    body,
    [data-testid="stAppViewContainer"],
    .stApp {
        background: #07111f;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 85% 5%,
                rgba(37, 99, 235, 0.13),
                transparent 30%
            ),
            radial-gradient(
                circle at 5% 90%,
                rgba(59, 130, 246, 0.08),
                transparent 30%
            ),
            var(--bg);
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        margin-bottom: 28px;
        color: var(--text-secondary);
        font-size: 13px;
    }

    .brand-mini {
        display: flex;
        align-items: center;
        gap: 9px;
        font-weight: 700;
        color: #d9e7fb;
        letter-spacing: 0.35px;
    }

    .brand-dot {
        width: 9px;
        height: 9px;
        background: var(--blue);
        border-radius: 50%;
        box-shadow: 0 0 14px rgba(59, 130, 246, 0.9);
    }

    .workspace-text {
        color: #6f829a;
        font-weight: 700;
        letter-spacing: 1.1px;
        font-size: 10px;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 44px 46px;
        margin-bottom: 30px;
        border: 1px solid var(--border);
        border-radius: 26px;
        background:
            linear-gradient(
                120deg,
                rgba(17, 40, 68, 0.95),
                rgba(9, 23, 42, 0.92)
            );
        box-shadow: 0 18px 50px rgba(0, 0, 0, 0.22);
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 320px;
        height: 320px;
        right: -100px;
        top: -150px;
        border-radius: 50%;
        background: rgba(59, 130, 246, 0.16);
        filter: blur(12px);
        pointer-events: none;
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .hero-badge {
        display: inline-block;
        padding: 6px 11px;
        background: rgba(59, 130, 246, 0.12);
        border: 1px solid rgba(96, 165, 250, 0.24);
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        color: var(--blue-light);
        letter-spacing: 1.3px;
        margin-bottom: 16px;
    }

    .hero h1 {
        margin: 0;
        color: #ffffff;
        font-size: clamp(31px, 4vw, 47px);
        font-weight: 750;
        letter-spacing: -1.4px;
        line-height: 1.06;
    }

    .hero p {
        max-width: 680px;
        margin-top: 13px;
        margin-bottom: 0;
        color: var(--text-secondary);
        font-size: 16px;
        line-height: 1.65;
    }

    .stats {
        display: flex;
        gap: 14px;
        margin-top: 28px;
        flex-wrap: wrap;
    }

    .stat {
        padding: 11px 17px;
        background: rgba(4, 15, 29, 0.38);
        border: 1px solid rgba(148, 163, 184, 0.10);
        border-radius: 12px;
        color: var(--text-secondary);
        font-size: 13px;
    }

    .stat strong {
        color: white;
        margin-right: 5px;
    }

    .status-dot {
        display: inline-block;
        width: 7px;
        height: 7px;
        margin-right: 7px;
        border-radius: 50%;
        background: #60a5fa;
        box-shadow: 0 0 10px rgba(96, 165, 250, 0.65);
    }

    .section-header {
        margin-top: 25px;
        margin-bottom: 17px;
    }

    .section-title {
        color: #f8fafc;
        font-weight: 700;
        font-size: 20px;
        margin: 0;
    }

    .section-subtitle {
        color: var(--text-muted);
        font-size: 13px;
        margin-top: 4px;
    }

    .links-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 17px;
        width: 100%;
    }

    .link-card {
        position: relative;
        display: block;
        min-height: 190px;
        padding: 23px 23px 21px 23px;
        border-radius: 19px;
        border: 1px solid var(--border);
        background:
            linear-gradient(
                145deg,
                rgba(18, 39, 65, 0.91),
                rgba(10, 24, 42, 0.91)
            );
        text-decoration: none !important;
        overflow: hidden;
        transition:
            transform 0.20s ease,
            border-color 0.20s ease,
            box-shadow 0.20s ease,
            background 0.20s ease;
    }

    .link-card::after {
        content: "";
        position: absolute;
        width: 120px;
        height: 120px;
        right: -50px;
        bottom: -55px;
        border-radius: 50%;
        background: rgba(59, 130, 246, 0.08);
        transition: 0.25s ease;
        pointer-events: none;
    }

    .link-card:hover {
        transform: translateY(-5px);
        border-color: var(--border-hover);
        box-shadow:
            0 16px 36px rgba(0, 0, 0, 0.27),
            0 0 24px rgba(59, 130, 246, 0.07);
        background:
            linear-gradient(
                145deg,
                rgba(23, 49, 81, 0.98),
                rgba(11, 28, 49, 0.98)
            );
    }

    .link-card:hover::after {
        transform: scale(1.35);
    }

    .card-icon {
        width: 43px;
        height: 43px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 19px;
        border-radius: 12px;
        background:
            linear-gradient(
                135deg,
                rgba(59, 130, 246, 0.22),
                rgba(37, 99, 235, 0.08)
            );
        border: 1px solid rgba(96, 165, 250, 0.17);
        font-size: 21px;
    }

    .card-category {
        position: absolute;
        right: 18px;
        top: 19px;
        color: #7291b8;
        font-size: 9px;
        font-weight: 800;
        letter-spacing: 1.15px;
    }

    .card-title {
        color: #f8fafc;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .card-description {
        color: #8799ae;
        font-size: 12.5px;
        line-height: 1.5;
        padding-right: 34px;
    }

    .card-open {
        position: absolute;
        right: 20px;
        bottom: 18px;
        color: #60a5fa;
        font-size: 19px;
        transition: transform 0.20s ease;
    }

    .link-card:hover .card-open {
        transform: translate(3px, -3px);
    }

    div[data-baseweb="input"] > div {
        background: #0d1e32 !important;
        border-color: rgba(96, 165, 250, 0.18) !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="input"] input {
        color: #eaf2ff !important;
    }

    div[data-baseweb="select"] > div {
        background: #0d1e32 !important;
        border-color: rgba(96, 165, 250, 0.18) !important;
        border-radius: 12px !important;
    }

    label[data-testid="stWidgetLabel"] p {
        color: #8fa4bc !important;
        font-size: 12px !important;
    }

    .custom-footer {
        margin-top: 45px;
        padding-top: 22px;
        border-top: 1px solid rgba(148, 163, 184, 0.08);
        color: #506176;
        text-align: center;
        font-size: 11px;
        letter-spacing: 0.7px;
    }

    @media (max-width: 650px) {
        .block-container {
            padding-left: 16px;
            padding-right: 16px;
        }

        .hero {
            padding: 30px 25px;
        }

        .hero h1 {
            font-size: 31px;
        }

        .hero p {
            font-size: 14px;
        }

        .links-grid {
            grid-template-columns: 1fr;
        }

        .topbar {
            margin-bottom: 20px;
        }
    }
</style>
"""
)


# =========================================================
# CABEÇALHO
# =========================================================

st.html(
    """
<div class="topbar">
    <div class="brand-mini">
        <span class="brand-dot"></span>
        CENTRAL PESSOAL
    </div>

    <div class="workspace-text">
        WORKSPACE
    </div>
</div>
"""
)


# =========================================================
# HERO
# =========================================================

quantidade_links = len(LINKS)
quantidade_categorias = len(set(item["categoria"] for item in LINKS))

st.html(
    f"""
<div class="hero">
    <div class="hero-content">
        <div class="hero-badge">
            PAINEL PESSOAL
        </div>

        <h1>Painel de Gestão Pessoal</h1>

        <p>
            Seus projetos, investimentos, agenda e ferramentas
            pessoais reunidos em um único lugar.
        </p>

        <div class="stats">
            <div class="stat">
                <strong>{quantidade_links}</strong> atalhos
            </div>

            <div class="stat">
                <strong>{quantidade_categorias}</strong> categorias
            </div>

            <div class="stat">
                <span class="status-dot"></span>
                Central de organização
            </div>
        </div>
    </div>
</div>
"""
)


# =========================================================
# PESQUISA / FILTRO
# =========================================================

col_busca, col_categoria = st.columns([2.5, 1])

with col_busca:
    busca = st.text_input(
        "Pesquisar",
        placeholder="🔎  Pesquisar projetos, cursos, ferramentas...",
        label_visibility="collapsed",
    )

with col_categoria:
    categorias = sorted(set(item["categoria"] for item in LINKS))

    categoria_selecionada = st.selectbox(
        "Categoria",
        ["Todos"] + categorias,
        label_visibility="collapsed",
    )


# =========================================================
# FILTRAGEM
# =========================================================

links_filtrados = LINKS

if categoria_selecionada != "Todos":
    links_filtrados = [
        item
        for item in links_filtrados
        if item["categoria"] == categoria_selecionada
    ]

if busca:
    busca_normalizada = busca.lower().strip()

    links_filtrados = [
        item
        for item in links_filtrados
        if (
            busca_normalizada in item["titulo"].lower()
            or busca_normalizada in item["descricao"].lower()
            or busca_normalizada in item["categoria"].lower()
            or busca_normalizada in item["destaque"].lower()
        )
    ]


# =========================================================
# TÍTULO DA SEÇÃO
# =========================================================

st.html(
    f"""
<div class="section-header">
    <div class="section-title">
        Acessos rápidos
    </div>

    <div class="section-subtitle">
        {len(links_filtrados)} acesso(s) disponível(is)
    </div>
</div>
"""
)


# =========================================================
# CARDS
# =========================================================

if links_filtrados:
    cards = ""

    for item in links_filtrados:
        titulo = escape(item["titulo"])
        descricao = escape(item["descricao"])
        url = escape(item["url"], quote=True)
        categoria = escape(item["destaque"])
        icone = escape(item["icone"])

        cards += f"""
<a
    class="link-card"
    href="{url}"
    target="_blank"
    rel="noopener noreferrer"
>
    <div class="card-category">{categoria}</div>

    <div class="card-icon">
        {icone}
    </div>

    <div class="card-title">
        {titulo}
    </div>

    <div class="card-description">
        {descricao}
    </div>

    <div class="card-open">
        ↗
    </div>
</a>
"""

    st.html(
        f"""
<div class="links-grid">
{cards}
</div>
"""
    )

else:
    st.info("Nenhum acesso encontrado para os filtros selecionados.")


# =========================================================
# RODAPÉ
# =========================================================

st.html(
    """
<div class="custom-footer">
    PAINEL DE GESTÃO PESSOAL • STREAMLIT
</div>
"""
)

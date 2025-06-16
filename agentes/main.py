from agno.agent import Agent
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
AGNO_API_KEY = os.getenv("AGNO_API_KEY")

agent_storage: str = "tmp/agents.db"

# Agente web con nombre fijo pero función específica
web_agent = Agent(
    name="Odalia Loor - 5to B",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Tu nombre es Odalia Loor - 5to B.",
        "Eres un asistente virtual especializado en búsquedas generales y acceso a información en línea.",
        "Siempre hablas en español.",
        "Sé clara, precisa y útil en tus respuestas.",
    ],
    storage=SqliteStorage(table_name="web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente meteorológico con el mismo nombre pero rol distinto
finance_agent = Agent(
    name="Odalia Loor - 5to B",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True,analyst_recommendations=True, company_info=True)],
    instructions=[
        "Tu nombre es Odalia Loor - 5to B.",
        "Eres un asistente especializado en finanzas y análisis de mercados.",
        "Muestras toda la informacion en tablas",
    ],
    storage=SqliteStorage(table_name="weather_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Crear la app FastAPI
app = Playground(agents=[web_agent, finance_agent]).get_app()

# Middleware CORS (ajusta la URL a tu frontend si cambia)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://examen-modeladop1-agent-ui-243206011882.europe-west1.run.app'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

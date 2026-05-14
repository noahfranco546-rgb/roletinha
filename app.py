from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from userList import UserList
from pokemonList import PokemonList
from pathlib import Path

app = FastAPI()

# Dados originais (usados para reset)
ORIGINAL_USERS = [
    "Gabriel - Hardware (Fullcond)",
    "Vitor - Mobile (Fullcond)",
    "Gabriel - AWS(careca) Infra",
    "Enzo - infra ",
    "Thiago - (Fullcond)",
    "Gui - (Fullcond)",
    "João Jorge - Infra",
    "Lucas Vieria (capas) - (Fullcond)",
    "Noah - (Fullcond)",
    "Vitor santos - (Fullcond)"
]

ORIGINAL_ELEMENTS = [
    "Aço (Steel)",
    "Água (Water)",
    "Dragão (Dragon)",
    "Elétrico (Electric)",
    "Fada (Fairy)",
    "Fogo (Fire)",
    "Gelo (Ice)",
    "Inseto (Bug)",
    "Lutador (Fighting)",
    "Normal",
    "Planta (Grass)",
    "Psíquico (Psychic)",
    "Pedra (Rock)",
    "Sombrio (Dark)",
    "Terrestre (Ground)",
    "Venenoso (Poison)",
    "Fantasma (Ghost)",
    "Voador (Flying)"
]

# Instâncias globais (iniciadas a partir dos originais)
users = UserList(list(ORIGINAL_USERS))
elements = PokemonList(list(ORIGINAL_ELEMENTS))

# Servir arquivos estáticos
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def root():
    # resetar as listas sempre que a página principal for servida
    reset_data()
    return FileResponse(static_dir / "index.html")


@app.get("/index.html")
async def index_html():
    # também resetar se o cliente requisitar /index.html diretamente
    reset_data()
    return FileResponse(static_dir / "index.html")


def reset_data():
    users.list = list(ORIGINAL_USERS)
    elements.list = list(ORIGINAL_ELEMENTS)


@app.post("/api/reset")
async def api_reset():
    reset_data()
    return {"status": "ok", "message": "listas resetadas"}

@app.get("/api/users")
async def get_users():
    return {"users": users.list}

@app.get("/api/elements")
async def get_elements():
    return {"elements": elements.list}

@app.post("/api/draw/user")
async def draw_user():
    return {"user": users.doorPrize()}

@app.post("/api/draw/element")
async def draw_element():
    return {"element": elements.doorPrizePokemon()}


class Command(BaseModel):
    comando: str


@app.post("/api/command")
async def handle_command(cmd: Command):
    c = cmd.comando.strip().lower()
    # listar usuários
    if c in ("listar", "listar users", "listar usuarios"):
        return {"output": "Usuarios:\n" + "\n".join(users.list)}
    # listar elementos
    if c in ("listar elementos", "listar elements", "pokemons"):
        return {"output": "Elementos:\n" + "\n".join(elements.list)}
    # sortear usuário
    if c in ("pop user", "pop usuario", "pop", "sortear usuario", "sorteio usuario", "sorterio"):
        return {"output": users.doorPrize()}
    # sortear elemento
    if c in ("pop element", "pop elemento", "sortear elemento"):
        return {"output": elements.doorPrizePokemon()}
    
    if c in ("comandos", "help"):
        return {"output": "Comandos disponíveis:\n- listar\n- listar users\n- sortear usuario \n-  listar elementos\n- pokemons \n- pop user\n- pop element\n- help"}

    return {"output": "Comando não reconhecido. Use 'listar' ou 'pop'."}

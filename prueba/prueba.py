import reflex as rx
import os
import dotenv
from supabase import create_client, Client


# url: str = "https://gcjyhrlcftbkeaiqlzlm.supabase.co"
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjanlocmxjZnRia2VhaXFsemxtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3MjQ3NzAsImV4cCI6MjAzMTMwMDc3MH0.MFsm9DJ9XnVnsTUK-N2SsCBf8wnhW03mGp5d2Z2Jf9Q"

# class Horarios(rx.Base):
#     id = int
#     horario = int
#     cant_users = int
    

# class Supabase:
    
#     dotenv.load_dotenv()
    
#     SUPABASE_URL = os.environ.get("SUPABASE_URL")
#     SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    
#     client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
#     def __init__(self) -> None:
#         if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
#             self.supabase: Client = create_client(
#                 self.SUPABASE_URL, self.SUPABASE_KEY
#             )
    
    
#     def data(self):
#         data_list = []
#         response = self.client.table('Horarios').select("*").execute()
#         if len(response.data) > 0:
#             for i in response.data:
#                 data_list.append(Horarios(id=i["id"], horario=i["horario"], cant_users=i["cant_users"]))
#         return data_list
    
#     def horarios(self):
#         horarios=[]
#         data = self.data()
#         for i in data:
#             horarios.append(i.horario)
#         horarios.sort()
#         return horarios
                
#     def unico_horario(self, id):
#         data = self.data()
#         for i in data:
#             if i.id == id:
#                 return i.horario
        
#     def subir_contador(self, id, contador):
#         data, count = self.client.table('Horarios').update({'cant_users': contador}).eq('id', id).execute()
    
#     def reservar_horario(self, id:int):
#         data = self.data()
#         for i in data:
#             if i.id == id:
#                 contador = i.cant_users
#                 contador += 1
#                 if contador <= 4:
#                     self.subir_contador(id, contador)
#                 else : print("la clase esta llena")
                
#     def reservar(self, id:int):
#         cant = self.client.table('Horarios').select("*").execute()
#         for i in cant.data:
#             if i["id"] == id:
#                 contador = i["cant_users"]
#                 contador += 1
#                 if i["cant_users"] < 4:
#                     actualizar = self.client.table('Horarios').update({'cant_users': contador}).eq('id', id).execute()
#                 else:
#                     print("la clase está llena")
                
    
                


# supabase = Supabase()


# class Estados(rx.State):
#     color: str = "green"
#     data_info: list = [Horarios]
    
#     def _init_(self):
#         self.horarios = supabase.data()
    
#     async def reservar_horario(self, id):
#         reservar_el_horario = reservar_horario(id)
#         return reservar_el_horario
    
#     async def data(self):
#         self.data_info = await data()
#         print(self.data_info)
        
#     async def reservar_turno(self, id: int) -> list:
#         supabase.reservar_horario(id)
#         self.horarios = supabase.data()
        


# async def data():
#     return supabase.data()

# async def reservar_horario(id):
#     return supabase.reservar_horario(id)





# @rx.page(
#     title="turnos",
#     description="Taller de ceramica",
#     on_load=Estados.data
# )
# def index() -> rx.Component:
#     return rx.center(
#             rx.vstack(
#                 button(1),
#                 button(2),
#                 button(3),
#                 button(4),
#                 button(5)
#             )
#         )
    

# def button(id):
#     return rx.button(
#         rx.text(supabase.unico_horario(id)),
#         color_scheme=Estados.color,
#         on_click=Estados.reservar_horario(id)
#     )

# async def hola(user: str) -> str:
#     if user == "juli":
#         return "hello juli"
#     elif user == "cami":
#         return "hello cami"
#     elif user == "theo":
#         return "hello theo"
#     elif user == "viejo":
#         return "hello viejo"
#     elif user == "vieja":
#         return "hello vieja"

# app = rx.App()
# app.add_page(index)

# app.api.add_api_route("/hola/{user}", hola)

# if __name__ == "__main__":
#     print("Current working directory:", os.getcwd())
#     app._compile()



class Horarios(rx.Base):
    id = int
    horario = int
    cant_users = int

class Supabase():
    dotenv.load_dotenv()
    
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
   
    client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def unico_horario(self, id: int):
        data = self.data()
        for i in data:
            if i.id == id:
                return i.horario

    def data(self):
        data_list = []
        response = self.client.table('Horarios').select("*").execute()
        if len(response.data) > 0:
            for i in response.data:
                data_list.append(Horarios(id=i["id"], horario=i["horario"], cant_users=i["cant_users"]))
        return data_list

    def cant_users(self, id) -> list:
        data = self.data()
        for i in data:
            if i.id == id:
                self.usuarios_maximos = i.cant_users
                return self.usuarios_maximos

    def check_cant_users(self, id):
        if self.cant_users(id) < 4:
            return True
        return False

    def reservar(self, id:int):
        data = self.data()
        for i in data:
            if i.id == id:
                contador = i.cant_users
                contador += 1
                if i.cant_users < 4:
                    actualizar = self.client.table('Horarios').update({'cant_users': contador}).eq('id', id).execute()
                else:
                    print("la clase está llena")
    
    def cancelar(self, id:int) -> rx.Component:
        cant = self.client.table('Horarios').select("*").execute()
        for i in cant.data:
            if i.id == id:
                contador = i.cant_users
                contador -= 1
                if i.cant_users >= 0:
                    actualizar = self.client.table('Horarios').update({'cant_users': contador}).eq('id', id).execute()
                
        

supabase = Supabase()


class Reserva_cancela(rx.State):
    async def reservar_turno(self, id: int) -> list:
        reservar_la_clase = supabase.reservar(id)
        return reservar_la_clase
    
    async def cancelar_turno(self, id: int) -> list:
        cancelar_turno = supabase.cancelar(id)
        return cancelar_turno
        


class Color():
    color_red: str = "red"
    color_green: str = "green"

color = Color()

@rx.page(
    title="turnos",
    description="Taller de cerámica",
)
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            button(1),
            button(2),
            button(3),
            button(4),
            button(5),
            button(5)
        )
    )

def button_green(text, click, id) -> rx.Component:
    return rx.button(
        rx.text(text),
        on_click=click,
        color_scheme=color.color_green
    )

def button_red(text, id) -> rx.Component:
    return rx.center(rx.button(
        rx.text(text),
        disabled=True,
    ),
    rx.button(
        rx.text("¿Cancelar esta clase?"),
        on_click=Reserva_cancela.cancelar_turno(id)
        ),
    rx.vstack(
        rx.text("(Si no cancelas con un dia de anticipacion",
            size="1",
            spacing="0px",
            padding="0px",
            margin="0px"),
        rx.text("no podras recuperar la clase)",
                size="1",
                spacing="0px",
                padding="0px",
                margin="0px"
            )
        )
    )

def button(id):
    return rx.cond(supabase.check_cant_users(id),
                   button_green(f"Turno de las {supabase.unico_horario(id)}", Reserva_cancela.reservar_turno(id), id),
                   button_red(f"Turno de las {supabase.unico_horario(id)}", id)

                )  
    
app = rx.App()
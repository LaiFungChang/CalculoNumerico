import flet as ft
#Estilo del boton
class boton_stilo(ft.ElevatedButton):
    def __init__(self, text, on_click,width):
        super().__init__()
        self.bgcolor = '#006BBA'
        self.color = ft.colors.WHITE
        self.text = text
        self.on_click = on_click
        self.width =width
        
#code display the code
def main_enunciado_1(page: ft.Page):
    #parametros de la pagina
    page.title = "Convertidor de bases" #title of the page
    page.window_resizable = False
    page.window_width = 600
    page.window_height = 630
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding =0
    page.window_center()

    #funciones
    def validacionInput(e): #validacion de entrada: solo permite el ingreso de numeros enteros del 0-9
        if (e.control.value != ''):
            if not(e.control.value[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                e.control.value =e.control.value[:-1]
                e.control.update()

    def conversor(e): #convierte los numeros
        """
        txt_number: input ingresado por el usuario.
        valores: lista de bases a elegir por el usuario para realizar conversion
        n: tamaño de base
        
        se introducira un numero entero el cual sera convertido en las siguientes bases:
        *binario(2)    * hexadecimal(16)    *cuarternario(4)
        *octal(8)      * terciario(3)

        """
        txt_number.read_only =True #no permite que el input se edite
        #valor de base
        if valores.value != "HEX" and (txt_number.value != "") :
            if valores.value =="BIN":
                n =2
            elif valores.value =="Base 3":
                n=3
            elif valores.value=="Base 4":
                n=4
            elif valores.value=="OCT":
                n=8

            #PROCEDIMIENTO DE CAMBIO DE BASE
            numero = int(txt_number.value) #convierte el textField en int
            lista = [] #almacena el numero que se convertira
            
            while(numero > 0): #ciclo donde se convierte numero deseado
                lista.append(str(numero % n)) #agrega resto a la lista
                numero //= n #calcula cociente
       
            result.value = ''.join(lista[::-1]) # [::-1] orden inverso
            result.update() #actualiza resultado obtenido

        elif valores.value=="HEX" and (txt_number.value != ""):
                n=16
                result.value = hex(int(txt_number.value))[2:].upper() #conversion a hexadecimal

    #valida cuando el input= textField esta vacio y responde con un mensaje de error
        else:
            txt_number.error_text="No a ingresado un número" #mensaje de error
        page.update()#actualiza la pagina

    def limpiar(e): #limpia informacion
        txt_number.read_only = False #permite que se edite el input
        txt_number.value = "" #limpia input
        result.value ="" #limpia output
        page.update() #actualiza la pagina

    #VARIABLES
    txt_number = ft.TextField(hint_text="0", text_align=ft.TextAlign.RIGHT, width=150,label="Ingresa un numero", on_change=validacionInput)
    result = ft.TextField(hint_text="0",text_align=ft.TextAlign.RIGHT,width=260)  #respuesta de operacion
    result.read_only =True #no se puede editar 
    valores = ft.Dropdown(
                    value="BIN", #valor predeterminado binario
                    width=100,
                    options=[ #BASES
                        ft.dropdown.Option("BIN"),
                        ft.dropdown.Option("Base 3"),
                        ft.dropdown.Option("Base 4"),
                        ft.dropdown.Option("OCT"),
                        ft.dropdown.Option("HEX"),
                    ],
                )
    #DISEÑO DE VENTANA 1: Enunciado 1
    page.add( 
        ft.Container( #container Principal
                #Propiedades externas 
                gradient= ft.LinearGradient(begin=ft.alignment.top_left,end=ft.alignment.top_right,colors=['#006BBA','#0E9DBC']),
                width=page.window_width,
                height=page.window_height,
                padding=ft.padding.symmetric(vertical=50,horizontal=45), 
                content=ft.Container( #container secundario
                        #propiedades internas del container 2
                        bgcolor="white",
                        border_radius=10,
                        padding= ft.padding.only(top=30),
                        margin= ft.margin.all(60),
                        content= ft.Column([
                                    ft.Text("          Conversor de Bases",size=25,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                                    ft.Text(""), #espacio 
                                    ft.Row(
                                    [
                                        txt_number,
                                        valores
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    ),      
                                    ft.Row(
                                        [
                                            result
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Text(""), #espacio
                                    ft.Row(
                                        [
                                            ft.IconButton(ft.icons.CLEANING_SERVICES, on_click=limpiar),
                                            boton_stilo(text="Calcular", on_click=conversor, width=135)
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    ),
                                ]),
                            ),
                ),
    )
ft.app(main_enunciado_1)
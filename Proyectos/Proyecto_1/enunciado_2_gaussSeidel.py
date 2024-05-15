import flet as ft
import numpy as np
#code display the code
def main_enunciado_2(page: ft.Page):
    #parametros de la pagina
    page.title = "Operacion de matrices: Gauss-seidel" #title of the page
    page.window_resizable = False
    #dimensiones
    page.window_width = 1000
    page.window_height = 630
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding =0
    page.window_center()

    def validacionInput(e): #validacion de entrada
        if (e.control.value != ''):
            if not(e.control.value[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                e.control.value =e.control.value[:-1]
                e.control.update()

    def limpiar(e): #Limpia toda la operacion junto a los elementos de la matriz y vectores
        for elemento in [c11,c12,c13,c21,c22,c23,c31,c32,c33,v1,v2,v3,x,y,z]:
            elemento.value = ''
            elemento.update() #actualiza elemento
        page.update() #actualiza pagina
         
    def gauss_seidel(a, b, x0, tol=1e-6, max_iterations=1000): #operacion gauss-seidel
        n = len(a)
        x1 = np.copy(x0)
        x_new = np.zeros_like(x1)
        iterations = 0
        error = tol + 1
        
        while error > tol and iterations < max_iterations:
            for i in range(n):
                # Calcula la suma de los productos de los coeficientes y las soluciones conocidas
                sum1 = np.dot(a[i, :i], x_new[:i])      
                sum2 = np.dot(a[i, i + 1:], x1[i + 1:])
                
                # Calcula la nueva estimación de la solución
                x_new[i] = (b[i] - sum1 - sum2) / a[i, i]
            
            # Calcula el error como la norma L2 de la diferencia entre x y x_new
            error = np.linalg.norm(x_new - x1, ord=2) 
            x1 = np.copy(x_new) # Actualiza x con la nueva estimación
            iterations += 1
        
        return x1 #respuesta de operacion
         
    def calcular(e):    
        #validacion string no vacio
        if(c11.value != '' and c12.value != '' and c13.value != '' and c21.value != '' and c22.value != '' and c23.value != '' and c31.value != '' and c32.value != '' and c33.value != '' and v1.value != '' and v2.value != '' and v3.value != ''):   
            #TENER EN CUENTA: se puede optimizar esta parte mediante un ciclo for
            
            a = [] ; b = [] #matriz y vector empleando numpy= np
            variable_matriz_A = [ #se adjuntan los elementos de la matriz A para optimizar el codigo mediante un for
            [c11.value, c12.value, c13.value],
            [c21.value, c22.value, c23.value],
            [c31.value, c32.value, c33.value]
            ]
            variable_vector_b=[v1.value,v2.value,v3.value] #se adjunta los elementos del vecto B para optimizar codigo meidante un for
            #Cambio de textField a float mediante ciclos comprimidos
            a= np.array([[float(element) for element in row] for row in variable_matriz_A]) 
            b= np.array([float(elemento) for elemento in variable_vector_b])
            x0 = np.zeros(3) #matriz de ceros
            solucion = gauss_seidel(a, b, x0) #llama a la funcion y realiza la operacion
            #asigna los valores a los elementos del vector x, es decir la respuesta y lo redondea a 3 decimales
            x.value = round(solucion[0],3)
            y.value = round(solucion[1],3)
            z.value = round(solucion[2],3)
            page.update() #actualiza la pagina
        else: #se cumple esta condicion cuando algun elemento no a sido rellenado por el usuario
            mensaje =ft.AlertDialog(title=ft.Text('Casillas vacias')) #messageBox error
            page.dialog = mensaje 
            mensaje.open= True #mensaje mostrar
            page.update() #actualiza pagina

    #VARIABLES
    #matriz A celdas: se puede hacer mediante un ciclo for, limitado por el fondo degradado
    c11 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)
    c12 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)
    c13 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)

    c21 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)
    c22 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)
    c23 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)

    c31 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)
    c32 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)
    c33 = ft.TextField(width=55,height=50,text_size=13, on_change=validacionInput)

    #VECTOR b: se puede hacer mediante un ciclo for, limitado por el fondo degradado
    v1= ft.TextField(width=60,height=50,text_size=13, on_change=validacionInput)
    v2= ft.TextField(width=60,height=50,text_size=13, on_change=validacionInput)
    v3= ft.TextField(width=60,height=50,text_size=13, on_change=validacionInput)
   
    #respuesta X: se puede hacer mediante un ciclo for, limitado por el fondo degradado
    x= ft.TextField(width=80,height=50,read_only=True,text_size=13)
    y= ft.TextField(width=80,height=50,read_only=True,text_size=13)
    z= ft.TextField(width=80,height=50,read_only=True,text_size=13)

    #posicion de matriz A, Vector b y repsuesta de icognita vector X
    fila_title = ft.Row(controls=[ft.Text("Matriz A                                b                          x ",size=20,weight=ft.FontWeight.BOLD)],
                         alignment= ft.MainAxisAlignment.SPACE_EVENLY
                        )
    fila_1 = ft.Row(
                controls=[c11,c12,c13,ft.Text("                  "),v1,ft.Text("                  "),x],
                alignment= ft.MainAxisAlignment.CENTER
            )
    fila_2 = ft.Row(
                controls=[c21,c22,c23,ft.Text("                  "),v2,ft.Text("                  "),y],
                alignment= ft.MainAxisAlignment.CENTER
            )
    fila_3 = ft.Row(
                controls=[c31,c32,c33,ft.Text("                  "),v3,ft.Text("                  "),z],
                alignment= ft.MainAxisAlignment.CENTER
            )
    contenedor_1 = ft.Column( #se agregan los rows dentro de una columna para mantener un orden
                    controls=[fila_title,fila_1,fila_2,fila_3]
            )
    page.add( #diseño de pagina 2
        ft.Container(
                #TENER EN CUENTA:El fondo degradado limita procesos de optimizacion del codigo
                #propiedades generales
                gradient= ft.LinearGradient(begin=ft.alignment.top_left,end=ft.alignment.top_right,colors=['#006BBA','#0E9DBC']),
                width=page.window_width,
                height=page.window_height,
                padding=ft.padding.symmetric(vertical=50,horizontal=45),
                content=ft.Container( 
                        #propiedades internas del container 2
                        bgcolor="white",
                        border_radius=10,
                        padding= ft.padding.only(top=35),
                        margin= ft.margin.all(60),
                        content= ft.Column([
                                ft.Row(
                                    [
                                        ft.Text("GAUSS-SEIDEL",size=25,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD), 
                                    ],
                                    alignment= ft.MainAxisAlignment.CENTER
                                ),   
                                ft.Text(""), #espacio 
                                contenedor_1,  
                                ft.Row([
                                    ft.ElevatedButton(text="limpiar",on_click=limpiar),
                                    ft.ElevatedButton(text="Calcular",on_click=calcular),
                                ],
                                alignment=  ft.MainAxisAlignment.SPACE_AROUND
                                )
                        ]),
                ),
        ),
    )
ft.app(main_enunciado_2)
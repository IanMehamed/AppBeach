
class Jugador:
	def __init__(self,idcont):
		self.id=idcont
		

	def cargardatos(self):
		self.nombre=input("Ingrese Nombre y Apellido: ")
		self.telefono=int(input("Ingrese su numero de telefono: "))
		self.mail=input("Ingrese su email: ")
		self.rank=0
		self.genero=input("Ingrese su genero con 'M' o 'F': ")
		self.fnac=(int(input("ingrese Dia de Nacimiento: ")),int(input("Ingrese (Con Numero) el mes: ")),int(input("Ingrese el año: ")))


	def mostrardatos(self):
		print("Datos del atleta:",self.nombre)
		print("ID:",self.id)
		print("Mail:",self.mail)
		print("Puntos de Ranking:",self.rank)
		if self.genero =="M":
			print("Genero: Masculino")
		else:
			print("Genero: Femenino")
		print("Fecha de Nacimiento: ",self.fnac[0],self.fnac[1],self.fnac[2],sep="/")


class Torneo:
	def __init__(self,idcont):
		self.id=idcont
		self.equiposmasc=[]
		self.equiposfem=[]
		self.resultadosmasc=[]
		self.resultadosfem=[]

	def cargardatos(self):
		self.nombre=input("Ingrese el nombre del torneo: ")
		self.ubicacion=input("Ingrese la ciudad donde se llevará a cabo: ")
		self.categoria=input("Ingrese la Categoria: ")
		self.cupo=int(input("Ingrese el cupo máximo por rama: "))	
		self.fecha=(int(input("ingrese Dia: ")),int(input("Ingrese (Con Numero) el mes: ")),int(input("Ingrese el año: ")))

	def mostrardatos(self):
		print("Datos del Torneo:",self.nombre)
		print("ID:",self.id)
		print("Ubicacion: ",self.ubicacion)
		print("Categoria: ",self.categoria)
		print("Cupo Maximo: ",self.cupo)
		print("Fecha: ",self.fecha[0],self.fecha[1],self.fecha[2],sep="/")
		print("Equipos Masculinos Anotados:",self.equiposmasc)
		print("Equipos Femeninos Anotados:",self.equiposfem)

	def mostrarresultados(self):
		print("Resultados Masculino")
		print("---------------------------------------------------------------------")
		print(self.resultadosmasc)
		print("Resultados Femenino")
		print("---------------------------------------------------------------------")
		print(self.resultadosfem)
		

		

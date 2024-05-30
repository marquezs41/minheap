import math

class Paciente:
    def __init__(self, id_paciente, genero, nombre, edad, triaje):
        self.id_paciente:int = id_paciente
        self.genero:str = genero
        self.nombre:str = nombre
        self.edad:int = edad
        self.triaje:int = triaje
        self.llegada:int = None 
    
    def __repr__(self):
        return f'Paciente({self.id_paciente}, {self.nombre}, {self.edad}, Triaje {self.triaje}, Llegada {self.llegada})'
    
    
class NodoPaciente:

  def __init__(self, paciente:Paciente):
    self.paciente = paciente
    self.parent = None
    self.leftchild = None
    self.rightchild = None
    
class min_heap:
  
  def __init__(self):
    self.root:NodoPaciente = None
    self.orden = 0
    self.nivelBusqueda = 0
    self.nodoBusqueda:NodoPaciente = None
  
  def print_recursivo(self, nodo:NodoPaciente, nivel):
    prefix = ''
    for i in range(nivel):
      prefix = prefix + '|--'
        
    print(prefix + str(nivel) + str(nodo.paciente))
    
    if nodo.leftchild is not None:
      self.print_recursivo(nodo.leftchild, nivel + 1)
      
    if nodo.rightchild is not None:
      self.print_recursivo(nodo.rightchild, nivel + 1)

  def consulta_Triaje_recursivo(self, nodoActual:NodoPaciente, triaje):
    if nodoActual.paciente.triaje == triaje:
      print(str(nodoActual.paciente))

    #consultar los hijos
    if nodoActual.leftchild is not None:
      self.consulta_Triaje_recursivo(nodoActual.leftchild, triaje)

    if nodoActual.rightchild is not None:
      self.consulta_Triaje_recursivo(nodoActual.rightchild, triaje)     

  def consulta_Triaje(self, triaje):
    print("Pacientes con triaje " + str(triaje))
    self.consulta_Triaje_recursivo(self.root, triaje)

  def proximoPaciente(self):
    print(str(self.root.paciente))

  def buscarPadreDisponible(self, nodoActual:NodoPaciente, nivel:int):
    if nodoActual.leftchild is None or nodoActual.rightchild is None:
      #El nodo actual tiene disponible para adicionar hijo, pero solo es valido si no existe otro padre de menor nivel
      if nivel < self.nivelBusqueda:
        self.nivelBusqueda = nivel
        self.nodoBusqueda = nodoActual
    else:
      #Buscar un nodo disponible en recursivamente
      self.buscarPadreDisponible(nodoActual.leftchild, nivel + 1)
      self.buscarPadreDisponible(nodoActual.rightchild, nivel + 1)

  def insert_nodo(self, nodoNuevo:NodoPaciente):
    if self.root.leftchild is None:
      nodoNuevo.parent = self.root
      self.root.leftchild = nodoNuevo
    elif self.root.rightchild is None:
      nodoNuevo.parent = self.root
      self.root.rightchild = nodoNuevo
    else:
      self.nivelBusqueda = 99999
      self.nodoBusqueda = None
      self.buscarPadreDisponible(self.root, 0)
      nodoNuevo.parent = self.nodoBusqueda
      if self.nodoBusqueda.leftchild is None:
        self.nodoBusqueda.leftchild = nodoNuevo
      else:
        self.nodoBusqueda.rightchild = nodoNuevo

  def intercambiar(self, nodo1:NodoPaciente, nodo2:NodoPaciente):
    paciente = nodo1.paciente
    nodo1.paciente = nodo2.paciente
    nodo2.paciente = paciente

  def minHeap(self, nodo:NodoPaciente):
    if nodo.parent is not None:
      if nodo.paciente.triaje < nodo.parent.paciente.triaje or (nodo.paciente.triaje == nodo.parent.paciente.triaje and nodo.paciente.llegada < nodo.parent.paciente.llegada):
        self.intercambiar(nodo, nodo.parent)
        self.minHeap(nodo.parent)

  def insert(self, paciente:Paciente):
    # orden de llegada del paciente
    self.orden = self.orden + 1
    paciente.llegada = self.orden
    newNodo = NodoPaciente(paciente)
    # adicionar el nodo al arbol
    if self.root is None:
      self.root = newNodo
    else:
      self.insert_nodo(newNodo)
      self.minHeap(newNodo) 
  
  def buscarUltimoNodo(self, nodoActual:NodoPaciente, nivel:int):
    if nivel >= self.nivelBusqueda:
      self.nivelBusqueda = nivel
      self.nodoBusqueda = nodoActual
    
    if nodoActual.leftchild is not None:
      self.buscarUltimoNodo(nodoActual.leftchild, nivel + 1)

    if nodoActual.rightchild is not None:
      self.buscarUltimoNodo(nodoActual.rightchild, nivel + 1)

  def eliminarNodo(self, nodo:NodoPaciente):
    self.nivelBusqueda = 0
    self.nodoBusqueda = None
    self.buscarUltimoNodo(self.root, 0)

    #Desconectar el ultimo nodo que pasa a reemplazar el nodo a eliminar
    if self.nodoBusqueda != self.root:
      if self.nodoBusqueda.parent.leftchild == self.nodoBusqueda:
        self.nodoBusqueda.parent.leftchild = None
      elif self.nodoBusqueda.parent.rightchild == self.nodoBusqueda:
        self.nodoBusqueda.parent.rightchild = None 

    #Reemplazar por el ultimo ingresado y reubicar el nodo segun el triaje y la llegada
    if self.nodoBusqueda == self.root:
      self.root = None
    elif self.nodoBusqueda != nodo:
      self.intercambiar(nodo,self.nodoBusqueda)
      self.minHeap_inverso(nodo)
    
    

  def minHeap_inverso(self, nodoActual:NodoPaciente):
    hijoIzq:NodoPaciente = nodoActual.leftchild
    hijoDer:NodoPaciente = nodoActual.rightchild
    hijoCambio:NodoPaciente = None
    
    if hijoDer is not None and hijoIzq is not None and hijoIzq.paciente.triaje == hijoDer.paciente.triaje and nodoActual.paciente.triaje > hijoDer.paciente.triaje:
      if hijoIzq.paciente.llegada > hijoDer.paciente.llegada:
        hijoCambio = hijoDer
      else:
        hijoCambio = hijoIzq
    elif hijoDer is not None and hijoIzq is not None and hijoIzq.paciente.triaje < nodoActual.paciente.triaje and hijoDer.paciente.triaje < nodoActual.paciente.triaje:      
      if hijoIzq.paciente.triaje < hijoDer.paciente.triaje:
        hijoCambio = hijoIzq
      elif hijoIzq.paciente.triaje == hijoDer.paciente.triaje:
        if hijoIzq.paciente.llegada < hijoDer.paciente.llegada:
          hijoCambio = hijoIzq
        else:
          hijoCambio = hijoDer
      else:
        hijoCambio = hijoDer

    elif hijoIzq is not None and hijoIzq.paciente.triaje < nodoActual.paciente.triaje:
      hijoCambio = hijoIzq
    elif hijoDer is not None and hijoDer.paciente.triaje < nodoActual.paciente.triaje:
      hijoCambio = hijoDer
    elif hijoIzq is not None and hijoIzq.paciente.triaje == nodoActual.paciente.triaje and hijoIzq.paciente.llegada < nodoActual.paciente.llegada:
      hijoCambio = hijoIzq
    elif hijoDer is not None and hijoDer.paciente.triaje == nodoActual.paciente.triaje and hijoDer.paciente.llegada < nodoActual.paciente.llegada:
      hijoCambio = hijoDer
      
    if hijoCambio is not None:
      self.intercambiar(hijoCambio, nodoActual)
      self.minHeap_inverso(hijoCambio)

  def atender(self):
    print("Atender el paciente: ")
    self.proximoPaciente()
    self.eliminarNodo(self.root)

  def buscarPaciente_id(self, nodoActual:NodoPaciente, idPaciente:int):
    if nodoActual.paciente.id_paciente == idPaciente:
      return nodoActual
    else:
      #buscar en los hijos
      nodoEncontrado:NodoPaciente = None
      if nodoActual.leftchild is not None and nodoEncontrado is None:
        nodoEncontrado = self.buscarPaciente_id(nodoActual.leftchild, idPaciente)

      if nodoActual.rightchild is not None and nodoEncontrado is None:
        nodoEncontrado = self.buscarPaciente_id(nodoActual.rightchild, idPaciente)
      
      return nodoEncontrado

  def eliminarPaciente_id(self, id:int):
    buscar = 1
    while buscar > 0:
      nodoEncontrado = self.buscarPaciente_id(self.root, id)
      if nodoEncontrado is not None:
        self.eliminarNodo(nodoEncontrado)
      else:
        buscar = 0  

  def buscarPaciente_nombre(self, nodoActual:NodoPaciente, nombre):
    if nodoActual.paciente.nombre == nombre:
      return nodoActual
    else:
      #buscar en los hijos
      nodoEncontrado:NodoPaciente = None
      if nodoActual.leftchild is not None and nodoEncontrado is None:
        nodoEncontrado = self.buscarPaciente_nombre(nodoActual.leftchild, nombre)

      if nodoActual.rightchild is not None and nodoEncontrado is None:
        nodoEncontrado = self.buscarPaciente_nombre(nodoActual.rightchild, nombre)
      
      return nodoEncontrado
    
  def eliminarPaciente_nombre(self, nombre):
    buscar = 1
    while buscar > 0:
      nodoEncontrado = self.buscarPaciente_nombre(self.root, nombre)
      if nodoEncontrado is not None:
        self.eliminarNodo(nodoEncontrado)
      else:
        buscar = 0   

"""
tree = min_heap()
tree.insert(Paciente(12233,'hombre','Pedro',67,4))
tree.insert(Paciente(12345,'mujer','Teresa',45,2))
tree.insert(Paciente(45678,'mujer','Sofia',15,4))
tree.insert(Paciente(56689,'mujer','Ana',45,3))
tree.insert(Paciente(56789,'mujer','Cecilia',25,2))
tree.insert(Paciente(78900,'mujer','Andrea',18,2))
tree.insert(Paciente(89012,'hombre','Jorge',47,3))
tree.insert(Paciente(90123,'mujer','Alejandra',21,3))
tree.insert(Paciente(23445,'mujer','Susana',10,1))
tree.insert(Paciente(34546,'homre','Julio',75,1))
tree.insert(Paciente(32456,'mujer','Antonia',29,4))
tree.insert(Paciente(54678,'mujer','Leonor',76,3))

tree.print_recursivo(tree.root, 0)

tree.eliminarPaciente_id(12233)

tree.print_recursivo(tree.root, 0)
"""
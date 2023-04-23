# Realizo el llamadoa a las librerias Open Cv2/ Y numpy
import cv2
import numpy as np

cap =cv2.VideoCapture(0,cv2.CAP_DSHOW) # Localiza el puerto de la camara

# recrea los el rango de los colores a capturar
celesteBajo = np.array([75,185,88], np.double)
celesteAlto = np.array([112, 255, 255], np.double)

# Colores para pintar
colorCeleste = (255, 113, 82)
colorAmarillo = (89,222, 255)
colorRosa = (128, 0, 255)
colorVerde = (0,255, 36)
colorNaranja = (26, 127, 239)
colorLimpiarPantalla = (255,255,255)

# Grosor de las figuras de colores
grosorCeleste = 6
grosorAmarillo = 2
grosorRosa = 2
grosorVerde = 2
grosorNaranja = 2
#grosorLimpiarPanttalla = 2

# Grosor de las figuras del tamaño del grosor
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1

# Seleccion del color
color = colorCeleste

# Grosor de Inicio
grosor = 3

# Inicios del punto en nulo hasata capturar un nuevo valor
x1 = None
y1 = None
imAux = None

# Inicio de la apertura para la camara
while True:

	# Abre y carga la pantalla
	ret,frame = cap.read()
	if ret == False: break

	frame = cv2.flip(frame,1)
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	if imAux is None: imAux = np.zeros(frame.shape,dtype=np.uint8)

	#------------------------------------- Seccion Superior ---------------------
	# Cuadraos de la parte superior izquierda ( Representa los colores para dibujar)
	cv2.rectangle(frame,(0,1),(30,30),colorAmarillo,grosorAmarillo)
	cv2.rectangle(frame,(34,1),(64,30),colorRosa,grosorRosa)
	cv2.rectangle(frame,(68,1),(98,30),colorVerde,grosorVerde)
	cv2.rectangle(frame,(102,1),(132,30),colorNaranja,grosorNaranja)
	cv2.rectangle(frame,(137,1),(170,30),colorCeleste,grosorCeleste)

	# Limpiador de Pantalla, (Limpia la Pantalla)
	cv2.rectangle(frame,(400,1),(250,30),colorLimpiarPantalla,2)
	cv2.putText(frame,'Limpiar',(295,13),6,0.6,colorLimpiarPantalla,1,cv2.LINE_AA)
	cv2.putText(frame,'Pantalla',(295,27),6,0.6,colorLimpiarPantalla,1,cv2.LINE_AA)

	# Dibujo para el Grosor (Parte superior Derecha)
	cv2.circle(frame,(515,20),3,(0,0,0),-1)
	cv2.circle(frame,(563,20),6,(0,0,0),-1)
	cv2.circle(frame,(613,20),9,(0,0,0),-1)

	maskCeleste = cv2.inRange(frameHSV,celesteBajo,celesteAlto)
	#maskCeleste = cv2.erode(maskCeleste,None,iterations=1)	
	#-----------------------------------------------------------------------------------
	# Para que o grafique en la pantalla auxiliar tambien se grafique en el video)
	maskCeleste = cv2.dilate(maskCeleste,None,iterations=6)
	maskCeleste = cv2.medianBlur(maskCeleste,15)

	cnts, _ = cv2.findContours(maskCeleste,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
	for c in cnts:
		area = cv2.contourArea(c)
		if area > 1000:
			x,y2,w,h = cv2.boundingRect(c)
			cv2.rectangle(frame,(x,y2),(x+w,y2+h),(0,255,0),2)
			x2 = x + w//2

			# Selecciones de las opiciones de color y grosor que definimos en la pantalla
			if x1 is not None:
				# Posiciones de las figuras
				if 0 < x2 < 50 and 0 < y2 < 50:
					color = colorAmarillo
					grosorAmarillo = 6
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 2
					grosorNaranja = 2
				if 50 < x2 < 100 and 0 < y2 < 50:
					color = colorRosa
					grosorAmarillo = 2
					grosorRosa = 6
					grosorVerde = 2
					grosorCeleste = 2
					grosorNaranja = 2
				if 100 < x2 < 150 and 0 < y2 < 50:
					color = colorVerde
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 6
					grosorCeleste = 2
					grosorNaranja = 2
				if 150 < x2 < 200 and 0 < y2 < 50:
					color = colorCeleste
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 6
					grosorNaranja = 2
				if 200 < x2 < 250 and 0 < y2 < 50:
					color = colorNaranja
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 2
					grosorNaranja = 6
				if 490 < x2 < 550 and 0 < y2 < 50:
					grosor= 3
					grosorPeque = 6
					grosorMedio = 1
					grosorGrande = 1
				if 540 < x2 < 590 and 0 < y2 < 50:
					grosor= 6
					grosorPeque = 1
					grosorMedio = 6
					grosorGrande = 1
				if 490 < x2 < 550 and 0 < y2 < 50:
					grosor= 9
					grosorPeque = 1
					grosorMedio = 1
					grosorGrande = 6

				if 300 < x2 < 400 and 0 < y2 < 50:
					cv2.rectangle(frame,(400,1),(250,30),colorLimpiarPantalla,2)
					cv2.putText(frame,'Limpiar',(295,13),6,0.6,colorLimpiarPantalla,1,cv2.LINE_AA)
					cv2.putText(frame,'Pantalla',(295,27),6,0.6,colorLimpiarPantalla,1,cv2.LINE_AA)
					imAux = np.zeros(frame.shape,dtype=np.uint8)

				if 0 < y2 < 60 or 0 < y1 < 60:
					imAux = imAux
				else:
					imAux = cv2.line(imAux,(x1,y1),(x2,y2),color,grosor)
			cv2.circle(frame,(x2,y2),grosor,color,3)
			x1 = x2
			y1 = y2

		else:
			x1 = None
			y1 = None
		#-----------------------------------------------------------------------------------
	# Para que o grafique en la pantalla auxiliar tambien se grafique en el video
	imAuxGray = cv2.cvtColor(imAux,cv2.COLOR_BGR2GRAY)
	_ , th = cv2.threshold(imAuxGray,10,255,cv2.THRESH_BINARY)
	thInv = cv2.bitwise_not(th)
	frame = cv2.bitwise_and(frame,frame,mask=thInv)
	frame = cv2.add(frame,imAux)


	cv2.imshow('Pizarra', frame)
	cv2.imshow('imAux', imAux)
	#cv2.imshow('th',th)
	#cv2.imshow('thInv',thInv)
	cv2.imshow('Color A Detectar',maskCeleste)

	k = cv2.waitKey(1)
	if k == 27:
		break

cap.realese()
cap.destroyAllWindows()

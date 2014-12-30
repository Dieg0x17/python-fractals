#!/usr/env/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from argparse import ArgumentParser
import random
import sys
import time

argp = ArgumentParser(
prog='fractales.py',
usage="\n python fractales.py -h",												

description='Generador de fractales en formato imagen',
epilog='Copyright 2014 Diego Rasero (diegolo.r8 at gmail.com) bajo licencia GPL v3.0',
)

argp.add_argument('-o', '--output', dest='file', type=str, help="Nombre de la imagen de salida", default="fractal.png")
argp.add_argument('-a', dest='a', type=int, help="Altura de la imagen", default=512)
argp.add_argument('-w', dest='w', type=int, help="Anchura de la imagen", default=512)
argp.add_argument('-t', '--type', dest='type', type=str, help="Tipo de fractal a generar: j (conjunto de julia) m (conjunto de mandelbrot)", default='j')
argp.add_argument('-c', dest='c', type=str, help="Variación del conjunto '(1.23,2.23)'", default=None)
argp.add_argument('-p', dest='p', type=int, help="Profundidad del fractal", default=10)
argp.add_argument('--colors', dest='colors', type=str, help="Ruta a un archivo con los colores del fractal en formato RGBA un color en cada linea ej: (255,0,255,30) #ABCDEF #ABC", default=None)

args = argp.parse_args()

# Dimensiones
m=args.w
n=args.a

# Lista de colores ( se puede cargar desde un archivo linea a linea y aceptar diferentes formatos de color )
colors=[
"#58C892",
"#3FA473",
"#277952",
"#144C31",
"#092C1C",
"#5A96BE",
"#3F7496",
"#28536F",
"#163346",
"#0B1D29",
"#FFC070",
"#EBAB5A",
"#AE7A38",
"#6E4A1D",
"#402A0E",
"#FF9570",
"#EB7F5A",
"#AE5638",
"#6E321D",	
"#401A0E",
]

if (args.colors): # Cargar colores
    col=[]
    try:
        f=open(args.colors, 'r')
        for line in f.readlines():
            line=line.strip("\n")
            if line[0] == '#' and ( len(line)==7 or len(line)==4 ):
                col.append(line)
            else:
                try:
                    col.append( eval( line ) )
                except:
                    print "Formato de color incorrecto: "+str(line)+"\nEl formato debe ser (255,255,255,255) ó #FFFFFF ó #FFF"
        f.close()
        if col:
            colors=col
    except:
        print "Error al intentar leer el archivo: "+args.colors

if (args.c):
	c=eval(args.c)
else:
	c=(random.randrange(-2000,2000)/1000.0, random.randrange(-2000,2000)/1000.0	)

# Modulo ( radio de la circunferencia que delimita el fractal )
rad=2

def modulo(pto):
	return ( (pto[0]**2) + (pto[1]**2) )**(1/2.0)

def f(pto,c):
	return ( (pto[0]**2-pto[1]**2)+c[0] ,(2*pto[0]*pto[1])+c[1] )

def color(pto, c):
	""" Función para calcular el color del punto. """
	i=0 						# iterador del color
	aux=f(pto, c)				# 1ª imagen del punto
	if ( modulo(aux) < rad ):
		while ( modulo(aux) < rad  and i<args.p):
			aux=f(aux, c)
			i+=1
		return colors[ (i%len(colors)) ] # se devuelve un color de la lista de colores.

	else:
	 	return (0,0,0,0) # los que se vallan fuera a la primera se ponen de color transparente


def julia(im, mandelbrot,c):
	""" dibuja el conjunto de julia y el de mandelbrot"""
	inicio = time.time()
	if (mandelbrot):
		print"Generando conjunto de Maldenbrot:"
	else:
		print "Generando conjunto de Julia\nC: [ %f, %f ]" % (c[0],c[1])
	draw = ImageDraw.Draw(im)

	for x in range(m):
		for y in range(n):
			xi=(4.0*x/m)-2 
			yi=(4.0*y/n)-2
			if (mandelbrot): c= (xi,yi)
			draw.point( [(x,y)],  color( (  xi, yi  ) , c ))
			
		progress=(((x)*100.0)/(m))
		sys.stdout.write( "\rProgress:\t%.2f%%\t[%s]" %  (progress, '#'*int(progress/10)+"\0") )
		sys.stdout.flush()
	fin = time.time()
	print "\rProgress:\t100.00%\t[   Done  ] in "+str(fin-inicio)+" seconds"	
	del draw


def main():
	im = Image.new("RGBA", (m, n), (0,0,0,0)) # Genera una nueva imagen de tamaño m , n
	if (args.type.lower() == "m" or args.type.lower() == "mandelbrot"):
		julia(im,True,c)
	else:
		julia(im,False,c)

	im.save(args.file, "PNG")

if __name__== "__main__":
    main()

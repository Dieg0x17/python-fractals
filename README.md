![Alt text](https://raw.githubusercontent.com/Dieg0x17/python-fractals/master/mandelbrot.png "Mandelbrot ejemplo")
Fractales con python
===================
Este sencillo script en python genera imágenes en formato png de los conjuntos de Julia y de Mandelbrot.  

----------


<i class="icon-fire"></i>Como generar los fractales 
-------------
Puedes hacerte una idea del funcionamiento del script con el texto de ayuda.
```
// Mostrar el texto de ayuda.
$ python fractal.py -h
```
Creando el primer fractal.
![Alt text](https://raw.githubusercontent.com/Dieg0x17/python-fractals/master/fractal.png "Julia ejemplo")
```
// Generar un fractal conjunto de julia de 512x512 px, colores por defecto.
$ python fractal.py
```
#### <i class="icon-picture"></i> Generar conjunto de Julia
La opción -c es un número complejo que interviene en la formación del conjunto, si no se usa esta opción se genera aleatoriamente.
```
// Generar un fractal conjunto de julia de 512x512 px, colores por defecto.
$ python fractal.py -t julia -c "(0.285, -0.01)"
```

#### <i class="icon-picture"></i> Generar conjunto de Mandelbrot
```
// Generar un fractal conjunto de mandelbrot de 512x512 px, colores por defecto.
$ python fractal.py -t mandelbrot
```

#### <i class="icon-tint"></i> Configurar archivo de colores
```
$ python fractal.py --colors colorfile.txt
```
El archivo de colores "colorfile.txt" debe tener un color por linea en cualquiera de los siguientes formatos, pueden combinarse:
```
#F1E57A
#FE0
(255,255,255,100)
(255,0,0)
```
#### <i class="icon-hdd"></i> Nombre del archivo de salida

```
$ python fractal.py -o nombredemifractal.png
```

#### <i class="icon-resize-full"></i> Resolución de la imagen
Por el momento el ratio es 1:1 por lo que si se introduce una altura distinta a la anchura el fractal se genera deformado.
```
// -a Altura -w Anchura. 
$ python fractal.py -a 1024 -w 1024
```
> **Nota:**

> - Cuanta mayor resolución tenga la imagen más tiempo tardara en generarse el fractal.
> - Cuanta mayor profundidad se defina más tiempo tardara en generarse el fractal.
> - Puedes crear tu lista de colores.


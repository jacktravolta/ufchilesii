import requests
import json
import re
import datetime,os
import numpy as np
import os.path, time
from flask import Flask

#==========================================
# Title:  Extrae reportes de UF SII-cl y permite consultas por dia-mes-año
# Author: juan.espinoza.castro88@gmail.com
# Date:   02 may 2023
#==========================================

g_url   = "https://www.sii.cl/"
g_sys   = 404
g_path  = "./repo/"
g_meses = ["","Enero", "Febrero", "Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

g_err0 = '{"data": { "Error": "El formato de fecha debe ser /api/dd-mm-aaaa"}}'
g_err1 = '{"data": { "Error": "No se encontraron registros en SII.cl para el año AAAA"}}' 

g_port = 5555
g_host = "0.0.0.0"

### Genera URL segun año indicado, las url antes de 2012 son diferente se valida ###
def gen_url(aa):
    urld = "valores_y_fechas"
    if int(aa) < 2013:
       urld = "pagina/valores"
    return(g_url+urld+"/uf/uf"+ aa +".htm")

### Descarga el html de SII segun año indicado ###
def get_rp(url):
    header_gs = {'Accept': 'application/json'}
    r = requests.get(url,headers=header_gs)
    if r.ok:
        return r.text
    else:
        return g_sys

### Desde el html descargado se genera un archivo CSV Filtrado y procesando ###
def export_uf_a_csv(url,f):
    r = get_rp(url)
    if r == g_sys:
        return r
    else:
        r = r.split('\n')
        dataLstA = list()
        dataLstA=r
        d=0
        m=0
        f = open(f, 'w')
        f.write("0;1;2;3;4;5;6;7;8;9;10;11;12\n")

        for x in dataLstA:
            x = x.split('\n')
            ### expresión regular para extraer los datos ###
            regexp=">(.*)<"
            rRegExp = re.search(regexp, x[0], re.IGNORECASE)
            
            if rRegExp:
                r = rRegExp.group(1)
                if str(r.strip()) == "1" :
                   d=1
                if d!=0 and d<32:
                    if r != d and d!=0 and r!= "&nbsp;":
                        if m==0 and d!=0:
                            f.write("%s" % d)
                        else:
                            f.write(";%s" % r)
                        m=m+1 
                    elif r =="&nbsp;":
                        f.write(";0")  
                        m=m+1 
                    if r == '</tbody>':
                        break
            elif m>12:
                m=0
                f.write("\n") 
            elif d!=0 and d<32:
                d=d+1
        f.close()

### Lee la informacion de CSV segun corresponda y la convierte a un array ###
def import_uf_array(dd,mm,aa,f):
    if os.path.exists(f):
        arr=[] 
        arr = np.loadtxt(f,delimiter=";", dtype=str)
        r = (arr[dd][mm])
        return('{"data": { "dia": "'+str(dd)+'", "mes": "'+g_meses[mm]+'","anio": "'+str(aa)+'","UF": "'+str(r)+'"}}')
    else:
        return 404    

### Compara fecha modificacion de archivo reporte v/s fecha de la consulta, determina si se actualiza fichero ###
def comp_file(url,f):
    if os.path.exists(f):
        m = os.path.getmtime(f)
        fm = time.strftime('%Y-%m-%d', time.localtime(m))
        fa = datetime.datetime.now().strftime("%Y-%m-%d ")

        if fa.strip() == fm.strip():
           return True
        else:
           return(export_uf_a_csv(url,f))
    else:
        return(export_uf_a_csv(url,f))

### Inicio programa ###
def main(f):
    try:
        f   = f.split("-")
        dd  = int(f[0])
        mm  = int(f[1])
        aa  = str(f[2])
        url = gen_url(aa)
        f   = datetime.datetime.now().strftime(g_path+aa+".csv")
        r   = comp_file(url,f)

        if r == g_sys:
           return(g_err0)
        else:
           return(import_uf_array(dd,mm,aa,f))
    except:
        return g_err0


### script modo servicio ###
def service():
    app = Flask(__name__)

    @app.route('/')
    def none():
        return(g_err0)

    @app.route('/api/<string:f>/')
    def ini(f):
        return main(f)

    app.run(host=g_host, port=g_port)
service()



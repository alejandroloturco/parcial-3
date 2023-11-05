import os
import json
import xml.etree.ElementTree as et
from test import *

if not os.path.exists("bd"):
        os.mkdir("bd")
if not os.path.exists("bd/listado.json"):
    data=[]
    with open("bd/listado.json","w",encoding="utf-8") as folder:
        json.dump(data,folder) 
else:
    with open("bd/listado.json","r",encoding="utf-8") as data:
        data=json.load(data) 


validacion = acces()
while validacion:
    carpeta=os.getcwd()
    if carpeta.endswith(f"\infoPacs"):
        carpeta=carpeta.split(f"\infoPacs")[0]
        os.chdir(carpeta)    
    user={}
    print("""
    \r1-- Ingresar pacientes manualmente
    \r2-- Importar informacion de archivos 
    \r3-- Buscar pacientes
    \r4-- Ver todos los pacientes
    \r5-- Salir                 
        """)
    menu=validar_nums("Selecione la opcion deseada: ")
    if menu==1:
        user["id"] = int(validar_nums("Ingrese el documento de identidad: "))
        if search_user(data,user["id"]) == False:
                    print("ya se encuentra un paciente con ese documento")
                    continue
        user["nombre"] = validar_words("Nombre: ")
        user["apellido"] = validar_words("Apellido: ")
        
        print("""Genero
        \r1--Masculino
        \r2--Femenino""")
        sexo = validar_nums("Seleccione el numero correspondiente: ")
        if sexo == 1:
            user["sexo"] = "Maculino"
        if sexo == 2:
            user["sexo"] = "Femenino"
        user["edad"] = validar_nums("Edad: ")
        user["fetal"] = validar_nums("Fetal: ")
        user["a1c"] = validar_nums("a1c: ")
        print("""S-Window
        \r1--Si
        \r2--No""")
        s_window = validar_nums("Seleccione el numero correspondiente: ")
        if s_window == 1:
            user["S-window"] = "Si"
        if s_window == 2:
            user["S-window"] = "No"
        print("""Estado del paciente
              \r1--No diabetico
              \r2--Controlado
              \r3--No controlado""")
        estado = validar_nums("Seleccione la opcion adecuada: ")
        if estado == 1:
            user["estado"] = "No diabetico"
        if estado == 2:
            user["estado"] = "Controlado"
        if estado == 3:
            user["estado"] = "No controlado"
        user["ciudad"] = validar_words("Ciudad de domicilio: ") 
        data.append(user)
        

        with open("bd/listado.json","w",encoding="UTF-8") as folder:
            json.dump(data,folder, ensure_ascii= False,indent="\t")
        continue

    if menu==2:
        archivos_xml = [archivo for archivo in os.listdir("infoPacs")]
          
        for xml in archivos_xml:
                user={}
                os.chdir("infoPacs")
                archivo_xml = et.parse(xml)
                xml_edit = archivo_xml.getroot()
                user["id"] = int(xml_edit.find("id").text)
                
                if search_user(data,user["id"]) == False:
                    break

                user["nombre"] = xml_edit.find("name").text
                user["apellido"] = xml_edit.find("lastname").text
                user["sexo"] = xml_edit.find("sex").text
                user["edad"] = float(xml_edit.find("age").text)                
                user["fetal"] = float(xml_edit[6].find("F").text)
                user["a1c"] = float(xml_edit[6].find("a1c").text)
                user["S-window"] = xml_edit[6].find("s-win").text
                user["estado"] = xml_edit.find("dia").text
                user["ciudad"] = xml_edit.find("address").attrib.get("city") 
                
                data.append(user)
                carpeta=os.getcwd()
                if carpeta.endswith(f"\infoPacs"):
                    carpeta=carpeta.split(f"\infoPacs")[0]
                    os.chdir(carpeta)

                

                with open("bd/listado.json","w",encoding="utf-8") as folder:
                    json.dump(data,folder, ensure_ascii= False,indent="\t")
                continue         
                         
    if menu==3:
        
            if len(data) == 0:
                print("No hay pacientes registrados")
                continue
            else:
                id=int(validar_nums("Ingrese el documento del paciente que desea buscar: "))
                cont=0
                for i in data:
                    
                    
                    if i["id"] == id:
                        print(f'''
                              \rDocumento: {i["id"]}
                              \rName: {i["nombre"]}
                              \rLastname: {i["apellido"]}
                              \rAge: {i["edad"]}
                              \rGender: {i["sexo"]}
                              \rFetal: {i["fetal"]} - a1c: {i["a1c"]} - S-Win: {i["S-window"]} 
                              \rEstado: {i["estado"]}
                              \rCiudad: {i["ciudad"]}''')
                        cont=1
                        break
                if cont == 0:    
                    print("Paciente no registrado")
                    continue
                         
             
    if menu==4:
        if len(data) == 0:
            print("No hay pacientes registrados")
        else: 
            for i in data:
                print(f'''
                \rDocumento: {i["id"]}
                \rName: {i["nombre"]}
                \rLastname: {i["apellido"]}
                \rAge: {i["edad"]}
                \rGender: {i["sexo"]}
                \rFetal: {i["fetal"]} - a1c: {i["a1c"]} - S-Win: {i["S-window"]} 
                \rEstado: {i["estado"]}
                \rCiudad: {i["ciudad"]}''')
        continue       
            
    if menu==5:
        print('Ha salido del sistema')
        break
        
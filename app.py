import streamlit as st

# ---------------------------------
# Configuración de la página
# ---------------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo Juan Torres.png", width=300)


# ---------------------------------
# Diccionario de fechas
# ---------------------------------

fechas = {}

# AGOSTO
for i in [1,2]:
    fechas[f"{i:02d}"] = "12 de agosto"

for i in [3,4]:
    fechas[f"{i:02d}"] = "13 de agosto"

for i in [5,6]:
    fechas[f"{i:02d}"] = "14 de agosto"

for i in [7,8]:
    fechas[f"{i:02d}"] = "18 de agosto"

for i in [9,10]:
    fechas[f"{i:02d}"] = "19 de agosto"

for i in [11,12]:
    fechas[f"{i:02d}"] = "20 de agosto"

for i in [13,14]:
    fechas[f"{i:02d}"] = "21 de agosto"

for i in [15,16]:
    fechas[f"{i:02d}"] = "24 de agosto"

for i in [17,18]:
    fechas[f"{i:02d}"] = "25 de agosto"

for i in [19,20]:
    fechas[f"{i:02d}"] = "26 de agosto"

for i in [21,22]:
    fechas[f"{i:02d}"] = "27 de agosto"

for i in [23,24]:
    fechas[f"{i:02d}"] = "28 de agosto"

for i in [25,26]:
    fechas[f"{i:02d}"] = "31 de agosto"

# SEPTIEMBRE

for i in [27,28]:
    fechas[f"{i:02d}"] = "1 de septiembre"

for i in [29,30]:
    fechas[f"{i:02d}"] = "2 de septiembre"

for i in [31,32]:
    fechas[f"{i:02d}"] = "3 de septiembre"

for i in [33,34]:
    fechas[f"{i:02d}"] = "4 de septiembre"

for i in [35,36]:
    fechas[f"{i:02d}"] = "7 de septiembre"

for i in [37,38]:
    fechas[f"{i:02d}"] = "8 de septiembre"

for i in [39,40]:
    fechas[f"{i:02d}"] = "9 de septiembre"

for i in [41,42]:
    fechas[f"{i:02d}"] = "10 de septiembre"

for i in [43,44]:
    fechas[f"{i:02d}"] = "11 de septiembre"

for i in [45,46]:
    fechas[f"{i:02d}"] = "14 de septiembre"

for i in [47,48]:
    fechas[f"{i:02d}"] = "15 de septiembre"

for i in [49,50]:
    fechas[f"{i:02d}"] = "16 de septiembre"

for i in [51,52]:
    fechas[f"{i:02d}"] = "17 de septiembre"

for i in [53,54]:
    fechas[f"{i:02d}"] = "18 de septiembre"

for i in [55,56]:
    fechas[f"{i:02d}"] = "21 de septiembre"

for i in [57,58]:
    fechas[f"{i:02d}"] = "22 de septiembre"

for i in [59,60]:
    fechas[f"{i:02d}"] = "23 de septiembre"

for i in [61,62]:
    fechas[f"{i:02d}"] = "24 de septiembre"

for i in [63,64]:
    fechas[f"{i:02d}"] = "25 de septiembre"

for i in [65,66]:
    fechas[f"{i:02d}"] = "28 de septiembre"

# OCTUBRE

for i in [67,68]:
    fechas[f"{i:02d}"] = "1 de octubre"

for i in [69,70]:
    fechas[f"{i:02d}"] = "2 de octubre"

for i in [71,72]:
    fechas[f"{i:02d}"] = "5 de octubre"

for i in [73,74]:
    fechas[f"{i:02d}"] = "6 de octubre"

for i in [75,76]:
    fechas[f"{i:02d}"] = "7 de octubre"

for i in [77,78]:
    fechas[f"{i:02d}"] = "8 de octubre"

for i in [79,80]:
    fechas[f"{i:02d}"] = "9 de octubre"

for i in [81,82]:
    fechas[f"{i:02d}"] = "13 de octubre"

for i in [83,84]:
    fechas[f"{i:02d}"] = "14 de octubre"

for i in [85,86]:
    fechas[f"{i:02d}"] = "15 de octubre"

for i in [87,88]:
    fechas[f"{i:02d}"] = "16 de octubre"

for i in [89,90]:
    fechas[f"{i:02d}"] = "19 de octubre"

for i in [91,92]:
    fechas[f"{i:02d}"] = "20 de octubre"

for i in [93,94]:
    fechas[f"{i:02d}"] = "21 de octubre"

for i in [95,96]:
    fechas[f"{i:02d}"] = "22 de octubre"

for i in [97,98]:
    fechas[f"{i:02d}"] = "23 de octubre"

for i in [99,0]:
    fechas[f"{i:02d}"] = "26 de octubre"


# ---------------------------------
# Interfaz
# ---------------------------------

st.markdown(
    "<h1 style='text-align: center;'>email: juannicolas2012@gmail.com</h2>", 
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='text-align: center;'>Whatsapp: +57 3134161053</h2>", 
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='text-align: center;'>📅 Consulta Fecha de vencimiento Declaración de renta</h1>", 
    unsafe_allow_html=True
)

st.write(
    "Digite su número de cédula o NIT para consultar la fecha correspondiente."
)

cedula = st.text_input(
    "Número de cédula",
    placeholder="Ejemplo: 1000123456"
)

if st.button("Consultar"):

    if cedula.strip() == "":
        st.warning("Ingrese una cédula.")
    elif not cedula.isdigit():
        st.error("La cédula solo debe contener números.")
    else:

        ultimos = cedula[-2:]

        fecha = fechas.get(ultimos)

        st.divider()

        st.success("Consulta realizada correctamente")

        st.metric(
            "Últimos dos dígitos",
            ultimos
        )

        st.info(f"📅 Su fecha límite es **{fecha}**")

import streamlit as st

# Título de la aplicación
st.title("💡 Electromagnetismo en la Luz")

# Descripción de la plataforma
st.write("Descubre cómo funciona el electromagnetismo en la luz, su fórmula fundamental y su importancia en la física.")

# Sección: ¿Qué es el electromagnetismo en la luz?
st.header("🔍 ¿Qué es el electromagnetismo en la luz?")
st.write(
    "El electromagnetismo describe cómo los campos eléctricos y magnéticos interactúan para generar ondas electromagnéticas, como la luz. "
    "Estas ondas viajan a través del espacio transportando energía y no requieren de un medio material para propagarse. La luz visible es solo una pequeña parte del espectro electromagnético."
)

# Fórmula fundamental
st.header("📐 Fórmula fundamental")
st.write(
    "La ecuación de onda electromagnética en el vacío es una forma compacta de describir cómo los campos eléctrico (\(E\)) y magnético (\(B\)) oscilan perpendiculares entre sí y en dirección de la propagación. La fórmula es:"
)
st.latex(r"""
\nabla^2 \mathbf{E} - \frac{1}{c^2} \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0
""")
st.write(
    "Donde:\n"
    "- \(\nabla^2\): Operador laplaciano que describe cómo varía el campo en el espacio.\n"
    "- \(c\): Velocidad de la luz en el vacío (aproximadamente \(3 \times 10^8\) m/s).\n"
    "- \(\frac{\partial^2}{\partial t^2}\): Segunda derivada temporal que describe cómo varía el campo en el tiempo."
)

# Imagen ilustrativa
st.header("🌈 Imagen ilustrativa")
st.write("Visualiza cómo los campos eléctrico y magnético se relacionan en una onda electromagnética:")

# Cargar imagen desde URL o archivo local
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Electromagneticwave3D.gif/220px-Electromagneticwave3D.gif"
st.image(image_url, caption="Representación 3D de una onda electromagnética", use_column_width=True)

# Conclusión
st.header("✨ Conclusión")
st.write(
    "El electromagnetismo en la luz es un fenómeno fundamental en la física que explica cómo las ondas electromagnéticas, como la luz visible, se propagan por el espacio. "
    "Este conocimiento es esencial para entender fenómenos como la reflexión, refracción, y aplicaciones como las comunicaciones inalámbricas y la óptica."
)

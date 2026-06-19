# ==========================
# SISTEMA DE CIFRADO CESAR
# ==========================


# --------------------------
# VALIDADOR
# --------------------------

def validar_desplazamiento(n):

    if n.isdigit():

        n = int(n)

        if 1 <= n <= 25:
            return n

    return None


# --------------------------
# MOTOR CESAR
# --------------------------

def cifrar_cesar(mensaje, desplazamiento):

    resultado = ""

    for c in mensaje:

        if c.isalpha():

            if c.isupper():

                inicio = ord("A")

            else:

                inicio = ord("a")

            nueva = (
                (ord(c) - inicio + desplazamiento)
                % 26
            ) + inicio

            resultado += chr(nueva)

        else:

            resultado += c

    return resultado


def descifrar_cesar(mensaje, desplazamiento):

    return cifrar_cesar(
        mensaje,
        -desplazamiento
    )


# --------------------------
# RESULTADO
# --------------------------

def mostrar_resultado(texto):

    print("\n====================")
    print(texto)
    print("====================\n")


# --------------------------
# CONTROLADOR
# --------------------------

def procesar(opcion):

    despl = input(
        "\nIngrese desplazamiento (1-25): "
    )

    despl = validar_desplazamiento(despl)

    if despl is None:

        print(
            "\n❌ Número inválido"
        )

        return

    mensaje = input(
        "\nIngrese el mensaje: "
    )

    if mensaje.strip() == "":

        print(
            "\n❌ Mensaje vacío"
        )

        return

    if opcion == "1":

        resultado = cifrar_cesar(
            mensaje,
            despl
        )

        mostrar_resultado(
            f"Mensaje cifrado:\n{resultado}"
        )

    else:

        resultado = descifrar_cesar(
            mensaje,
            despl
        )

        mostrar_resultado(
            f"Mensaje descifrado:\n{resultado}"
        )


# --------------------------
# INTERFAZ
# --------------------------

def menu():

    while True:

        print("""
==============================
 SISTEMA DE CIFRADO CÉSAR
==============================

1. Cifrar mensaje
2. Descifrar mensaje
3. Salir
""")

        opcion = input(
            "Seleccione opción: "
        )

        if opcion in ["1", "2"]:

            procesar(opcion)

            input(
                "\nPresione ENTER para volver..."
            )

        elif opcion == "3":

            print(
                "\nGracias por usar el sistema 🔐"
            )

            break

        else:

            print(
                "\n❌ Opción inválida"
            )


# --------------------------
# INICIO
# --------------------------

menu()
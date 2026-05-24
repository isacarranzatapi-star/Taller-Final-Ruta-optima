# Frontend/app_envios.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import sqlite3
import os
import sys
from datetime import datetime

# =====================================================
# CONEXIÓN BACKEND
# =====================================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'Backend'
        )
    )
)

from paquetes import Paquete

# =====================================================
# RUTA BASE DE DATOS
# =====================================================

DB_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        'Backend',
        'ruta_optima.db'
    )
)

# =====================================================
# CLASE PRINCIPAL
# =====================================================

class PantallaEnvios:

    def __init__(self, root):

        self.root = root

        self.root.title("Ruta Óptima 🚚")
        self.root.geometry("550x700")
        self.root.configure(bg="#f4f5f9")
        self.root.resizable(False,False)

        # =====================================================
        # LOGO
        # =====================================================

        try:

            ruta_logo = os.path.join(
                os.path.dirname(__file__),
                "logo.png"
            )

            img = Image.open(ruta_logo)

            img = img.resize(
                (250,250)
            )

            self.logo = ImageTk.PhotoImage(img)

            tk.Label(
                root,
                image=self.logo,
                bg="#f4f5f9"
            ).pack(
                pady=10
            )

        except:

            tk.Label(
                root,
                text="🚚 RUTA ÓPTIMA",
                font=("Arial",22,"bold"),
                bg="#f4f5f9"
            ).pack()

        # =====================================================
        # TITULO
        # =====================================================

        tk.Label(
            root,
            text="Sistema Logístico",
            font=("Arial",18,"bold"),
            bg="#f4f5f9"
        ).pack(
            pady=10
        )

        # =====================================================
        # BOTONES CRUD
        # =====================================================

        botones=[

            (
                "📦 Registrar",
                self.registrar_envio,
                "#4CAF50"
            ),

            (
                "📋 Ver Tabla",
                self.ver_tabla,
                "#2196F3"
            ),

            (
                "✏ Actualizar",
                self.actualizar_envio,
                "#FF9800"
            ),

            (
                "🗑 Eliminar",
                self.eliminar_envio,
                "#9C27B0"
            ),

            (
                "📊 Abrir Dashboard",
                self.abrir_dashboard,
                "#607D8B"
            )

        ]

        for texto,funcion,color in botones:

            tk.Button(
                root,
                text=texto,
                font=("Arial",13,"bold"),
                bg=color,
                fg="white",
                width=30,
                height=2,
                cursor="hand2",
                command=funcion
            ).pack(
                pady=8
            )

    # =====================================================
    # REGISTRAR
    # =====================================================

    def registrar_envio(self):

        try:

            id_cliente=simpledialog.askinteger(
                "Registro",
                "Ingrese ID cliente:"
            )

            peso=simpledialog.askfloat(
                "Registro",
                "Ingrese peso:"
            )

            destino=simpledialog.askstring(
                "Registro",
                "Ingrese destino:"
            )

            if (
                id_cliente is None
                or peso is None
                or destino is None
            ):
                return

            if peso<=0:

                raise ValueError(
                    "El peso debe ser mayor a cero."
                )

            paquete=Paquete(
                peso,
                destino
            )

            tipo=paquete.tipo

            costo=paquete.calcular_costo()

            fecha_actual=datetime.now().strftime(
                "%Y-%m-%d"
            )

            conexion=sqlite3.connect(
                DB_PATH
            )

            cursor=conexion.cursor()

            cursor.execute("""

            INSERT INTO envios
            (
                id_cliente,
                peso,
                destino,
                tipo,
                costo,
                fecha
            )

            VALUES
            (
                ?,?,?,?,?,?
            )

            """,

            (
                id_cliente,
                peso,
                destino,
                tipo,
                costo,
                fecha_actual
            )
            )

            conexion.commit()

            conexion.close()

            messagebox.showinfo(
                "Registro exitoso",
                f"Tipo: {tipo}\n"
                f"Costo: ${costo:,.0f}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================
    # VER TABLA
    # =====================================================

    def ver_tabla(self):

        try:

            conexion=sqlite3.connect(
                DB_PATH
            )

            cursor=conexion.cursor()

            cursor.execute(
                "SELECT * FROM envios"
            )

            datos=cursor.fetchall()

            conexion.close()

            if len(datos)==0:

                messagebox.showwarning(
                    "Advertencia",
                    "No hay registros"
                )

                return

            texto=""

            for fila in datos:

                texto+=str(
                    fila
                )+"\n\n"

            messagebox.showinfo(
                "Tabla de Envíos",
                texto
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar_envio(self):

        try:

            id_envio=simpledialog.askinteger(
                "Actualizar",
                "Ingrese ID envío:"
            )

            destino=simpledialog.askstring(
                "Actualizar",
                "Nuevo destino:"
            )

            if (
                id_envio is None
                or destino is None
            ):
                return

            conexion=sqlite3.connect(
                DB_PATH
            )

            cursor=conexion.cursor()

            cursor.execute(
                """
                UPDATE envios
                SET destino=?
                WHERE id=?
                """,
                (
                    destino,
                    id_envio
                )
            )

            conexion.commit()

            conexion.close()

            messagebox.showinfo(
                "Actualizado",
                "Registro actualizado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================
    # ELIMINAR
    # =====================================================

    def eliminar_envio(self):

        try:

            id_envio=simpledialog.askinteger(
                "Eliminar",
                "Ingrese ID:"
            )

            if id_envio is None:

                return

            conexion=sqlite3.connect(
                DB_PATH
            )

            cursor=conexion.cursor()

            cursor.execute(
                """
                DELETE FROM envios
                WHERE id=?
                """,
                (id_envio,)
            )

            conexion.commit()

            conexion.close()

            messagebox.showinfo(
                "Eliminado",
                "Registro eliminado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================
    # POWER BI
    # =====================================================

    def abrir_dashboard(self):

        try:

            ruta_pbix=os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    '..',
                    'ruta_optima_final.pbix'
                )
            )

            os.startfile(
                ruta_pbix
            )

        except:

            messagebox.showwarning(
                "Advertencia",
                "No se encontró el dashboard"
            )
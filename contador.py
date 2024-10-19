from multiprocessing import Value
from turtle import onclick
import flet as ft

def main(page: ft.Page):
    page.title = "Meu app flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) - 1)
        page.update()

    def somar(e):
        caixa_texto.value =str(int(caixa_texto.value) + 1)
        page.update()

    botão_menos = ft.IconButton(
        ft.icons.REMOVE,
        on_click=diminuir
    )

    botão_mais = ft.IconButton(
        ft.icons.ADD,
        on_click=somar
    )

    caixa_texto = ft.TextField(
        value="0",
        width=100,
        text_align=ft.TextAlign.CENTER
    )

    page.add(
        ft.Row(
            [botão_mais,
            caixa_texto,
            botão_menos],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)
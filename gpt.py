import openai
import config
import typer
from rich import print
from rich.table import Table



def main():
    openai.api_key = config.api_key

    #la parte que se mostrara primero del programa
    print("[bold green]ChatGPT con python[/bold green]")

    #tabla de opciones 
    table  = Table("Comando", "Descripcion")
    table.add_row("break", "salir del chat")
    print(table)
    
    while True:
        text = input("Introduce algo: ")
        
        if text == "break":
            break
        
        # crear la solicitud de completado utilizando el estado actual del modelo
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=2048
        )
        
        # imprimir la respuesta del modelo de IA
        message = completion.choices[0].text
        print(message)


    
   
if __name__ == "__main__":
    typer.run(main)
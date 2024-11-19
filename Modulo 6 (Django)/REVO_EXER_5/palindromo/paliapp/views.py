from django.shortcuts import render

def palindromo(request, palabra):
    palabra = str(palabra).lower()
    invertido = palabra[::-1]
    if invertido == palabra:
        context = {palabra, 'es palindromo!'}
        return render(request, 'palindromo.html', context)
    else:
        context = {palabra, 'palindromo'}
        return render(request, 'palindromo.html', context)

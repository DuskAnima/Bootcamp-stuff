from django.shortcuts import render

def palindromo(request, palabra):
    palabra_alt = str(palabra).replace(' ', '').lower()
    invertido = palabra_alt[::-1]
    if invertido == palabra_alt:
        context = {'palabra' : palabra, 'mensaje' : 'es palindromo!'}
        return render(request, 'palindromo.html', context)
    else:
        context = {'palabra' : palabra, 'mensaje' : 'no es palindromo :('}
        return render(request, 'palindromo.html', context)

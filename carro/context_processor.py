from core.models import nuevoUsuario


def importe_total_carro(request):
    total=0
    #for key, value in request.session["carro"].items():
        #total=total+int(value["precio"])
    return { "importe_total_carro": total}
from django.shortcuts import render

# Create your views here. CONTROLLER


def listar_tarefas(request):
    nome_tarefa = "Pagar contas"
    return render(request, 'tarefas/listar_tarefas.html',
                  {'nome_tarefa': nome_tarefa})

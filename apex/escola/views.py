from django.http import JsonResponse, HttpResponse
from escola.models import Aluno, Curso
from escola.serializers import AlunosSerialiazer, CursosSerializer
import json

#def alunos(request):
 #    if request.method == 'GET':
        #aluno = {'Id': 1, 'Nome': 'Seu Nome'}
        #return JsonResponse(aluno)
def alunos(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        serializer = AlunosSerialiazer(alunos, many=True)
        return JsonResponse(serializer.data, safe=False)
        

def alunos2(request):
    alunos = Aluno.objects.all()
    serializer = AlunosSerialiazer(alunos, many=True)
    data = serializer.data
    return HttpResponse(json.dumps(data), content_type='application/json')

def cursos(request):
    cursos = Curso.objects.all()
    serializer = CursosSerializer(cursos, many=True)
    return JsonResponse(serializer.data, safe=False)

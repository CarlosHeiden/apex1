import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from escola.models import Aluno, Curso, Notas
from escola.serializers import (
    AlunosSerialiazer,
    CursosSerializer,
    NotasSerialiazer,
)
from rest_framework import viewsets, status
from rest_framework.response import Response


class AlunosViewSets(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""

    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunosSerialiazer


class CursosViewSets(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursosSerializer


class NotasViewSet(viewsets.ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotasSerialiazer

    def list(self, request):
        media_notas = {}
        for nota in self.get_queryset():
            if nota.aluno.nome in media_notas:
                media_notas[nota.aluno.nome] += nota.nota
            else:
                media_notas[nota.aluno.nome] = nota.nota
        media_notas = {
            k: round(v / len(self.get_queryset()), 2)
            for k, v in media_notas.items()
        }
        media_notas = dict(
            sorted(media_notas.items(), key=lambda item: item[1], reverse=True)
        )
        return Response(media_notas)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

from rest_framework import serializers
from escola.models import Aluno, Curso, Notas


class AlunosSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class NotasSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = ['id', 'aluno', 'curso', 'nota']

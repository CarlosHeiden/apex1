from django.contrib import admin
from escola.models import Aluno, Curso, Notas


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)


admin.site.register(Curso, Cursos)


class Nota(admin.ModelAdmin):
    list_display = (
        'id',
        'aluno',
        'curso',
        'nome_aluno',
        'descricao_curso',
        'nota',
    )
    list_display_links = ('id', 'aluno')
    search_fields = ('aluno',)
    list_per_page = 20


admin.site.register(Notas, Nota)

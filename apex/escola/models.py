from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome}'


class Curso(models.Model):
    nivel = (('B', 'Basico'), ('I', 'Intermediario'), ('A', 'Avancado'))

    codigo_curso = models.CharField(max_length=9)
    descricao = models.CharField(max_length=11)
    nivel = models.CharField(
        max_length=1, choices=nivel, blank=False, null=False
    )

    def __str__(self):
        return f'{self.descricao}'


class Notas(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome_aluno = models.CharField(max_length=100)
    descricao_curso = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('aluno', 'curso')

    def __str__(self):
        return f'{self.nome_aluno}, {self.descricao_curso}'

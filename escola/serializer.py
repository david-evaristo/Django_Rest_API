from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' #PODE USAR O __ALL__ PARA MOSTRAR TODOS OS CAMPOS AO INVES DE ESCREVER TODOS OS CAMPOS

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__' #PODE USAR O __ALL__ PARA MOSTRAR TODOS OS CAMPOS AO INVES DE ESCREVER TODOS OS CAMPOS

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo'] #PODE USAR O __ALL__ PARA MOSTRAR TODOS OS CAMPOS AO INVES DE ESCREVER TODOS OS CAMPOS
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
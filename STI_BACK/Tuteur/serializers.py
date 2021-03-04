from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import Domaine, Cours, CatQuestion, Question,Etudiant,Session_cours


class DomaineSerializer(ModelSerializer):

    class Meta:
        model = Domaine
        fields = '__all__'

class CoursSerializer(ModelSerializer):
    id = serializers.CharField()
    domaine=serializers.CharField()
    name = serializers.CharField()
    description=serializers.CharField()
    contenu=serializers.CharField()
    ressource=serializers.CharField()

    class Meta:
        model = Cours
        fields = '__all__'



class EtudiantSerializer(serializers.Serializer):
    id=serializers.CharField()
    cours=serializers.CharField()
    connaissance=serializers.CharField()
    username=serializers.CharField()
    nom=serializers.CharField()
    prenom=serializers.CharField()
    email=serializers.CharField()
    sexe=serializers.CharField()
    niveau_social=serializers.CharField()
    age=serializers.CharField()
    #matricule=serializers.CharField()

#class CatPlainteSerializer(ModelSerializer):
#
 #   class Meta:
  #      model = CatPlainte
   #     fields = '__all__'

class CatQuestionSerializer(serializers.Serializer):
    id=serializers.CharField()
    name=serializers.CharField()

class QuestionSerializer(serializers.Serializer):
    id = serializers.CharField()
    cours=serializers.CharField()
    libelle = serializers.CharField()
    reponse=serializers.CharField()
    libelle_reponse=serializers.CharField()
    section=serializers.CharField()
    propostion1=serializers.CharField(max_length=250)
    propostion2=serializers.CharField(max_length=250)
    propostion3=serializers.CharField(max_length=250)
    propostion4=serializers.CharField(max_length=250)

class Session_coursSerializer(serializers.Serializer):
    id = serializers.CharField()
    etudiant = serializers.CharField()
    cours=serializers.CharField()
    progression=serializers.CharField()
    note=serializers.CharField()
    def __str__(self):
    	return str(self.user.username)+" "+str(self.user.id)

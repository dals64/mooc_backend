from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view, action,permission_classes
from rest_framework.response import Response
from .models import Domaine, Cours, CatQuestion, Question,Etudiant,Session_cours
from .serializers import DomaineSerializer,CoursSerializer, EtudiantSerializer, QuestionSerializer,CatQuestionSerializer,Session_coursSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, logout, login
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
import json
from datetime import datetime
from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView 
from rest_framework.generics import ListCreateAPIView  
from rest_framework import viewsets  ,status 
from random import randint
from django.conf import settings 
from django.core.mail import send_mail 
import pandas as pd
import random
from STI_BACK.settings import BASE_DIR
import operator
import numpy as np
import pandas as pd
# Create your views here.
URL='http://127.0.0.1:8000/'
@api_view(['GET'])
def DownloadPDF(self):
    path_to_file = BASE_DIR + '/filename.pdf'
    f = open(path_to_file, 'rb')
    pdfFile = File(f)
    response = HttpResponse(pdfFile.read())
    response['Content-Disposition'] = 'attachment'
    return response


@api_view(['POST'])
def loginUser(request):
    password = request.data['password']
    username = request.data['username']
    cours=[]
    
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        success = {'state':'success','username':username}
        etudiant=get_object_or_404(Etudiant,user=user)
        cours_set=etudiant.cours.all()
        for cour in cours_set:
            domaines=cour.domaine.all()
            liste_domaine=[]
            for data in domaines:
                liste_domaine.append({'id':data.id,'nom':data.name})
            lien=URL+str(cour.ressource)
            cours.append({'id':cour.id,
                            'description':cour.description,
                            'contenu':cour.contenu,
                            'domaine':liste_domaine,
                            'ressource':lien,
                            'name':cour.name,
                                })
                                
       
        serializer=CoursSerializer(cours,many=True)
        
        return JsonResponse({'cours':serializer.data,'state':'success','username':username},safe=False)
        
    else:
        
        try:
            etudiant=get_object_or_404(Etudiant,email=username)
            name=etudiant.user.username
            user = authenticate(request, username = name, password = password)
            #login(request, user)
            if user is not None:
                login(request, user)
                success = {'state':'success','username':name}
                etudiant=get_object_or_404(Etudiant,user=user)
                cours_set=etudiant.cours.all()
                for cour in cours_set:
                    domaines=cour.domaine.all()
                    liste_domaine=[]
                    for data in domaines:
                      liste_domaine.append({'id':data.id,'nom':data.name})
                    lien=URL+str(cour.ressource)
                    cours.append({'id':cour.id,
                                                'description':cour.description,
                                                'contenu':cour.contenu,
                                                'domaine':liste_domaine,
                                                'ressource':lien,
                                                'name':cour.name,
                                                    })
                                        
            
                serializer=CoursSerializer(cours,many=True)
                
                return JsonResponse({'cours':serializer.data,'state':'success','username':username},safe=False)
                    
            else:
               fail={'state':'fail','motif':'Mot de passe Erroné'}
             
               return JsonResponse(fail) 
        except :
            try:
               utilisateurs=get_object_or_404(User,username=username)
               fail={'state':'fail','motif':'Mot de passe Erroné'}
            except :
               fail={'state':'fail','motif':'Utilisateur non Existant'}
            
            
            return JsonResponse(fail)

@api_view(['GET'])
def get_cours(request):
    cours_set=get_list_or_404(Cours)
    cours=[]
    for cour in cours_set:
        domaines=cour.domaine.all()
        liste_domaine=[]
        for data in domaines:
            liste_domaine.append({'id':data.id,'nom':data.name})
        lien=URL+str(cour.ressource)
        cours.append({'id':cour.id,
                                    'description':cour.description,
                                    'contenu':cour.contenu,
                                    'domaine':liste_domaine,
                                    'ressource':lien,
                                    'name':cour.name,
                                        })
                            

    serializer=CoursSerializer(cours,many=True)
    
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def Signup(request):
    username = request.data['username']
    password = request.data['password']
    nom = request.data['nom']
    prenom= request.data['prenom']
    age=request.data['age']
    sexe=request.data['sexe']
    mail=request.data['email']

    fails = {"state":"User exist"}
    user = User.objects.create_user(username, mail, password)
    user.last_name = prenom
    user.first_name=nom
    user.email=mail
    user.save()
    etudiant = Etudiant(
        user=user,
        email=request.data['email'],
        name=request.data['nom'],
        prenom=request.data['prenom'],
        sexe=request.data['sexe'],
        age=request.data['age'],
    )
    etudiant.save()
    cours=[]
    
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        success = {'state':'success','username':username}
        etudiant=get_object_or_404(Etudiant,user=user)
        cours_set=etudiant.cours.all()
        for cour in cours_set:
            domaines=cour.domaine.all()
            liste_domaine=[]
            for data in domaines:
                liste_domaine.append({'id':data.id,'nom':data.name})
            lien=URL+str(cour.ressource)
            cours.append({'id':cour.id,
                            'description':cour.description,
                            'contenu':cour.contenu,
                            'domaine':liste_domaine,
                            'ressource':lien,
                            'name':cour.name,
                                })
                                
       
        serializer=CoursSerializer(cours,many=True)
        
        return JsonResponse({'cours':serializer.data,'state':'success','username':username},safe=False)
        
    else:
        
        try:
            etudiant=get_object_or_404(Etudiant,email=username)
            name=etudiant.user.username
            user = authenticate(request, username = name, password = password)
            #login(request, user)
            if user is not None:
                login(request, user)
                success = {'state':'success','username':name}
                etudiant=get_object_or_404(Etudiant,user=user)
                cours_set=etudiant.cours.all()
                for cour in cours_set:
                    domaines=cour.domaine.all()
                    liste_domaine=[]
                    for data in domaines:
                      liste_domaine.append({'id':data.id,'nom':data.name})
                    lien=URL+str(cour.ressource)
                    cours.append({'id':cour.id,
                                                'description':cour.description,
                                                'contenu':cour.contenu,
                                                'domaine':liste_domaine,
                                                'ressource':lien,
                                                'name':cour.name,
                                                    })
                                        
            
                serializer=CoursSerializer(cours,many=True)
                
                return JsonResponse({'cours':serializer.data,'state':'success','username':username},safe=False)
                    
            else:
               fail={'state':'fail','motif':'Mot de passe Erroné'}
             
               return JsonResponse(fail) 
        except :
            try:
               utilisateurs=get_object_or_404(User,username=username)
               fail={'state':'fail','motif':'Mot de passe Erroné'}
            except :
               fail={'state':'fail','motif':'Utilisateur non Existant'}
            
            
            return JsonResponse(fail)
    

@api_view(['POST'])
def TerminerCours(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    etudiant=get_object_or_404(Etudiant,user=user)
    cours=get_object_or_404(Cours,id=request.data['id_cours'])
    connaissance=cours.domaine.all()
    for data in connaissance:
      etudiant.connaissance.add(data)
    data = {"state":"success"} 
    return  JsonResponse(data)

@api_view(['POST'])
def Incrire_cours(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    id_cours = request.data['id']
    etudiant = Etudiant.objects.get(user=user)
    cours = get_object_or_404(Cours,id=id_cours)
    try:
        new_session=get_object_or_404(Session_cours,etudiant=etudiant,cours=cours)
        
    except :
        session_cours = Session_cours(note=0, progression=0)
        session_cours.etudiant = etudiant
        session_cours.cours =cours
        session_cours.save()
        etudiant.cours.add(cours)
        return JsonResponse({'status':'success'})

    data = {"state":"success"} 
    return  JsonResponse(data)

@api_view(['POST'])
def create_session(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    id_cours = request.data['id_cours']
    etudiant = Etudiant.objects.get(user=user)
    cours = Cours.objects.get(id=id_cours)
    session_cours = Session_cours(note=0, progression=0)
    session_cours.etudiant = etudiant
    session_cours.cours =cours
    session_cours.save()

    data = {"state":"success"} 
    return  JsonResponse(data)
    
@api_view(['POST'])
def upgrade_progression(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    id_cours = request.data['id_cours']
    etudiant = Etudiant.objects.get(user=user)
    cours = Cours.objects.get(id=id_cours)
    session_cours = Session_cours.objects.get(cours=cours,etudiant=etudiant)
    #chaque cours a trois sections 
    if session_cours.progression==0:
       session_cours.progression =34
    elif session_cours.progression==100 :
       session_cours.progression=session_cours.progression
    else:
       session_cours.progression =session_cours.progression+33

    session_cours.save()

    data = {"state":"success"} 
    return  JsonResponse(data)
    

@api_view(['POST'])
def Envoyer_questions(request):
    questions=[]
    id = request.data['id']
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    etudiant = Etudiant.objects.get(user=user)
    cours = Cours.objects.get(id=id)
    session_cours = Session_cours.objects.get(cours=cours,etudiant=etudiant)
    all_questions_section= get_list_or_404(Question,cours=cours)
    questions_section = random.sample(all_questions_section, 15)
   
    questions_a_envoyer = questions_section
    for question in questions_a_envoyer:
        questions.append({'id':question.id,
                        'cours':question.cours,
                        'libelle':question.libellé,
                        'reponse':question.reponse,
                        'libelle_reponse':question.libellé_reponse,
                        'section':question.section,
                        'propostion1':question.propostion1,
                        'propostion2':question.propostion2,
                        'propostion3':question.propostion3,
                        'propostion4':question.propostion4,
                            })
                                        
            
    serializer=QuestionSerializer(questions,many=True)
    return JsonResponse(serializer.data,safe=False)
    


@api_view(['POST'])
def Evaluation(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    id = request.data['id']
    note=0
    etudiant = Etudiant.objects.get(user=user)
    cours = Cours.objects.get(id=id)
    session_cours = Session_cours.objects.get(cours=cours,etudiant=etudiant)
    liste_reponses = request.data['Liste_reponses']
    for valeur in liste_reponses:
       question=get_object_or_404(Question, id = int(valeur['id']))
       if valeur['reponse']==question.reponse:
           print(valeur['reponse'])
           note=note+1
       
    #pourcentage_questions_ratée_section=(nombre_questions_ratée_section*100)*(1/sum(nombre_questions_ratée_section))
    

    session_cours.note =note
    

    session_cours.save()
    print(note)
    return JsonResponse({'note':note}, safe=False)

@api_view(['GET'])
def listeDomaines(request):
    domaines = get_list_or_404(Domaine)
    serializer = DomaineSerializer(domaines,many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def initialize_connaissance(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    etudiant = Etudiant.objects.get(user=user)
    liste_connaissance_base=request.data['Connaissances']

    for data in liste_connaissance_base:
        domaine = Domaine.objects.get(id=data)
        etudiant.connaissance.add(domaine)
    data = {"state":"success"} 
    return  JsonResponse(data)


### Partie Recommandation  

@api_view(['POST'])
def Recommandation1(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    etudiant = Etudiant.objects.get(user=user)
    liste_connaissance_base=etudiant.connaissance.all()
    liste_cours_etudiant=[]
    liste_connaissance_etudiant=[]
    dictionnaire_cours={}
    
    for data in liste_connaissance_base:
        liste_connaissance_etudiant.append(data.id)

    
    liste_cours=Session_cours.objects.get(etudiant=etudiant)
    for data in liste_cours:
        liste_cours_etudiant.append(data.cours.id)
    

    cours=get_list_or_404(Cours)

    for data in Cours:
        domaines=data.domaine.all()
        for domaine in domaines:
            liste_domaine=[]
            liste_domaine.append(domaine.id)
        dictionnaire_cours[data.id]=liste_domaine

    proba_cour={}
    for i in dictionnaire_cours.keys():
        if(i in liste_cours_etudiant):
            proba_cour[i]=0 
            continue
        count_valid_domain=0
        for j in liste_connaissance_etudiant:
            if (j in dictionnaire_cours[i]):
             count_valid_domain += 1
        proba_cour[i]=(count_valid_domain/len(dictionnaire_cours[i]))
    probadict=sorted(proba_cour.items(), key=operator.itemgetter(1),reverse=True)
    cours=[]
    for id in probadict.keys():

        cour=Cours.objects.get(id=id)
        domaines=cour.domaine.all()
        liste_domaine=[]
        for data in domaines:
            liste_domaine.append({'id':data.id,'nom':data.name})
        lien=URL+str(cour.ressource)
        cours.append({'id':cour.id,
                            'description':cour.description,
                            'contenu':cour.contenu,
                            'domaine':liste_domaine,
                            'ressource':lien,
                            'name':cour.name,
                                })

    serializer=CoursSerializer(cours,many=True)



    return  JsonResponse(serializer.data,safe=False)




##### Recommandation via Association Rule Mining

def support(list_cours_user,cours_vise):
    temp=np.array(datasets[cours_vise])
    for i in list_cours_user:
        temp=temp+np.array(datasets[i])
    return list(temp).count(len(list_cours_user)+1)/len(list_user)

def confidence(list_cours_user,cours_vise):
    flag=True
    for i in list_cours_user:
        if flag:
            temp=np.array(datasets[i])
            flag=False
            continue
        temp=temp+np.array(datasets[i])
    position_1=list(temp).count(len(list_cours_user))
    
    confidence=list(temp+np.array(datasets[cours_vise])).count(len(list_cours_user)+1)/position_1
    return confidence

def lift(list_cours_user,cours_vise):
    if support(list_cours_user,cours_vise)==0.0 : return 0
    return confidence(list_cours_user,cours_vise)/support(list_cours_user,cours_vise)

def moyenne_proba(list_cours_user,cours_vise):
    return (confidence(list_cours_user,cours_vise)+support(list_cours_user,cours_vise)+lift(list_cours_user,cours_vise))/3
def recommendation_cours_choix(list_cours_user):
    proba_cour_choix={}
    for i in list_cour:
        if i in list_cours_user :
             continue
        proba_cour_choix[i]=moyenne_proba(list_cours_user,i)
    return  sorted(proba_cour_choix.items(), key=operator.itemgetter(1),reverse=True)   

@api_view(['POST'])
def Association_Rule_Mining(request):
    user = authenticate(request, username = request.data['username'], password = request.data['password'])
    etudiant = Etudiant.objects.get(user=user)
    etudiants = get_list_or_404(Etudiant)
    liste_connaissance_base=etudiant.connaissance.all()
    cours=get_list_or_404(Cours)
    list_cours=[]
    list_user=[]
    list_cours_user=[]
    liste_connaissance_etudiant=[]
    dictionnaire_cours={}

    liste_cours=get_list_or_404(Session_cours,etudiant=etudiant)
    for data in liste_cours:
        list_cours_user.append(data.cours.id)
    
    for data in cours:
        list_cours.append(data.id)

    for data in etudiants:
        list_user.append(data.id)
        
    for data in etudiants:
        list_user.append(data.id)

    for data in etudiants:
        cours=data.cours.all()
        for i in cours:
            liste_cours=[]
            liste_cours.append(i.id)
        dictionnaire_cours[data.id]=liste_cours
    probadict=recommendation_cours_choix(list_cours_user)
    cours=[]

    for id in probadict.keys():
        cour=Cours.objects.get(id=id)
        domaines=cour.domaine.all()
        liste_domaine=[]
        for data in domaines:
            liste_domaine.append({'id':data.id,'nom':data.name})
        lien=URL+str(cour.ressource)
        cours.append({'id':cour.id,
                            'description':cour.description,
                            'contenu':cour.contenu,
                            'domaine':liste_domaine,
                            'ressource':lien,
                            'name':cour.name,
                                })

    serializer=CoursSerializer(cours,many=True)

    return JsonResponse(result)
    
     
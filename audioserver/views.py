from django.http import HttpResponse
from .models import Song
from .models import Podcast
from .models import Audiobook
from .models import Participant
from . import serializers
import json
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
 

def home(request):
    return HttpResponse("This is my home page")

@csrf_exempt 
def createAPI(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if data['type'] == "Song":
            serialized_data = serializers.Song_Serializer(data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                return HttpResponse("Action successful", status=200)
            else:
                return HttpResponse("invalid request", status=400)

        elif data['type'] == "Podcast":
            if len(data['participants']) <= 10:
                new_podcast = Podcast.objects.create(podId=data["podId"], name = data["name"], duration=data["duration"], upload_time=data["upload_time"], host=data["host"])
                new_podcast.save()

                for participant in data["participants"]:
                    if Participant.objects.filter(name=participant['name']).exists():
                        participant_obj = Participant.objects.get(name=participant["name"])
                    else:    
                        participant_obj = Participant.objects.create(name=participant["name"])
                    new_podcast.participants.add(participant_obj)

                serialized_data = serializers.Podcast_Serializer(new_podcast)
                return HttpResponse("Action successful", status=200)
            else:
                return HttpResponse("Invalid request: More then 10 participants are not allowed", status=400)

        elif data['type'] == "Audiobook":
            serialized_data = serializers.Audiobook_Serializer(data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                return HttpResponse("Action successful", status=200)
            else:
                return HttpResponse("invalid request", status=400)
        else:
            return HttpResponse("Invalid request", status=400)
    else:
        return HttpResponse("Internal server error", status=500)

@csrf_exempt
def deleteAPI(request,type,id):
    if type=="Song":
        try:
            song = Song.objects.get(songId=id)
        except:
            return HttpResponse("Invalid request", status=400)
        song.delete()
        return HttpResponse("record deleted", status=200)

    elif type=="Podcast":
        try:
            pod = Podcast.objects.get(podId=id)
        except:
            return HttpResponse("Invalid request", status=400)
        pod.delete()
        return HttpResponse("record deleted", status=200)

    elif type=="Audiobook":
        try:
            audio = Audiobook.objects.get(audioId=id)
        except:
            return HttpResponse("Invalid request", status=400)
        audio.delete()
        return HttpResponse("record deleted", status=200)
    
    else:
        return HttpResponse("Invalid request", status=400)

@csrf_exempt
def updateAPI(request, type, id):
    if type == "Song":
        try:
            song = Song.objects.get(songId=id)
        except:
            return HttpResponse("Invalid request", status=400)
        
        if request.method == "PUT":
            song_data = JSONParser().parse(request)
            serialized_song_data = serializers.Song_Serializer(song, song_data, partial=True)
            if serialized_song_data.is_valid():
                serialized_song_data.save()
                return HttpResponse("Action is successful", status=200)
            else:
                return HttpResponse("Invalid request", status=400)
        else:
            return HttpResponse ("Internal server error", status=500)

    elif type == "Podcast":
        try:
            pod = Podcast.objects.get(podId=id)
        except:
            return HttpResponse("Invalid request", status=400)
        field_name = 'participants'
        field_object = Podcast._meta.get_field(field_name)
        field_value = field_object.value_from_object(pod)
        if request.method == "PUT":
            pod_data = JSONParser().parse(request)
            if 'participants' in pod_data:
                if len(field_value) + len(pod_data['participants']) <=10:
                    for participant in pod_data['participants']:
                        if Participant.objects.filter(name=participant['name']).exists():
                            participant_obj = Participant.objects.get(name=participant['name'])
                            pod.participants.add(participant_obj)
                        else:
                            participant_obj = Participant.objects.create(name=participant['name'])
                            pod.participants.add(participant_obj)
                else:
                    return HttpResponse("Invalid request: More then 10 partiipants are not allowed", status=400)
                

            serialized_pod_data = serializers.Podcast_Serializer(pod, data=pod_data, partial=True)
            if serialized_pod_data.is_valid():
                serialized_pod_data.save()
                return HttpResponse("Action is successful", status=200)
            else:
                return HttpResponse("Invalid reques", status=400)
        else:
            return HttpResponse ("Internal server error", status=500)

    elif type == "Audiobook":
        try:
            audio = Audiobook.objects.get(audioId=id)
        except:
            return HttpResponse("Invalid request", status=400)
        
        if request.method == "PUT":
            audio_data = JSONParser().parse(request)
            serialized_audio_data = serializers.Audiobook_Serializer(audio, data=audio_data, partial = True)
            if serialized_audio_data.is_valid():
                serialized_audio_data.save()
                return HttpResponse("Action is successful", status=200)
            else:
                return HttpResponse("Invalid reques", status=400)
        else:
            return HttpResponse ("Internal server error", status=500)
    else:
        return HttpResponse("Internal server error", status=500)

@csrf_exempt
def getAPI(request, type, id):
    if type=="Song":
        try:
            song = Song.objects.get(songId=id)
        except:
            return HttpResponse("Invalid Request", status=400)

        if request.method == 'GET':
            serialized_song = serializers.Song_Serializer(song)
            return JsonResponse(serialized_song.data, status=200)
        else:
            return HttpResponse("Internal server error", status=500)

    elif type == "Podcast":
        try:
            pod = Podcast.objects.get(podId=id)
        except:
            return HttpResponse("Invalid Request", status=400)

        if request.method == 'GET':
            serialized_pod = serializers.Podcast_Serializer(pod)
            return JsonResponse(serialized_pod.data, safe=False, status=200)
        else:
            return HttpResponse("Internal server error", status=500)

    elif type == "Audiobook":
        try:
            audio = Audiobook.objects.get(audioId=id)
        except:
            return HttpResponse("Invalid Request", status=400)

        if request.method == 'GET':
            serialized_audio = serializers.Audiobook_Serializer(audio)
            return JsonResponse(serialized_audio.data, status=200)
        else:
            return HttpResponse("Internal server error", status=500)
    
    else:
        return HttpResponse("Invalid request", status=400)

@csrf_exempt
def get_by_type(request, type):
    if type == "Song":
        song = Song.objects.all()
        if request.method == 'GET':
            serialized_songs = serializers.Song_Serializer(song, many=True)
            return JsonResponse(serialized_songs.data, safe=False, status=200)
        else:
            return HttpResponse("Internal server error", status=500)
    elif type == "Podcast":
        pod = Podcast.objects.all()
        if request.method == 'GET':
            serialized_pods = serializers.Podcast_Serializer(pod, many=True)
            return JsonResponse(serialized_pods.data, safe=False, status=200)
        else:
            return HttpResponse("Internal server error", status=500)
    elif type == "Audiobook":
        audio = Audiobook.objects.all()
        if request.method == 'GET':
            serialized_audios = serializers.Audiobook_Serializer(audio, many=True)
            return JsonResponse(serialized_audios.data, safe=False, status=200)
        else:
            return HttpResponse("Internal server error", status=500)
    else:
        return HttpResponse("Invalid request", status=400)
    


        

        
        
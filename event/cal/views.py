from django.shortcuts import render
from django.http import JsonResponse 
from .models import Event
 
# def index(request):
#     return render(request,'index.html')


# Create your views here.
def index(request):  
    all_events = Event.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'index.html',context)
 
def all_events(request):                                                                                                 
    all_events = Event.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.title,                                                                                         
            'event_id': event.event_id,                                                                                              
            'start_date': event.start_date.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end_date': event.end_date.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start_date = request.GET.get("start_date", None)
    end_date = request.GET.get("end_date", None)
    title = request.GET.get("title", None)
    # event = Event(description=str(title), start_date=start_date, end_date=end_date)
    # event.save()
    data = {}
    return JsonResponse(data)
 




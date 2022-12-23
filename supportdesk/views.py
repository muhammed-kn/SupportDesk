from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SupportTicketForm
import random
from .models import SupportTicket
import datetime as dt
from django.contrib.admin.views.decorators import staff_member_required



def get_agent_context(user):
    query_set=SupportTicket.objects.filter(assigned_to=user)
    data=[]
    for i in query_set:
        tdy = dt.datetime.today()
        d={
        "id":str(i.id),
        "summary":str(i.summary),
        "description":i.description[:180]+".....",
        "is_priority":i.is_priority,
        "assigned_to":i.assigned_to,
        "is_completed":i.is_completed,
        "days":(tdy.date()-i.created_date.date()).days,  
        }
        data.append(d) 
    return data         
def customer_ticket_count(user):
    query_set=SupportTicket.objects.filter(created_by=user)
    return (len(query_set))


@login_required(login_url='auth/login/')
def home(request):
    if not request.user.is_staff:
        form = SupportTicketForm()
        context={'form':form,"count":customer_ticket_count(request.user)}
        return render(request, "supportdesk/customer/customer_home.html", context)
    else:  
        context={"listed_data":get_agent_context(request.user),}
        return render(request, "supportdesk/agent/agent_home.html", context)


@login_required(login_url='auth/login/')
def createRequest(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.is_completed=False
            instance.created_by = User.objects.get(id=request.user.id)
            instance.assigned_to = random.choice(list(User.objects.filter(is_staff=True)))
            instance.save()
            form = SupportTicketForm()
            context={'form':form,"message":"succesfully created","count":customer_ticket_count(request.user)}
            return render(request, "supportdesk/customer/customer_home.html", context)
        else:
            context={'form':form,"count":customer_ticket_count(request.user)}
            return render(request, "supportdesk/customer/customer_home.html", context)
 
@login_required(login_url='auth/login/')
def myRequest(request):
    query_set=SupportTicket.objects.filter(created_by=request.user)
    data=[]
    for i in query_set:
        tdy = dt.datetime.today()
        d={
        "summary":str(i.summary),
        "description":i.description,
        "is_priority":i.is_priority,
        "assigned_to":i.assigned_to,
        "is_completed":i.is_completed,
        "days":(tdy.date()-i.created_date.date()).days,  
        }
        data.append(d)          
    context={"listed_data":data,"count":customer_ticket_count(request.user)}
    return render(request, "supportdesk/customer/my_ticket.html", context)

@staff_member_required
@login_required(login_url='auth/login/')
def completed(request,id):
    instance=SupportTicket.objects.get(id=id)
    if  instance.is_completed==False:
        instance.is_completed=True
        instance.save()
    return redirect('supportdesk_home')

@staff_member_required
@login_required(login_url='auth/login/')
def reassign(request,id):
    instance=SupportTicket.objects.get(id=id)
    if  instance.is_completed==False:
        lst=list(User.objects.filter(is_staff=True))
        if len(lst) >1:
            while True:
                new_staff=choice=random.choice(lst)
                if instance.assigned_to != new_staff:
                    instance.assigned_to = new_staff
                    instance.save()
                    break
    return redirect('supportdesk_home')

@staff_member_required   
@login_required(login_url='auth/login/')
def agentSingleView(request,id):
    tdy = dt.datetime.today()
    instance=SupportTicket.objects.get(id=id)
    d={
        "id":str(instance.id),
        "summary":str(instance.summary),
        "description":instance.description,
        "is_priority":instance.is_priority,
        "assigned_to":instance.assigned_to,
        "is_completed":instance.is_completed,
        "days":(tdy.date()-instance.created_date.date()).days,  
        }
    return render(request, "supportdesk/agent/agent_single.html", d)
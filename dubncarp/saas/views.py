from django.shortcuts import render
from .models import Member
from .utitiles import  get_tenant


def our_team(request):
    tenant=get_tenant(request)
    members=Member.objects.filter(tenant=tenant)

    return render(request,'tenant/our_team.html',{'tenant':tenant,'members':members})

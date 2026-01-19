from django.shortcuts import render
from .models import Complaint, Category

def complaint_form(request):
    if request.method == 'POST':
        category = Category.objects.first()

        if category:  
            Complaint.objects.create(
                name=request.POST.get('name'),
                message=request.POST.get('message'),
                category=category
            )

    return render(request, 'complaints/complaint_form.html')
def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/complaint_list.html', {
        'complaints': complaints
    })
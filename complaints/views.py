from django.shortcuts import render, redirect
from .models import Complaint, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ComplaintSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET', 'PUT', 'DELETE'])
def complaint_detail_api(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)

    if request.method == 'GET':
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        complaint.delete()
        return Response(
            {'status': 'deleted'},
            status=status.HTTP_204_NO_CONTENT
        )


def complaint_form(request):
    if request.method == 'POST':
        category = Category.objects.first()

        if category:
            Complaint.objects.create(
                name=request.POST.get('name'),
                message=request.POST.get('message'),
                category=category
            )
            return redirect('success') 

    return render(request, 'complaints/complaint_form.html')


@api_view(['GET', 'POST'])
def complaint_api(request):
    if request.method == 'GET':
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'created'})
        return Response(serializer.errors, status=400)



def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/complaint_list.html', {
        'complaints': complaints
    }
    )

def success(request):
    return render(request, 'complaints/success.html')

def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'complaints/complaint_detail.html', {
        'complaint': complaint
    })


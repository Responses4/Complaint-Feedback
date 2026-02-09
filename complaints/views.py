from django.shortcuts import render, redirect, get_object_or_404
from .models import Complaint, Category

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ComplaintSerializer


# ================= API =================

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
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)


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


# ================= PAGES =================

def complaint_form(request):
    if request.method == 'POST':
        category = Category.objects.first()
        if not category:
            category = Category.objects.create(name='General')

        Complaint.objects.create(
            name=request.POST.get('name'),
            message=request.POST.get('message'),
            file=request.FILES.get('file'),
            category=category
        )

        return redirect('complaints:success')

    return render(request, 'complaints/complaint_form.html')


def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(
        request,
        'complaints/complaint_list.html',
        {'complaints': complaints}
    )


def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(
        request,
        'complaints/complaint_detail.html',
        {'complaint': complaint}
    )


def reply_to_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)

    if request.method == 'POST':
        complaint.reply = request.POST.get('message')
        complaint.save()
        return redirect('complaints:complaint_list')  # ❗ ИСПРАВЛЕНО

    return render(
        request,
        'complaints/reply.html',
        {'complaint': complaint}
    )


def success(request):
    return render(request, 'complaints/success.html')

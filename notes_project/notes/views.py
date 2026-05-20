from django.shortcuts import render, redirect
from .models import Note

def home(request):

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Note.objects.create(title=title)

        return redirect('/')

    notes = Note.objects.all()

    return render(request, 'notes/home.html', {'notes': notes})

def delete_note(request, note_id):

    note = Note.objects.get(id=note_id)

    note.delete()

    return redirect('/')
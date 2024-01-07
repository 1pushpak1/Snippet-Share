# snippets/views.py
from django.shortcuts import render, redirect
from .models import Snippet, SharedSnippet
from .forms import SnippetForm
from datetime import datetime, timedelta

def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/snippet_list.html', {'snippets': snippets})

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippet_list')
    else:
        form = SnippetForm()
    return render(request, 'snippets/create_snippet.html', {'form': form})

def share_snippet(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    
    # Set visibility expiration (e.g., 7 days from now)
    visibility_expiry = datetime.now() + timedelta(days=7)

    shared_snippet = SharedSnippet.objects.create(snippet=snippet, visibility_expiry=visibility_expiry)

    shared_link = f'http://yourdomain.com/shared/{shared_snippet.id}/'

    return render(request, 'snippets/share_snippet.html', {'shared_link': shared_link})

def view_shared_snippet(request, shared_id):
    shared_snippet = SharedSnippet.objects.get(pk=shared_id)

    # Check if the link is still valid
    if shared_snippet.visibility_expiry >= datetime.now():
        snippet = shared_snippet.snippet
        return render(request, 'snippets/view_shared_snippet.html', {'snippet': snippet})
    else:
        return render(request, 'snippets/link_expired.html')
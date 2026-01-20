from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()  # Save to database
            name = inquiry.name
            request.session['submitted_name'] = name  # Store in session for success page
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    name = request.session.get('submitted_name', 'Unknown')
    if 'submitted_name' in request.session:
        del request.session['submitted_name']  # Clean up
    return render(request, 'success.html', {'name': name})

def contact(request):
    if request.method == "POST":
        # 1. Collect the data from the form
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_subject = request.POST.get('subject')
        user_message = request.POST.get('message')

        # 2. Process the data (For now, we'll send it to the success page)
        context = {
            'name': user_name,
            'subject': user_subject
        }
        return render(request, 'contact_success.html', context)

    # If it's a normal visit (GET), just show the form
    return render(request, 'contact.html')

def homepage(request):
    context = {
        'title': 'City Police Station',
        'welcome_message': 'Welcome to the City Police Station. We are committed to keeping our community safe.',
        'services': ['Emergency Response', 'Crime Reporting', 'Traffic Enforcement', 'Community Outreach'],
        'contact': {'phone': '911 (Emergency) or (123) 456-7890', 'email': 'info@citypolice.gov', 'address': '123 Main Street, City, State 12345'}
    }
    return render(request, 'app/homepage.html', context)

def about(request):
    context = {
        'title': 'About Us - City Police Station',
        'mission': 'Our mission is to protect and serve the community with integrity.',
        'history': 'Founded in 1950, we have evolved with the community.',
        'team': [{'name': 'Chief John Doe', 'role': 'Chief of Police'}, {'name': 'Officer Jane Smith', 'role': 'Community Liaison'}],
        'values': ['Integrity', 'Respect', 'Accountability']
    }
    return render(request, 'app/about.html', context)

def services(request):
    context = {
        'title': 'Services - City Police Station',
        'services_list': [
            {'name': 'Emergency Response', 'desc': '24/7 emergency services.'},
            {'name': 'Crime Reporting', 'desc': 'Report crimes online or in person.'},
            {'name': 'Traffic Enforcement', 'desc': 'Ensure road safety.'}
        ]
    }
    return render(request, 'app/services.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect after success
    else:
        form = ContactForm()
    context = {'title': 'Contact Us - City Police Station', 'form': form}
    return render(request, 'app/contact.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

def contact_list(request):
    query = request.GET.get('q', '')
    if query:
        contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(last_name__icontains=query) | Contact.objects.filter(phone__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts, 'query': query})

def contact_add(request):
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST.get('email', ''),
            address=request.POST.get('address', ''),
            category=request.POST.get('category', 'other'),
        )
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'categories': Contact.CATEGORY_CHOICES})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.first_name = request.POST['first_name']
        contact.last_name = request.POST['last_name']
        contact.phone = request.POST['phone']
        contact.email = request.POST.get('email', '')
        contact.address = request.POST.get('address', '')
        contact.category = request.POST.get('category', 'other')
        contact.save()
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'contact': contact, 'categories': Contact.CATEGORY_CHOICES})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
    
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from guitar_house.common.forms import MessageForm
from guitar_house.guitar.models import Guitar



# Create your views here.
def index(request):
    return render(request, 'common/index.html')

def show_guitars(request):
    guitar_type_pattern = request.GET.get('guitar_type_pattern', None)





    guitars = Guitar.objects.all().order_by('model')

    if guitar_type_pattern:
        guitars = guitars.filter(type__icontains=guitar_type_pattern)
    items_per_page = 3 # You can adjust this value baseeld on your preference

    # Initialize the paginator
    paginator = Paginator(guitars, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page', 1)

    try:
        # Get the Page object for the given page number
        current_page = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        current_page = paginator.page(1)
    except EmptyPage:
        # If the page parameter is out of range (e.g., 9999), deliver the last page
        current_page = paginator.page(paginator.num_pages)

    # Pass the current page's objects to the template

    context = {


        'current_page': current_page,
        'guitars': guitars,
        'guitar_type_pattern': guitar_type_pattern
    }

    return render(request, 'guitars/guitars.html', context)

def user_guitars(request):
    user = request.user
    user_guitars = Guitar.objects.filter(user=user).all().order_by('model')
    return render(request, 'guitars/user-guitars.html', {'user_guitars': user_guitars})



def contact_seller(request, guitar_id):
    guitar = Guitar.objects.get(pk=guitar_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = guitar.user
            message.guitar = guitar
            message.save()
            return redirect('guitar-info', guitar.pk)
    else:
        form = MessageForm()
    return render(request, 'common/contact_seller.html', {'form': form, 'guitar': guitar})

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .forms import MessageForm, ReplyForm
from .models import Message
from .models import Guitar


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def show_guitars(request):
    guitar_type_pattern = request.GET.get('guitar_type_pattern', None)

    guitars = Guitar.objects.all().order_by('model')

    if guitar_type_pattern:
        guitars = guitars.filter(type__icontains=guitar_type_pattern)
    items_per_page = 6

    paginator = Paginator(guitars, items_per_page)

    page = request.GET.get('page', 1)

    try:

        current_page = paginator.page(page)
    except PageNotAnInteger:

        current_page = paginator.page(1)
    except EmptyPage:

        current_page = paginator.page(paginator.num_pages)

    context = {

        'current_page': current_page,
        'guitars': guitars,
        'guitar_type_pattern': guitar_type_pattern
    }

    return render(request, 'guitars/guitars.html', context)


def user_guitars(request):
    current_user = request.user
    user_guitars = Guitar.objects.filter(user=current_user).order_by('model')
    return render(request, 'guitars/user-guitars.html', {'user_guitars': user_guitars})


def contact_seller(request, guitar_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Only logged in users can contact the seller.")
        return redirect('sign-in')
    else:
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


def sent_messages(request):
    sent_messages = Message.objects.filter(recipient=request.user)

    context = {
        'sent_messages': sent_messages
    }

    return render(request, 'common/sent_messages.html', context)


def reply_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = message.recipient
            reply.recipient = message.sender
            reply.guitar = message.guitar
            reply.save()
            return redirect('show-messages')

    else:
        form = ReplyForm()

    return render(request, 'common/reply-message.html', {'form': form, 'message': message})


def delete_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.delete()
    return redirect('show-messages')

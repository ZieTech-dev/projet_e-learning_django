from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from django.shortcuts import render
from .models import Chat, Forum, Groupe
from django.shortcuts import render, get_object_or_404
from .form import ChatMessageForm,ForumMessageForm, GroupeMessageForm


def discussion(request, room_name):
    """
    Afficher le chat d'une salle donnée (room_name), et gérer l'envoi de nouveaux messages.
    """
    # Récupérer ou créer la salle de chat
    chat, created = Chat.objects.get_or_create(nomChat=room_name)

    # Récupérer les messages de cette salle, triés par date d'envoi
    messages = Message.objects.filter(chat=chat).order_by('dateEnvoi')

    # Envoi d'un message via un formulaire POST
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            # Créer et sauvegarder le message
            message = Message.objects.create(
                contenu=message_content,
                auteur_id=request.user,
                statut=True,  # message actif
            )
            message.save()

            # Rediriger pour recharger la page avec le nouveau message
            return redirect('room', room_name=room_name)

    # Retourner la vue avec les messages de la salle et la salle de chat elle-même
    return render(request, 'chat.html', {'chat': chat, 'messages': messages})



def chat(request):
    """
    Récupérer tous les chats, forums et groupes pour afficher dans la sidebar.
    """
    # Récupérer tous les objets de type Chat, Forum et Groupe
    chats = Chat.objects.all()
    forums = Forum.objects.all()
    groupes = Groupe.objects.all()

    # Passer les données au template
    return render(request, 'chat.html', {
        'chats': chats,
        'forums': forums,
        'groupes': groupes
    })



def chat_detail(request, chat_id):
    # Récupère l'objet Chat par ID
    chat = get_object_or_404(Chat, id=chat_id)
    
    # Récupère les messages du chat
    messages = chat.chat_messages.all()
    participants = chat.participants_id.all()
    
    # Récupère tous les chats, forums et groupes
    chats = Chat.objects.all()
    forums = Forum.objects.all()
    groupes = Groupe.objects.all()
    
    # Passe les données au template
    return render(request, 'chat_detail.html', {
        'chat': chat,
        'messages': messages,
        'participants': participants,
        'chats': chats,
        'forums': forums,
        'groupes': groupes,
    })

def forum_detail(request, forum_id):
    # Récupère l'objet Forum par ID
    forum = get_object_or_404(Forum, id=forum_id)
    
    # Récupère les messages du forum
    messages = forum.forum_messages.all()
    participants = forum.participants_id.all()
    
    # Récupère tous les chats, forums et groupes
    chats = Chat.objects.all()
    forums = Forum.objects.all()
    groupes = Groupe.objects.all()
    
    # Passe les données au template
    return render(request, 'forum_detail.html', {
        'forum': forum,
        'messages': messages,
        'participants': participants,
        'chats': chats,
        'forums': forums,
        'groupes': groupes,
    })

def groupe_detail(request, groupe_id):
    # Récupère l'objet Groupe par ID
    groupe = get_object_or_404(Groupe, id=groupe_id)
    
    # Récupère les messages du groupe
    messages = groupe.groupe_messages.all()
    participants = groupe.participants_id.all()
    
    # Récupère tous les chats, forums et groupes
    chats = Chat.objects.all()
    forums = Forum.objects.all()
    groupes = Groupe.objects.all()
    
    # Passe les données au template
    return render(request, 'groupe_detail.html', {
        'groupe': groupe,
        'messages': messages,
        'participants': participants,
        'chats': chats,
        'forums': forums,
        'groupes': groupes,
    })


def send_chat_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.auteur_id = request.user
            message.chat = chat
            message.save()
            return redirect("chat_detail", chat_id=chat.id)
    else:
        form = ChatMessageForm()

    return render(request, "chat_detail.html", {"chat": chat, "form": form})


def send_forum_message(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)

    if request.method == "POST":
        form = ForumMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.auteur_id = request.user
            message.forum = forum
            message.save()
            return redirect("forum_detail", forum_id=forum.id)
    else:
        form = ForumMessageForm()

    return render(request, "forum_detail.html", {"forum": forum, "form": form})



def send_groupe_message(request, groupe_id):
    groupe = get_object_or_404(Groupe, id=groupe_id)

    if request.method == "POST":
        form = GroupeMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.auteur_id = request.user
            message.groupe = groupe
            message.save()
            return redirect("groupe_detail", groupe_id=groupe.id)
    else:
        form = GroupeMessageForm()

    return render(request, "groupe_detail.html", {"groupe": groupe, "form": form})
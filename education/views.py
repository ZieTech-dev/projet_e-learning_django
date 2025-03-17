from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Question, Student, Course, Evaluation, Quiz, QuizAttempt, StudentAnswer, Discussion, Message, Invoice, Payment, Choice, Note
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


def process_payment(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        # Effectuez ici le traitement du paiement (par exemple, enregistrement dans la base de données, etc.)
        # Vous pouvez également ajouter une logique pour gérer les détails spécifiques de chaque méthode de paiement.
        
        payment = Payment(
            invoice=invoice,
            payment_method=payment_method,
            amount=invoice.amount,
            payment_date=timezone.now(),
            # Ajoutez d'autres détails de paiement comme le numéro de transaction si nécessaire
        )
        payment.save()
        
        # Mettez à jour le statut de la facture
        invoice.status = 'paid'
        invoice.payment_date = payment.payment_date
        invoice.save()

        # Affichez un message de succès et redirigez
        messages.success(request, 'Le paiement a été effectué avec succès.')
        return redirect('invoice_detail', invoice_id=invoice.id)
    
    # Si ce n'est pas une requête POST, affichez simplement la facture
    return render(request, 'invoice_detail.html', {'invoice': invoice})

def user_logout(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('login')  # Redirige vers la page de connexion après la déconnexion


def index(request):

    return render(request, 'index.html')

@login_required
def dashboard(request):
    """Vue pour le tableau de bord de l'utilisateur"""
    # Récupération des données récentes de l'utilisateur
    recent_courses = Course.objects.filter(student=request.user).order_by('-start_date')[:5]
    upcoming_evaluations = Evaluation.objects.filter(student=request.user, date__gte=datetime.now()).order_by('date')[:5]
    recent_notes = Note.objects.filter(student=request.user).order_by('-created_at')[:5]
    pending_invoices = Invoice.objects.filter(student=request.user, status='pending').order_by('due_date')[:3]
    
    context = {
        'recent_courses': recent_courses,
        'upcoming_evaluations': upcoming_evaluations,
        'recent_notes': recent_notes,
        'pending_invoices': pending_invoices,
    }
    return render(request, 'dashboard.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect("dashboard")  # Rediriger vers la page d'accueil après connexion
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "login.html")


# Vue pour afficher la liste des cours
@login_required
def courses(request):
    student = get_object_or_404(Student, user=request.user)
    courses = student.courses.all()
    return render(request, 'course.html', {'courses': courses})

# Vue pour afficher les détails d'un cours et ses évaluations
@login_required
def course_detail(request, course_id):
    # Récupérer le cours en fonction de l'ID
    course = get_object_or_404(Course, id=course_id)

    # Filtrer les évaluations associées au cours et à l'étudiant connecté
    evaluations = Evaluation.objects.filter(course=course, student__user=request.user)

    # Récupérer les notes associées au cours et à l'étudiant
    notes = Note.objects.filter(course=course, student__user=request.user)

    # Passer les données au template
    return render(request, 'course_details.html', {
        'course': course,
        'evaluations': evaluations,
        'notes': notes
    })


# Vue pour afficher la liste des factures
@login_required
def invoices(request):
    student = get_object_or_404(Student, user=request.user)
    invoices = student.invoices.all()
    return render(request, 'invoices.html', {'invoices': invoices})

# Vue pour afficher la liste des quiz disponibles pour un cours
@login_required
def quiz_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = course.quizzes.all()
    return render(request, 'quizzes.html', {'course': course, 'quizzes': quizzes})


def submit_quiz(request, attempt_id):
    # Récupérer l'instance de Student associée à l'utilisateur actuel
    student = get_object_or_404(Student, user=request.user)
    
    # Récupérer la tentative de quiz
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, student=student)

    if request.method == 'POST':
        # Traiter les réponses soumises
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.replace('question_', '')
                selected_choice = get_object_or_404(Choice, id=value)
                
                # Enregistrer la réponse de l'utilisateur
                StudentAnswer.objects.create(
                    attempt=attempt,
                    question_id=question_id,
                    selected_choice=selected_choice
                )

        # Calculer le score
        score = 0
        for answer in attempt.student_answers.all():
            if answer.selected_choice.is_correct:
                score += 1

        # Enregistrer le score et marquer comme terminé
        total_questions = attempt.quiz.questions.count()
        attempt.score = (score / total_questions) * 100 if total_questions > 0 else 0
        attempt.completed_at = timezone.now()
        attempt.save()

        messages.success(request, "Quiz terminé avec succès !")
        return redirect('quiz_result', attempt_id=attempt.id)
    else:
        messages.error(request, "Méthode non autorisée.")
        return redirect('quiz_detail', quiz_id=attempt.quiz.id)
    

from django.views.decorators.csrf import csrf_exempt
def resume_quiz(request, attempt_id):
    # Récupérer l'instance de Student associée à l'utilisateur actuel
    student = get_object_or_404(Student, user=request.user)
    
    # Récupérer la tentative de quiz
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, student=student)
    
    # Rediriger vers la page des détails du quiz
    return redirect('quiz_detail', quiz_id=attempt.quiz.id)

def quiz_result(request, attempt_id):
    # Récupérer l'instance de Student associée à l'utilisateur actuel
    student = get_object_or_404(Student, user=request.user)
    
    # Récupérer la tentative de quiz
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, student=student)
    
    # Afficher les résultats du quiz
    return render(request, 'quiz_result.html', {'attempt': attempt})

@csrf_exempt
def save_quiz_progress(request, attempt_id):
    if request.method == 'POST':
        attempt = get_object_or_404(QuizAttempt, id=attempt_id, student=request.user)
        for key, value in request.POST.items():
            if key.startswith('question_'):
                answer = get_object_or_404(Choice, id=value)
                attempt.answers.add(answer)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Méthode non autorisée.'})


def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Récupérer l'instance de Student associée à l'utilisateur actuel
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Vous devez être un étudiant pour commencer ce quiz.")
        return redirect('quiz_detail', quiz_id=quiz.id)

    # Créer une nouvelle tentative de quiz
    attempt = QuizAttempt.objects.create(student=student, quiz=quiz)

    # Rediriger vers la première question du quiz
    first_question = quiz.questions.first()
    if first_question:
        return redirect('question_detail', quiz_id=quiz.id, question_id=first_question.id)
    else:
        messages.error(request, "Ce quiz n'a aucune question.")
        return redirect('quiz_detail', quiz_id=quiz.id)
    

# Vue pour afficher les détails d'un quiz et permettre à l'étudiant de le passer
@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    student = get_object_or_404(Student, user=request.user)

    # if QuizAttempt.objects.filter(student=student, quiz=quiz).exists():
    #     messages.warning(request, "Vous avez déjà terminé ce quiz.")
    #     # Redirigez vers la page des résultats du quiz
    #     attempt = QuizAttempt.objects.filter(student=student, quiz=quiz).first()
    #     return redirect('quiz_result', attempt_id=attempt.id)

    # Vérifier si une tentative de quiz est en cours
    attempt = QuizAttempt.objects.filter(student=student, quiz=quiz, completed_at__isnull=True).first()

    if request.method == 'POST':
        if not attempt:
            # Créer une nouvelle tentative de quiz si aucune n'est en cours
            attempt = QuizAttempt.objects.create(student=student, quiz=quiz)

        # Traiter les réponses soumises
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.replace('question_', '')
                selected_choice = get_object_or_404(Choice, id=value)
                StudentAnswer.objects.create(
                    attempt=attempt,
                    question_id=question_id,
                    selected_choice=selected_choice
                )

        # Si l'utilisateur soumet le quiz, calculer le score et marquer comme terminé
        if 'submit_quiz' in request.POST:
            score = 0
            for answer in attempt.student_answers.all():
                if answer.selected_choice.is_correct:
                    score += 1

            # Calculer le score (en pourcentage)
            total_questions = quiz.questions.count()
            attempt.score = (score / total_questions) * 100 if total_questions > 0 else 0
            attempt.completed_at = timezone.now()
            attempt.save()

            # Enregistrer la note dans Evaluation
            Evaluation.objects.create(
                student=request.user,
                quiz=quiz,
                score=attempt.score
            )

            messages.success(request, "Quiz terminé avec succès !")
            return redirect('quiz_result', attempt_id=attempt.id)
    else:
        messages.error(request, "Méthode non autorisée.")
        return redirect('quiz_detail', quiz_id=quiz.id)

    # Si une tentative est en cours, afficher les questions et les choix
    if attempt:
        user_answers = {answer.question.id: answer.selected_choice.id for answer in attempt.student_answers.all()}
        return render(request, 'quiz_details.html', {
            'quiz': quiz,
            'attempt': attempt,
            'user_answers': user_answers,
            'started': True,
        })
    else:
        # Si aucune tentative n'est en cours, afficher les instructions
        return render(request, 'quiz_details.html', {
            'quiz': quiz,
            'attempt': None,
            'started': False,
        })



def submit_answer(request, quiz_id, question_id):
    if request.method == 'POST':
        # Récupérer la réponse sélectionnée
        answer_id = request.POST.get('answer')
        if not answer_id:
            messages.error(request, "Veuillez sélectionner une réponse.")
            return redirect('question_detail', quiz_id=quiz_id, question_id=question_id)

        # Récupérer la réponse ou renvoyer une erreur 404 si non trouvée
        answer = get_object_or_404(Choice, id=answer_id, question_id=question_id)

        # Récupérer la tentative de quiz en cours
        attempt = QuizAttempt.objects.filter(student__user=request.user, quiz_id=quiz_id, completed_at__isnull=True).first()

        if not attempt:
            messages.error(request, "Aucune tentative de quiz active trouvée.")
            return redirect('quiz_detail', quiz_id=quiz_id)

        # Enregistrer la réponse de l'utilisateur
        attempt.answers.add(answer)

        # Passer à la question suivante
        next_question = answer.question.quiz.questions.filter(id__gt=question_id).first()
        if next_question:
            return redirect('question_detail', quiz_id=quiz_id, question_id=next_question.id)
        else:
            # Marquer la tentative comme terminée
            attempt.completed_at = timezone.now()
            attempt.save()
            messages.success(request, "Vous avez terminé le quiz !")
            return redirect('quiz_detail', quiz_id=quiz_id)

def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Récupérer l'instance de Student associée à l'utilisateur actuel
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Vous devez être un étudiant pour commencer ce quiz.")
        return redirect('quiz_detail', quiz_id=quiz.id)

    # Créer une nouvelle tentative de quiz
    attempt = QuizAttempt.objects.create(student=student, quiz=quiz)

    # Rediriger vers la page des détails du quiz
    return redirect('quiz_detail', quiz_id=quiz.id)
    
    
    

# Vue pour afficher la liste des discussions d'un cours
@login_required
def discussion_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    discussions = course.discussions.all()
    return render(request, 'discussions.html', {'course': course, 'discussions': discussions})

# Vue pour afficher les messages d'une discussion
@login_required
def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    student = get_object_or_404(Student, user=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                discussion=discussion,
                author=student,
                content=content
            )
        return redirect('discussions_details', discussion_id=discussion.id)

    messages = discussion.messages.all().order_by('created_at')
    return render(request, 'discussions_details.html', {'discussion': discussion, 'messages': messages})


def add_message(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Assurez-vous de récupérer l'instance de Student associée à l'utilisateur connecté
            student = Student.objects.get(user=request.user)
            Message.objects.create(content=content, discussion=discussion, author=student)
            messages.success(request, "Message envoyé avec succès.")
            return redirect('discussion_detail', discussion_id=discussion_id)

    return redirect('discussion_detail', discussion_id=discussion_id)
# Vue pour payer une facture
@login_required
def payer_facture(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, student__user=request.user)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        if payment_method:
            Payment.objects.create(
                invoice=invoice,
                amount=invoice.amount,
                payment_method=payment_method
            )
            invoice.status = 'paid'
            invoice.payment_date = timezone.now()
            invoice.save()
            return render(request, 'payment_success.html', {'invoice': invoice})

    return render(request, 'facture.html', {'invoice': invoice})

# Vue pour afficher les notes de l'étudiant
@login_required
def notes(request):
    student = get_object_or_404(Student, user=request.user)
    notes = Note.objects.filter(student=student).order_by('-created_at')
    return render(request, 'note.html', {'notes': notes})

# Vue pour afficher toutes les évaluations
@login_required
def evaluations(request):
    student = get_object_or_404(Student, user=request.user)
    evaluations = Evaluation.objects.filter(student=student).order_by('course__name', '-date')
    return render(request, 'evaluation.html', {'evaluations': evaluations})

# Vue pour afficher les tentatives d'un quiz spécifique
@login_required
def quiz_attempts(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    student = get_object_or_404(Student, user=request.user)
    attempts = QuizAttempt.objects.filter(quiz=quiz, student=student).order_by('-completed_at')
    return render(request, 'quiz_attempts.html', {'quiz': quiz, 'attempts': attempts})

# Vue pour afficher les détails d'une facture spécifique
@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, student__user=request.user)
    return render(request, 'invoice_detail.html', {'invoice': invoice})

# Vue pour afficher l'historique des paiements
@login_required
def payments(request):
    student = get_object_or_404(Student, user=request.user)
    payments = Payment.objects.filter(invoice__student=student).order_by('-payment_date')
    return render(request, 'payments.html', {'payments': payments})

# Vue pour le tableau de bord
@login_required
def dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    courses = student.courses.all()
    recent_evaluations = Evaluation.objects.filter(student=student).order_by('-date')[:5]
    upcoming_invoices = Invoice.objects.filter(student=student, status='pending').order_by('due_date')[:3]
    recent_notes = Note.objects.filter(student=student).order_by('-created_at')[:5]
    
    return render(request, 'dashboard.html', {
        'student': student,
        'courses': courses,
        'recent_evaluations': recent_evaluations,
        'upcoming_invoices': upcoming_invoices,
        'recent_notes': recent_notes
    })
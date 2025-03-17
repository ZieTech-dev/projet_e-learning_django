from django.urls import path
from . import views

urlpatterns = [

      path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),
    path('', views.index, name='index'),

     path('dashboard/', views.dashboard, name='dashboard'),
    # Démarrer le quiz
    path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),

    # Soumettre le quiz
    path('quiz/<int:attempt_id>/submit/', views.submit_quiz, name='submit_quiz'),  # Utilisez attempt_id

    # Sauvegarder la progression
    path('quiz/<int:attempt_id>/save/', views.save_quiz_progress, name='save_quiz_progress'),

    # Reprendre le quiz
    path('quiz/<int:attempt_id>/resume/', views.resume_quiz, name='resume_quiz'),

    # Résultats du quiz
    path('quiz/<int:attempt_id>/result/', views.quiz_result, name='quiz_result'),
    path('logout/', views.user_logout, name='logout'),
    path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),

    # Pages principales
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('invoices/', views.invoices, name='invoices'),

    # Quiz
    path('course/<int:course_id>/quizzes/', views.quiz_list, name='quiz_list'),

    # Discussions
    path('course/<int:course_id>/discussions/', views.discussion_list, name='discussion_list'),
    path('discussion/<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),

    # Paiement de facture
    path('invoice/<int:invoice_id>/pay/', views.payer_facture, name='payer_facture'),

    path("login/", views.user_login, name="login"),
    path('discussion/<int:discussion_id>/add_message/', views.add_message, name='add_message'),
    path('invoice/<int:invoice_id>/payment/', views.process_payment, name='process_payment'),

    # Nouvelles URLs pour les pages manquantes
    path('notes/', views.notes, name='notes'),
    path('evaluations/', views.evaluations, name='evaluations'),
    path('quiz/<int:quiz_id>/attempts/', views.quiz_attempts, name='quiz_attempts'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('payments/', views.payments, name='payments'),
]
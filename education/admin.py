from django.contrib import admin
from .models import (
    Course, Student, Note, Evaluation, Quiz, Question, Choice,
    QuizAttempt, StudentAnswer, Discussion, Message, Invoice, Payment
)

# class StudentAnswerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'attempt', 'question', 'selected_choice', 'is_correct')
#     readonly_fields = ('is_correct',)

# admin.site.register(StudentAnswer, StudentAnswerAdmin)




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    filter_horizontal = ('courses',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('title', 'content', 'student__user__username')
    date_hierarchy = 'created_at'

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'score', 'date')
    list_filter = ('course', 'date')
    search_fields = ('student__user__username', 'course__name', 'comment')
    date_hierarchy = 'date'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    list_filter = ('quiz',)
    search_fields = ('text', 'quiz__title')
    inlines = [ChoiceInline]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'time_limit')
    list_filter = ('course',)
    search_fields = ('title', 'description', 'course__name')

class StudentAnswerInline(admin.TabularInline):
    model = StudentAnswer
    extra = 0
    readonly_fields = ('question', 'selected_choice', 'is_correct')

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'started_at', 'completed_at', 'is_completed')
    list_filter = ('quiz', 'started_at', 'completed_at')
    search_fields = ('student__user__username', 'quiz__title')
    date_hierarchy = 'started_at'
    inlines = [StudentAnswerInline]
    readonly_fields = ('is_completed',)

@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'selected_choice', 'is_correct')
    list_filter = ('attempt__quiz',)
    search_fields = ('attempt__student__user__username', 'question__text')
    readonly_fields = ('is_correct',)

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_by', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('title', 'course__name', 'created_by__user__username')
    date_hierarchy = 'created_at'
    inlines = [MessageInline]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'discussion', 'created_at')
    list_filter = ('discussion', 'created_at')
    search_fields = ('content', 'author__user__username', 'discussion__title')
    date_hierarchy = 'created_at'

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'amount', 'created_at', 'due_date', 'status', 'is_overdue')
    list_filter = ('status', 'created_at', 'due_date')
    search_fields = ('student__user__username', 'description')
    date_hierarchy = 'created_at'
    readonly_fields = ('is_overdue',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'amount', 'payment_method', 'payment_date')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('invoice__student__user__username', 'transaction_id')
    date_hierarchy = 'payment_date'
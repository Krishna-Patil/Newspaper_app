from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.models import *
from .forms import *


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

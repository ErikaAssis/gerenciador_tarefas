from django import forms
from .models import Tarefa
from django.db import models


class TarefaForm(forms.ModelForm):
    data_expiracao = forms.DateField(
                        input_formats=['%d/%m/%Y'],
                        widget=forms.DateTimeInput(attrs={
                            'class': 'flatpickr'
                        }))

    class Meta:
        model = Tarefa
        fields = '__all__'

from .models import Veiculo
from django import forms


class InsereVeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = [
            'marca',
            'modelo',
            'cor',
            'placa',
        ]

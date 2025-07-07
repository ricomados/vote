from django import forms


class RatingForm(forms.Form):
    score = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
        label="평가 점수 (1~5)",
    ) 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = '__all__'
        fields = UserCreationForm.Meta.fields 

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # fields = '__all__'
        # fields = ('email', 'first_name', 'last_name', )
        fields = UserCreationForm.Meta.fields 
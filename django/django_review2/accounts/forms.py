from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model 
# 현재 활성화된 usermodel return  >> 특별히 안만들면 default usermodel이 나옴
## settings에 활성화 있음
class CunstomUserChangeForm(UserChangeForm):

    class Meta:
        model= get_user_model()
        fields=['email', 'first_name', 'last_name']


# default UserCreationForm은 Cunstom usermodel 정보인식 x
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
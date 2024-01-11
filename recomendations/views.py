from rest_framework import generics
from account.models import Anketa
from account.serializers import AnketaSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import CharField, Case, Value, When,IntegerField,F
from django.db.models.functions import Abs
class RecomendationsListAPIView(generics.ListAPIView):
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer
    permission_classes = [IsAuthenticated]
    
    # def list(self, request, *args, **kwargs):
    #     user = request.user
    #     print(user)
    #     queryset = Anketa.objects.exclude(user=current_user)
    #     return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        current_user = self.request.user
        queryset = Anketa.objects.exclude(user=current_user)
        current_sex = current_user.anket.first().sex
        current_age = current_user.anket.first().age
        queryset = queryset.annotate(
        is_current_sex=Case(
            When(sex=current_sex, then=Value(1)),
            When(sex='think', then=Value(2)),
            default=Value(0),
            output_field=CharField(),
        ),
        age_difference=Abs(F('age') - current_age),
        height_priority=Case(
            When(is_current_sex=1, then=F('height')),
            When(is_current_sex=0, then=-F('height')),
            default=Value(0),
            output_field=CharField(), 
        ),
        ).order_by('is_current_sex','age_difference','height_priority')
        return queryset
        


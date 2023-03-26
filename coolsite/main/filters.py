import django_filters
from .models import Lesson


class LessonFilter(django_filters.FilterSet):
    discipline_search = django_filters.CharFilter(field_name='discipline__title', lookup_expr='icontains')

    class Meta:
        model = Lesson
        fields = ['discipline', 'city', 'teacher', 'start_date', 'start_time']
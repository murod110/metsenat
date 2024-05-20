import django_filters
from .models import Sponsor, Student

class SponsorFilter(django_filters.FilterSet):
    dt = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Sponsor
        fields = ['status', 'prices', 'dt']


class StudentFilter(django_filters.FilterSet):
    dt = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Student
        fields = ['otm', 'type', 'dt']
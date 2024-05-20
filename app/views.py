from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *
from .filters import SponsorFilter, StudentFilter

months_name = {
        1: 'Yanvar',
        2: 'Fevral',
        3: 'Mart',
        4: 'Aprel',
        5: 'May',
        6: 'Iyun',
        7: 'Iyul',
        8: 'Avgust',
        9: 'Sentabr',
        10: 'Oktabr',
        11: 'Noyabr',
        12: 'Dekabr',
    }


class MyPaginationClass(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    max_page_size = 10

class LoginView(APIView):
    """
    Bu Sahifa adminni ro'ycatdan o'tishi 
    uchun qilingan default admin 
    login=admin, parol=admin
    """
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        else:
            return Response({'error': 'Foydalanuvchi nomi yoki paroli xato'}, status=401)


class SponsorApiView(ListAPIView):
    """
    Bu Homiylarni ro'yxatini chiqaradi 
    filterlaydi va to'liq ismi bo'yicha qidiradi.
    """
    queryset = Sponsor.objects.all()
    pagination_class = MyPaginationClass
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SponsorFilter
    search_fields = ['full_name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = self.queryset
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(request, queryset, self)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = SponsorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class SponsorCreateView(CreateAPIView):
    """Homiydan Ariza qabul qiluvchi api"""
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer

class SingleSponsorApi(RetrieveAPIView):
    """Homiyni id si bo'yicha ko'rish uchun ishlatiladi."""
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(
                serializer.data
            )
        except:
            return Response({
                'error':"bunday idga ega homiy mavjud emas"},status=404
            )

class SponsorUpdateView(RetrieveUpdateAPIView):
    """Homiyni tahrirlash uchun api"""
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(
                serializer.data
            )
        except:
            return Response({
                'error':"bunday idga ega homiy mavjud emas"},status=404
            )
class SponsorDeleteApiView(DestroyAPIView):
    """Homiyni ro'yxatdan o'chirish uchun ishlatiladi"""
    queryset = Sponsor.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Student 
class StudentApiView(ListAPIView):
    """Talabalar ro'yxati uchun api"""
    pagination_class = MyPaginationClass
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['full_name']
    filterset_class = StudentFilter
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = self.queryset
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(request, queryset, self)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class StudentCreateView(CreateAPIView):
    """Talaba qo'shish uchun api"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SingleStudentApi(RetrieveAPIView):
    """Talabani idsi bilan ko'rish uchun api"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            
            return Response(
                serializer.data
            )
        except:
            return Response({
                'error':"bunday idga ega student mavjud emas"},status=404
            )


class StudentUpdateView(RetrieveUpdateAPIView):
    """Talabani tahrirlash uchun api"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            
            return Response(
                serializer.data
            )
        except:
            return Response({
                'error':"bunday idga ega homiy mavjud emas"},status=404
            )

class StudentDeleteApiView(DestroyAPIView):
    """Bu api talabani o'chirish uchun ishlatiladi"""
    queryset = Student.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Statistika       
class StatisticsApiView(APIView):
    """Bu apida statistika chiqariladi"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        stats = Statistics.objects.all()
        students = Student.objects.all()
        sponsors = Sponsor.objects.all()
        student_amounts = 0
        sponsor_price = 0
        for student in students:
            student_amounts += int(student.contract)
        for sponsor in sponsors:
            if sponsor.prices == "boshqa":
                sponsor_price += int(sponsor.other_price)
            else:
                sponsor_price += int(sponsor.prices)
        years = []
        for stat in stats:
            if stat.year not in years:
                years.append(stat.year)
        data = {}
        for year in years:
            staTis = Statistics.objects.filter(year=year)
            months = {}
            for stat in staTis:
                months[months_name[int(stat.month)]]= {"yangi talaba":stat.student_count, "yangi homiy":stat.sponsor_count}
            data[stat.year] = months
        return Response({
            "Jami to'langan":sponsor_price,
            "Jami So'ralgan":student_amounts,
            "To'lanishi kerak" : sponsor_price-student_amounts,
            "statistika" : data
        })

# Sponsorship
class SponsorshipCreateApiView(CreateAPIView):
    """Bu Api talabaga Homiy biriktirish uchun"""
    queryset = Sponsor_Attachment.objects.all()
    serializer_class = SponsorshipSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        student_id = self.kwargs.get('id')

        try:
            student = Student.objects.get(id=int(student_id))
        except Student.DoesNotExist:
            return Response({'error': 'Bunday id dagi student mavjud emas.'}, status=404)

        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            sponsorship =serializer.validated_data['sponsorship']
            sponsor = serializer.validated_data['sponsor']
            # Summa to'g'ri kiritilganini tekshirish
            if sponsor.residual >= sponsorship and student.max_needed >sponsorship:
                serializer.save(student=student)
                return Response(serializer.data, status=201)
            elif sponsor.residual < sponsorship and sponsor.residual != 0:
                return Response({"error":f"Homiydan o'tkazmoqchi bo'lgan mablag'ingiz {sponsorship-sponsor.residual} ga ko'p. Homiyda qolgan mablag' {sponsor.residual}"},status=403)   
            elif student.max_needed <sponsorship and student.max_needed != 0:
                return Response({"error":f"Studentga o'tkazilayotgan mablag'ni {sponsorship-student.max_needed} ga kamaytiring. Studentga kerakli mablag' {student.max_needed}"},status=403)
            elif student.max_needed == 0:
                return Response({"error":"Student So'ralagan mablag'ni olib bo'lgan."}, status=403)
            elif sponsor.residual == 0:
                return Response({"error":"Homiy kiritgan mablag' tugagan."},status=403)
            else: return False
            
                
        
        return Response(serializer.errors, status=400)
        
class StudentSponsorView(ListAPIView):
    """Bu talabaga biriktirilgan homiylarni ko'rish uchun ishlatiladi"""
    serializer_class = SponsorshipSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        student_id = self.kwargs['id']
        return Sponsor_Attachment.objects.filter(student_id=student_id)
# Search view
class CombinedSearchApiView(APIView):
    """Bu api talaba yoki homiyni to'liq ishmi va hmiyni tashiloti bilan qidirish uchun"""
    filter_backends = [SearchFilter]
    search_fields = {
        'sponsor': ['full_name', 'organization'],
        'student': ['full_name','type']
    }

    def get(self, request):
        search_term = request.query_params.get('search', '')

        sponsors = Sponsor.objects.all()
        students = Student.objects.all()

        if search_term:
            sponsors = self.filter_queryset(sponsors, 'sponsor')
            students = self.filter_queryset(students, 'student')

        sponsor_serializer = SponsorSerializer(sponsors, many=True)
        student_serializer = StudentSerializer(students, many=True)

        return Response({
            'sponsors': sponsor_serializer.data,
            'students': student_serializer.data
        }, status=200)

    def filter_queryset(self, queryset, model_name):
        search_fields = self.search_fields[model_name]
        backend = SearchFilter()
        request = self.request._request
        request.query_params = request.GET.copy()
        request.query_params['search'] = self.request.query_params.get('search', '')
        return backend.filter_queryset(request, queryset, self)
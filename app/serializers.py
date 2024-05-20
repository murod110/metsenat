from rest_framework.serializers import ModelSerializer
from .models import Sponsor, Student, Sponsor_Attachment

class SponsorCreateSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['full_name', 'person_type', 'phone', 'prices', 'other_price']

class SponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id','full_name', 'person_type', 'phone', 'prices', 'other_price','spent', 'organization','status','dt']
        

    def create(self, validated_data):
        sponsor = Sponsor.objects.create(**validated_data)
        return sponsor

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','full_name', 'phone', 'otm', 'type','appected', 'contract','dt']

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student
    
class SponsorshipSerializer(ModelSerializer):
    class Meta:
        model = Sponsor_Attachment
        fields = ['student', 'sponsor', 'sponsorship']
    
    def create(self, validated_data):
        sponsorship = Sponsor_Attachment.objects.create(**validated_data)
        return sponsorship


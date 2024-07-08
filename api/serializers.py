from rest_framework import serializers
from crud.models import Student,Classroom


#serializers are the feature provided by DRF to serialize and deserialize the objects in API
#serialization is the process of changing the pyhtin objects to json 


class ClassRoomSeralizer(serializers.Serializer):
    id=serializers.IntegerField(required=False)
    
    name=serializers.CharField()
    section=serializers.CharField()

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields=["id","name","section"]


class StudentSeralizer(serializers.Serializer):
    id=serializers.IntegerField(required=False)
    
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    address=serializers.CharField()    

class StudentModelSerializer(serializers.ModelSerializer):
    #classroom=ClassRoomModelSerializer()
    class Meta:
        model=Student
        fields=["id","name","age","email","address","classroom"]
 
    def get_fields(self):
        fields=super().get_fields()
        request=self.context.get("request")
        if request.method and request.method == "GET":
           fields["classroom"] = ClassRoomModelSerializer()
        return fields
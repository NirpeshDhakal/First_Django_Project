from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from crud.models import Classroom,Student
from .serializers import ClassRoomSeralizer,StudentSeralizer,ClassRoomModelSerializer,StudentModelSerializer


class MessageView(APIView):
    def get(self, *args, **kwargs):
        return Response({
            "message":"this is my first api"
        })
    
class SimpleStudentView(APIView):
    def get(self, *args, **kwargs):
        return Response({
            "name":"jon",
            "age":20,
            "address":"ktm"
        })
    
class ClassRoomDetailView(APIView):
    def get(self, *args, **kwargs):
        classroom_id=kwargs["id"]
        try:
            classroom = Classroom.objects.get(id=classroom_id)
        except:
            return Response({
                "message":"invalid id"
            })
        classroom=Classroom.objects.get(id=classroom_id)
        return Response({
            "id":classroom.id,
            "name":classroom.name,
            "section":classroom.section               })
    


class StudentRoomDetailView(APIView):
    def get(self, *args, **kwargs):
        student_id=kwargs["id"]
        try:
            student = Student.objects.get(id=student_id)
        except:
            return Response({
                "message":"invalid id"
            })
        student=Student.objects.get(id=student_id)
        return Response({
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "email":student.email,
            "address":student.address,
            "classroom":student.classroom.id
                                                                    })
class ClassroomListView(APIView):
    def get(self,*args,**kwargs):
        classrooms=Classroom.objects.all()
        response=[]
        for classroom in classrooms:
            response.append({
                "id":classroom.id,
                "name":classroom.name,
                "section":classroom.section


            })
        return Response(response)
    def post(self,*args,**kwargs):
        data=self.request.data
        name=data.get("name")
        section=data.get("section")
        classroom=Classroom.objects.create(name=name,section=section)
        return Response({
            "message":"Classroom created successfully",
            "id":classroom.id,
            "name":classroom.name,
            "section":classroom.section,
        })
 
class StudentListView(APIView):
    def get(self,*args,**kwargs):
        students=Student.objects.all()
        response=[]
        for student in students:
            response.append({
                "id":student.id,
                "name":student.name,
                "age":student.age,
                "email":student.email,
                "address":student.address,
                "classroom":student.classroom.id if student.classroom else None


            })
        return Response(response)        

    def post(self,*args,**kwargs):
        data=self.request.data
        name=data.get("name")
        age=data.get("age")
        email=data.get("email")
        address=data.get("address")
        student=Student.objects.create(name=name,age=age,email=email,address=address)
        return Response({
            "message":"Student created successfully",
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "email":student.email,
            "address":student.address,
            
        })
        
  
class ClassRoomDetailUsingSerView(APIView):
    def get(self,*args,**kwargs):
        classroom_id=kwargs["id"]
        try:
            classroom=Classroom.objects.get(id=classroom_id)
        except:
            return Response({
                "message":"inavalid id"
            })
        
        serializer=ClassRoomSeralizer(classroom)
        return Response(serializer.data)

        
class StudentDetailUsingSerView(APIView):
    def get(self,*args,**kwargs):
        student_id=kwargs["id"]
        try:
            student=Student.objects.get(id=student_id)
        except:
            return Response({
                "message":"inavalid id"
            })
        
        serializer=StudentSeralizer(student)
        return Response(serializer.data)

class ClassroomListUsingSerView(APIView):
    def get(self, *args,**kwargs):
        query_dict=self.request.GET
        search=query_dict.get("search")
        section=query_dict.get("section")
        if search and section:
            classrooms=Classroom.objects.filter(name__startwith=search,section=section)
        elif search:
            classrooms=Classroom.objects.filter(name__startwith=search)
        elif section:
            classrooms=Classroom.objects.filter(section=section) 
        else:    
             classrooms=Classroom.objects.all()
        serializer=ClassRoomSeralizer(classrooms,many=True)
        return Response(serializer.data)
    def post(self,*args,**kwargs):
        data=self.request.data
        
        serializer=ClassRoomSeralizer(data=data) #this is deserialization

        if serializer.is_valid():
            validated_data=serializer.validated_data
            print(validated_data)
            name=validated_data.get("name")
            section=validated_data.get("section")
            classroom=Classroom.objects.create(name=name,section=section)
        return Response({
            "message":"Classroom created successfully",
            "id":classroom.id,
            "name":classroom.name,
            "section":classroom.section,
        })

    
class StudentListUsingSerView(APIView):
    def get(self, *args,**kwargs):
        students=Student.objects.all()
        serializer=StudentSeralizer(students,many=True)
        return Response(serializer.data) 
    def post(self,*args,**kwargs):
        data=self.request.data
        
        serializer=StudentSeralizer(data=data) #this is deserialization

        if serializer.is_valid():
            validated_data=serializer.validated_data
            print(validated_data)
            name=validated_data.get("name")
            age=validated_data.get("age")
            email=validated_data.get("email")
            address=validated_data.get("address")
            student=Student.objects.create(name=name,age=age,email=email,address=address)
        return Response({
            "message":"Student created successfully",
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "email":student.email,
            "address":student.address,
        },status=201)   
    

class ClassRoomView(APIView):
    def get(self,*args,**kwargs):
        classrooms=Classroom.objects.all()
        serializer=ClassRoomModelSerializer(classrooms,many=True,context={"request":self.request})
        return Response(serializer.data)
    
    def post(self,*args,**kwargs):
        data=self.request.data
        serializer=ClassRoomModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"classroom created successfully",
                "data":serializer.data
            },status=201)
        return Response(serializer.errors,status=400)




class StudentView(APIView):
    def get(self,*args,**kwargs):
        students=Student.objects.all()
        serializer=StudentModelSerializer(students,many=True,context={"request":self.request})
        return Response(serializer.data)
    
    def post(self,*args,**kwargs):
        data=self.request.data
        serializer=StudentModelSerializer(data=data, context={"request":self.request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Student created successfully",
                "data":serializer.data
            },status=201)
        return Response(serializer.errors,status=400)
    
class ClassRoomGenericView(ListAPIView):
    serializer_class=ClassRoomModelSerializer
    queryset=Classroom.objects.all()

class ClassRoomGenericCreateView(CreateAPIView):
    serializer_class=ClassRoomModelSerializer

class ClassRoomListCreateView(ListCreateAPIView):
    serializer_class=ClassRoomModelSerializer
    queryset=Classroom.objects.all()


class ClassRoomUpdateGenericView(UpdateAPIView):
    serializer_class=ClassRoomModelSerializer
    queryset=Classroom.objects.all()
    



class ClassRoomUpdateDetailsDelete(RetrieveUpdateDestroyAPIView):
     serializer_class=ClassRoomModelSerializer
     queryset=Classroom.objects.all()


class StudentDetailsUpdateDelete(RetrieveUpdateDestroyAPIView):
     serializer_class=StudentModelSerializer
     queryset=Classroom.objects.all()


class ClassRoomViewset(ModelViewSet):
     serializer_class=ClassRoomModelSerializer
     queryset=Classroom.objects.all()     
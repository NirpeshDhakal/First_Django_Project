from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import(MessageView,SimpleStudentView,ClassRoomDetailView,StudentRoomDetailView,ClassroomListView,
                   StudentListView,ClassRoomDetailUsingSerView,StudentDetailUsingSerView,ClassroomListUsingSerView,StudentListUsingSerView,
                   ClassRoomView,StudentView,ClassRoomGenericView,ClassRoomGenericCreateView,ClassRoomListCreateView,ClassRoomUpdateGenericView,ClassRoomUpdateDetailsDelete
                   ,StudentDetailsUpdateDelete,ClassRoomViewset)

router=DefaultRouter()
router.register("classroom-viewset",ClassRoomViewset,basename="classroom")

urlpatterns=[

    path("message/",MessageView.as_view()),
    path("simple-student/",SimpleStudentView.as_view()),
    path("classroom/<int:id>/",ClassRoomDetailView.as_view()),
    path("classroom-list/",ClassroomListView.as_view()),
    path("student-list/",StudentListView.as_view()),
    path("student/<int:id>/",StudentRoomDetailView.as_view()),

]

urls_for_serializer_views=[
    path("classroom-using-serializer/<int:id>/",ClassRoomDetailUsingSerView.as_view()),
    path("student-using-serializer/<int:id>/",StudentDetailUsingSerView.as_view()),
    path("classroom-list-using-serializer/",ClassroomListUsingSerView.as_view()),
    path("student-list-using-serializer/",StudentListUsingSerView.as_view()),
    path("classroom-model-ser/",ClassRoomView.as_view()),
    path("student-model-ser/",StudentView.as_view())
    

]

urlpatterns+=urls_for_serializer_views

urls_for_generic_view=[
    path("classroom-generic-view/",ClassRoomGenericView.as_view()),
    path("classroom-generic-create-view/",ClassRoomGenericCreateView.as_view()),
    path("classroom-list-create/",ClassRoomListCreateView.as_view()),

    path("classroom-update/<int:pk>/",ClassRoomUpdateGenericView.as_view()),
    path("classroom-update-delete/<int:pk>/",ClassRoomUpdateDetailsDelete.as_view()),
    path("student-update-delete<int:pk>/",StudentDetailsUpdateDelete.as_view())
    
]
urlpatterns+=urls_for_serializer_views+urls_for_generic_view+router.urls



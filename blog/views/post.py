from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import PostSerializers
from ..models import Post
from ..ai_content.service.summarize import summarize_post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() # بستخدم ال default انه اجيب كل البوستات في الداتا بيس
    serializer_class = PostSerializers
@api_view(['GET'])  #عشان نحدد بالزبط شو اللي بقدر يعمله المستخدم يعني حاليا بس بقدر يعمل Get انما من غير المسموح مثلا يعمل ابديت
def get_posts(request):  #في الاعلى كان Default وكان عبارة عن class انما في ال custmize بتكون function
    try : #عملنا try عشان لو صار اخطاء ما يوقف كل النظام
        page =int(request.query_params.get('page',1)) # هنا عبارة عن انه مثلا عنا داتا بيس فيها 50 Row بدنا نحط كل صفحة عدد من ال rows
        limit =int(request.query_params.get('limit',10))# في الاعلى كان ال default للصفحة =1 وهنا الليمت = 10
        start = (page-1)*limit
        end = start + limit
        posts = Post.objects.filter(category='AI')[start:end] # هنا بدنا نجيب كل البوستات اللي ال category تبعها هي AI
        serializer = PostSerializers(posts, many=True)
        return Response(
            {'post':serializer.data,'page':page,'limit':limit}
        )
    except Exception :
        return Response(
            {'error':'An unexpected error occurred!'},
            status = status.HTTP_500_INTERNAL_SERVER_ERROR, #لما انا احكي 500 يعني الايرور من عندي انا كسيرفر, عشان اعرف انه المشكلة من جهتي
        )

@api_view(['POST'])
def summarize_post_view(request, post_id):
    try:
        result = summarize_post(post_id)
        return Response(result, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



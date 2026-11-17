from rest_framework import serializers
from ..models.post import Post

class PostSerializers (serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields =('id','title','content','created_at','updated_at') #هاد مخصص اني خصصت بس بعض الاعمدة, بستخدمها لما يكون في Security information
        fields = '__all__' #هنا افتراضي يعني الكل
        read_only_fields = ('title_id',) #هاي ال fields اللي ما بقدر انا اغيره او اعدله هاي بتكون للقراءة فقط دون تعديل

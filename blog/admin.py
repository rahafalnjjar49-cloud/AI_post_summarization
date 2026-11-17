from django.contrib import admin

from .models import Post,User,Category,Comment


#admin.site.register(Post)

@admin.register(Post) #هاي عشان نحط الداشبور للمودل اللي بدنا ياه
#عشان نعمل custmize اكثر ونعطي صلاحيات بدل ما تكون عامة
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id','title', 'author') # شو الاشي اللي لازم يظهر , لو ماكان في مثلا author مش موجود في ال display ما بتقدر تحطه في ال filter
    list_filter = ('title_id','title', 'author') # يتم فلترتها بناءا على اكثر نت شيء
    search_fields = ('title_id','title' ,'author')
    ordering = ('title_id','title' ,'author')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name')

admin.site.register(Category)
admin.site.register(Comment)



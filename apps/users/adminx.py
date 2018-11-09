import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile
from courses.models import Course, Lesson, Video, CourseResource
from operation.models import CourseComments, UserCourse, UserFavorite, UserMessage, UserAsk
from organization.models import CityDict, Teacher, CourseOrg

# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '测试后台管理系统'
    site_footer = '测试网'
    # 收起菜单
    menu_style = 'accordion'

# ------


class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin:
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


'''
 直接修改 xadmin 的源码，即 xadmin/plugins/auth.py 里添加这两行代码
from django.contrib.auth import get_user_model
User = get_user_model()
 就可以代替下面那段代码
'''
# ---
# class UserProfileAdmin(UserAdmin):
#     pass


# 卸载 django 自带的 auth_user
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)


# 继承自定义的 UserProfile 覆盖 django 自带的 auth_user
# xadmin.site.register(UserProfile, UserProfileAdmin)
# --


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Главная страница/', Main_Page.as_view(), name='Main_Page'),
    path('Вторые блюда с фото/', Second_Budes_With_Photos.as_view(), name='Second_Budes_With_Photos'),
    path('Вторые блюда списком/', Second_Budes_List.as_view(), name='Second_Budes_List'),
    path('Десерты с фото/', Desserts_With_Photos.as_view(), name='Desserts_with_photos'),
    path('Десерты списком/', Desserts_List.as_view(), name='Desserts_list'),
    path('Салаты с фото/', Salads_With_Photos.as_view(), name='Salads_with_photos'),
    path('Салаты списком/', Salads_List.as_view(), name='Salads_list'),
    path('Супы с фото/', Soups_With_Photos.as_view(), name='Soups_with_photos'),
    path('Супы списком/', Soups_List.as_view(), name='Soups_list'),
    path('Контакты/', Contacts.as_view(), name='Contacts'),
    path('Помощь/', Help.as_view(), name='Help'),
    path('Рецепт/<int:pk>/', Recipe.as_view(), name='Recipe'),
    path('Добавление рецепта/', New_Recipe.as_view(), name='New_recipe'),
    path('Регистрация/', Register.as_view(), name="register"),
    path('Подтверждение регистрации/', Confirmation_Of_Registration.as_view(), name='confirmation'),
    path('Выход/', LogoutView.as_view(next_page='Main_Page'), name='logout'),
    path('Профиль/', Profile.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

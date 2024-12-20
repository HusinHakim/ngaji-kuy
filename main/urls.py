from django.urls import path
from main.views import show_main, create_quran_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, add_quran_entry_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_quran
from main.views import delete_quran
from main.views import create_product_flutter
app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-quran-entry', create_quran_entry, name='create_quran_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-quran/<uuid:id>', edit_quran, name='edit_quran'),
    path('delete/<uuid:id>', delete_quran, name='delete_quran'),
    path('create-quran-entry-ajax', add_quran_entry_ajax, name='add_quran_entry_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    

]
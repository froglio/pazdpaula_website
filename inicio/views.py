from django.shortcuts import render
from django.views.generic import ListView
from . models import Post

from django.db import connection
from tools.views import dict_fetch_all

def post_list(request):
    sql_script = """SELECT ip.*, u.last_name, u.first_name FROM inicio_post ip
                    INNER JOIN auth_user u ON
                    ip.autor_id = u.id
                    ORDER BY ip.id DESC"""

    cursor = connection.cursor()
    cursor.execute(sql_script)

    object_list = dict_fetch_all(cursor)

    last_post = object_list[0].get('id', 0)

    return render(request, 'inicio/home.html', {'object_list': object_list,
                                                'last_post_id': last_post})

    


# class PostListView(ListView):
#     model = Post
#     template_name = 'inicio/home.html'
    
#     def get_last_post(request):
#         sql_script = "SELECT id FROM inicio_post ORDER BY id DESC LIMIT 0, 1"
        
#         cursor = connection.cursor()
#         cursor.execute(sql_script)

#         last_post = dict_fetch_all(cursor)

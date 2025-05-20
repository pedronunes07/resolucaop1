from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todos import views
from todos.views import (
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView,
    dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Página inicial é o login
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Cadastro de usuário
    # Inclui todas as URLs do app todos
    path('', include('todos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

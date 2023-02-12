from django.contrib import admin
from django.urls import path
from trade import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pnl/<str:strategy_id>', views.Get_PNL),
]

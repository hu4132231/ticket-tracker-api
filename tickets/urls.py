from django.urls import path

from .views import TicketDetailView, TicketListCreateView


urlpatterns = [
    path("tickets/", TicketListCreateView.as_view(), name="ticket-list-create"),
    path(
        "tickets/<int:pk>/",
        TicketDetailView.as_view(),
        name="ticket-detail",
    ),
]# as_view() 是把 Class-based View 轉成 Django 可以接收網址請求的形式。
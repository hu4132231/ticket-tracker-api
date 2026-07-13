from rest_framework import generics
# generics 提供已經寫好的常用 API 功能，不需要從零處理每一種 HTTP 請求。

from .models import Ticket
from .serializers import TicketSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    # ListCreateAPIView＝ 全部資料＋新增
    queryset = Ticket.objects.all().order_by("-created_at")#新資料排前
    # 從資料庫取出 Ticket 模型的所有資料紀錄，再依 created_at 建立時間做由新到舊排序。
    serializer_class = TicketSerializer


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroyAPIView ＝ 指定一筆＋查詢／修改／刪除
    queryset = Ticket.objects.all()# 這個 View 可以從所有 Ticket 中，找到網址指定的那一筆。
    serializer_class = TicketSerializer
# Ticket Tracker API

使用 Django REST Framework 與 SQLite 開發的 Ticket 管理 API，可新增、查詢、修改及刪除問題單。

## 功能

- 新增 Ticket
- 查詢全部 Ticket
- 查詢單一 Ticket
- 完整或部分修改 Ticket
- 刪除 Ticket
- Ticket 狀態管理：Open、In Progress、Closed

## 技術

- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

| Method | Endpoint | 功能 |
|---|---|---|
| GET | `/api/tickets/` | 查詢全部 Ticket |
| POST | `/api/tickets/` | 新增 Ticket |
| GET | `/api/tickets/<id>/` | 查詢單一 Ticket |
| PUT | `/api/tickets/<id>/` | 完整修改 Ticket |
| PATCH | `/api/tickets/<id>/` | 部分修改 Ticket |
| DELETE | `/api/tickets/<id>/` | 刪除 Ticket |

## 安裝與執行

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
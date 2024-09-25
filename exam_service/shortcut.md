
```
md exam_service\app  & echo > exam_service\app\__init__.py  & echo > exam_service\app\models.py  & echo > exam_service\app\routers.py  & echo > exam_service\app\database.py
```

uvicorn app:app --reload --port 8001

from flask import request
from app.services.book import upload_book_service
from app.interfaces import Response


def upload_book_controller():
    try:
        req_json = request.get_json()
        title = req_json.get('title')
        language_id = req_json.get('language_id')
        if not title or not language_id:
            return None
        book = upload_book_service(title, language_id)
        if book:
            return Response.create(True, "Create book successfully", None)
        return Response.create(False, "Can not create new book", None)
    except:
        return Response.create(False, "Can not create new book", None)

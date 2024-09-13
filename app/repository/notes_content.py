from .base import BaseRepository
from ..models.notes_content import NotesContentModel


class NotesRepository(BaseRepository):
    MODEL_CLASS = NotesContentModel
from .base import BaseRepository
from ..models.notes import NotesModel


class NotesRepository(BaseRepository):
    MODEL_CLASS = NotesModel
from app.models import db, Note
import datetime

now = datetime.datetime.utcnow()
def seed_notes():
    notes = [
    Note(
    heading='Parents Anniversary',
    description='Buy them a cake!',
    notebook_id='1',
    user_id='1',
    created_at=now
    ),
    Note(
    heading='Capstone Project',
    description='Finish by Friday!',
    notebook_id='2',
    user_id='1',
    created_at=now
    ),
    Note(
    heading='Gym Schedule',
    description='Get ready for hot boy summer!',
    notebook_id='3',
    user_id='1',
    created_at=now
    ),
    Note(
    heading='Demo heading',
    description='Demo description',
    notebook_id='1',
    user_id='1',
    created_at=now
    ),
    Note(
    heading='Marnie heading',
    description='Marnie description',
    notebook_id='1',
    user_id='2',
    created_at=now
    ),
    Note(
    heading='Bobbie heading',
    description='Bobbie description',
    notebook_id='1',
    user_id='3',
    created_at=now
    ),
    ]

    for note in notes:
        db.session.add(note)
    db.session.commit()


def undo_notes():
    db.session.execute('TRUNCATE notes RESTART IDENTITY CASCADE;')
    db.session.commit()
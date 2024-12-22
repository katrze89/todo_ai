import pytest
from datetime import datetime, timedelta
from uuid import uuid4, UUID
from unittest.mock import patch
from freezegun import freeze_time

from core.task.create import init_task
def test_create_minimal_valid_task():
    mock_uuid4 = UUID('d2005d90-f90d-4b6f-94b6-f63d95830262')
    with freeze_time("2024-12-12"), patch("uuid.uuid4", return_value=mock_uuid4):
        name = 'My task name'
        task = init_task(name=name)

        assert task == {'name': name, 'status': 'pending', "id": mock_uuid4, "created_at": datetime(2024, 12, 12)}


def test_create_task_with_empty_name():
    with pytest.raises(ValueError, match='Task name is required'):
        init_task(name='')


def test_create_task_with_invalid_name():
    with pytest.raises(ValueError, match='Task name is required'):
        init_task(name='    ')


# def test_create_task_with_all_options():
#     with freeze_time("2024-12-12"):
#         payload = {
#             'name': 'My task name',
#             'description': 'My description',
#             'start_datetime': datetime.now() + timedelta(days=1),
#             'duration': timedelta(minutes=10),
#             'estimated_duration': timedelta(minutes=15),
#             'type': 'Meeting',
#             'priority': 'low',
#         }

#         task = create_task(**payload)

#         assert task == {**payload, "id": 1, "status": "pending", "created_at": datetime(2024, 12, 12)}


# def test_create_task_with_past_datetime():
#     pass


# def test_create_task_with_non_positive_duration():
#     pass


# def test_create_task_with_non_positive_estimated_duration():
#     pass
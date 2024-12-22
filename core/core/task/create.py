from datetime import datetime

import uuid


def init_task(name: str) -> dict[str, str | uuid.UUID | datetime]:
	"""
	Initializes a to-do task with the provided name, generating a unique ID and
	capturing the creation timestamp. The task is assigned a "pending" status
	by default.

	:param name: The name of the task to initialize. Must not be empty.
	:type name: str
	:raises ValueError: If the provided task name is empty.
	:return: A dictionary containing the task's name, status, unique ID, and
	    creation timestamp.
	:rtype: dict[str, str | uuid.UUID | datetime]
	"""

	cleaned_name = name.strip()

	if cleaned_name == '':
		raise ValueError('Task name is required.')

	return {'id': uuid.uuid4(), 'name': name, 'status': 'pending', 'created_at': datetime.now()}

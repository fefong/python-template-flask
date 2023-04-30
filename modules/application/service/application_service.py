from modules.application.model.application import Application
from modules.application.repository import application_repository as repository


def get_applications() -> list[Application]:
    applications = repository.find_all()
    return applications


def get_application(id: int) -> Application:
    application = repository.find_by_id(id)
    if application is None:
        raise Exception
    return application


def create_application(id: int, name: str, email: str) -> int:
    application = Application(id, name, email)
    repository.save(application)
    return application.id


def update_application(id: int, application_modified: Application) -> int:
    application = repository.find_by_id(id)
    if application is None:
        raise Exception
    application_id = repository.update(id, application_modified)
    return application_id


def update_full_application(id: int, application_modified: Application) -> int:
    application = repository.find_by_id(id)
    if application is None:
        raise Exception
    application_id = repository.update(id, application_modified)
    return application_id


def delete_application(id: int) -> int:
    application = get_application(id)
    if application is None:
        raise Exception
    repository.delete(id)
    return id

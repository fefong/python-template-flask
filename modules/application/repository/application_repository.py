from modules.application.model.application import Application


def find_by_id(id: int) -> Application:
    # TODO: find by id
    return None


def find_all() -> list[Application]:
    # TODO: find all
    applications: list[Application] = []
    return applications


def save(application: Application) -> int:
    # TODO: save
    return application.id


def update(id: int, application_modified: Application) -> int:
    # TODO: update
    return id


def delete(id: int) -> int:
    # TODO: delete
    return id

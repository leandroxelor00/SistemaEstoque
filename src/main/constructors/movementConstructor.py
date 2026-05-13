from src.controlers.movementController import MovementController
from src.views.viewMovement import ViewMovimento

def movementConstructor(page):
    viewMovevement = ViewMovimento()
    MovementController(page,viewMovevement)

    return viewMovevement.build()
from src.controlers.searchMovementController import SearchMovementController
from src.views.viewShowMovement import ViewShowMovement

def searchMovementConstructor(page):
    viewShowMovement = ViewShowMovement()
    SearchMovementController(page,viewShowMovement)

    return viewShowMovement.build()
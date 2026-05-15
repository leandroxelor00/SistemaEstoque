from src.views.viewMovement import ViewMovement

def movementConstructor(page):
    viewMovevement = ViewMovement(page)

    return viewMovevement.build()
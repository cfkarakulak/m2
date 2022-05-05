from masonite.routes import Route

ROUTES = [
    Route.get('/contractors', 'ContractorController@index')
]
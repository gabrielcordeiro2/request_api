import requests

class SwapiApiConsumer:
    '''
        Teste
    '''
    @classmethod
    def get_starships(cls, page: int) -> any:
        '''
            Texto
        '''
        params = {'page': page}
        response = requests.get('https://swapi.dev/api/starships/', params=params)

        return response.json()

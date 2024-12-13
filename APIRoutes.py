class APIRoutes:
    BASE_URLS = {
        'dog_api': 'https://dog.ceo/api/',
        'brewerydb': 'https://api.openbrewerydb.org/v1/',
        'jsonplace': 'https://jsonplaceholder.typicode.com/',
    }

    @classmethod
    def _build_url(cls, base_key, path, **params):
        base_url = cls.BASE_URLS[base_key]
        url = f'{base_url}{path}'
        if params:
            query_string = '&'.join(f'{key}={value}' for key, value in params.items())
            url = f'{url}?{query_string}'
        return url
    @classmethod
    def get_dog_breeds(cls):
        return cls._build_url('dog_api', 'breeds/list/all')

    @classmethod
    def get_random_dog_image(cls):
        return cls._build_url('dog_api', 'breeds/image/random')

    @classmethod
    def get_dog_images_by_breed(cls, breed):
        return cls._build_url('dog_api', f'breed/{breed}/images')

    @classmethod
    def get_breweries_by_city(cls, city, per_page=3):
        return cls._build_url('brewerydb', 'breweries', by_city=city, per_page=per_page)

    @classmethod
    def get_random_breweries(cls, size=3):
        return cls._build_url('brewerydb', 'breweries/random', size=size)

    @classmethod
    def search_breweries(cls, query, per_page=3):
        return cls._build_url('brewerydb', 'breweries/search', query=query, per_page=per_page)

    @classmethod
    def autocomplete_breweries(cls, query):
        return cls._build_url('brewerydb', 'breweries/autocomplete', query=query)

    @classmethod
    def get_posts_by_filter(cls, **filters):
        return cls._build_url('jsonplace', 'posts', **filters)

    @classmethod
    def get_post_by_id(cls, post_id):
        return cls.get_posts_by_filter(id=post_id)
    
    @classmethod
    def get_posts_by_title(cls, title):
        return cls.get_posts_by_filter(title=title)
    
    @classmethod
    def get_posts_by_body(cls, body):
        return cls.get_posts_by_filter(body=body)
    
    @classmethod
    def get_posts_by_user(cls, user_id):
        return cls.get_posts_by_filter(userId=user_id)
def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'},
        {
            'id': 2,
            'name': 'Table'
        }]


def load_product(kw=None):
   products= [{
        'id': 1,
        'name': 'Iphone 13',
        'price': 20000000,
        'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
            },
        {
            'id': 1,
            'name': 'Iphone 13',
            'price': 20000000,
            'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
        },
        {
            'id': 1,
            'name': 'Iphone 13',
            'price': 20000000,
            'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
        },
        {
            'id': 1,
            'name': 'Iphone 13',
            'price': 20000000,
            'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
        },
        {
            'id': 1,
            'name': 'Iphone 12',
            'price': 20000000,
            'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
        },
        {
            'id': 1,
            'name': 'ipad 13',
            'price': 20000000,
            'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
        },
        {
            'id': 1,
            'name': 'Iphone 13',
            'price': 20000000,
            'image': "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-11.png"
        },
        ]
   if kw:
        products=[p for p in products if p['name'].find(kw)>=0]
   return products

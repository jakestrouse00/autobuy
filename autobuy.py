import requests


class get:
    @staticmethod
    def order(APIKey, order):
        r = requests.get(f'https://autobuy.io/api/Order/{order}', headers={'APIKey': APIKey})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid order ID or invalid APIKey")

    @staticmethod
    def orders(APIKey, page):
        r = requests.get(f'https://autobuy.io/api/Orders?page={page}', headers={'APIKey': APIKey})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid page number or invalid APIKey")

    @staticmethod
    def products(APIKey):
        r = requests.get('https://autobuy.io/api/Products', headers={'APIKey': APIKey})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey")

    @staticmethod
    def product(APIKey, id):
        r = requests.get('https://autobuy.io/api/Product',
                         headers={'APIKey': APIKey, 'content-type': 'application/x-www-form-urlencoded'},
                         data={'id': id})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey or invalid product ID")


class product:
    @staticmethod
    def create(APIKey, name, description, price, productType, unlisted=False, blockProxy=False, purchaseMax='100000',
               purchaseMin='1', webhookUrl=None, serials=[], stockDelimiter=','):
        payload = {
            'Name': name,
            'Description': description,
            'Price': price,
            'ProductType': productType,
            'Unlisted': unlisted,
            'BlockProxy': blockProxy,
            'PurchaseMax': purchaseMax,
            'PurchaseMin': purchaseMin,
            'WebhookUrl': webhookUrl,
            'StockDelimiter': stockDelimiter,
            'Serials': serials

        }
        r = requests.post('https://autobuy.io/api/Product',
                          headers={'content-type': 'application/x-www-form-urlencoded', 'APIKey': APIKey}, data=payload)
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey or invalid parameter(s)")

    @staticmethod
    def update(APIKey, id, name, description, price, productType, unlisted, blockProxy, purchaseMax, purchaseMin,
               webhookUrl, stockDelimiter, serials):
        payload = {
            'id': id,
            'name': name,
            'description': description,
            'price': price,
            'productType': productType,
            'unlisted': unlisted,
            'blockProxy': blockProxy,
            'purchaseMax': purchaseMax,
            'purchaseMin': purchaseMin,
            'webhookUrl': webhookUrl,
            'stockDelimiter': stockDelimiter,
            'serials': serials

        }
        r = requests.put('https://autobuy.io/api/Product',
                         headers={'content-type': 'application/x-www-form-urlencoded', 'APIKey': APIKey}, data=payload)
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey or invalid parameter(s)")

    @staticmethod
    def delete(APIKey, id):
        requests.delete('https://autobuy.io/api/Product',
                        headers={'content-type': 'application/x-www-form-urlencoded', 'APIKey': APIKey},
                        data={'id': id})

    @staticmethod
    def addStock(APIKey, id, serial):
        productJson = get.product(APIKey=APIKey, id=id)
        # couldn't append to the original list. Used a quick solution
        p = []
        for j in productJson['serials']:
            p.append(j)
        p.append(serial)
        updatedProduct = product.update(APIKey, productJson['id'], productJson['name'], productJson['description'],
                                        productJson['price'],
                                        productJson['productType'], productJson['unlisted'], productJson['blockProxy'],
                                        productJson['purchaseMax'], productJson['purchaseMin'],
                                        productJson['webhookUrl'], productJson['stockDelimiter'], p)
        return updatedProduct

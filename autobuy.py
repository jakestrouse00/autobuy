import requests


class Get:
    def __init__(self, APIKey):
        self.APIKey = APIKey

    def order(self, order):
        r = requests.get(f'https://autobuy.io/api/Order/{order}', headers={'APIKey': self.APIKey})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid order ID or invalid APIKey")

    def orders(self, page):
        r = requests.get(f'https://autobuy.io/api/Orders?page={page}', headers={'APIKey': self.APIKey})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid page number or invalid APIKey")

    def products(self):
        r = requests.get('https://autobuy.io/api/Products', headers={'APIKey': self.APIKey})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey")

    def product(self, id):
        r = requests.get('https://autobuy.io/api/Product',
                         headers={'APIKey': self.APIKey, 'content-type': 'application/x-www-form-urlencoded'},
                         data={'id': id})
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey or invalid product ID")


class Product:
    def __init__(self, APIKey):
        self.APIKey = str(APIKey)

    def create(self, name, description, price, productType, unlisted=False, blockProxy=False, purchaseMax='100000',
               purchaseMin='1', webhookUrl=None, serials='', stockDelimiter=','):
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
                          headers={'content-type': 'application/x-www-form-urlencoded', 'APIKey': self.APIKey},
                          data=payload)
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey or invalid parameter(s)")

    def update(self, id, name, description, price, productType, unlisted, blockProxy, purchaseMax, purchaseMin,
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
                         headers={'content-type': 'application/x-www-form-urlencoded', 'APIKey': self.APIKey}, data=payload)
        if int(r.status_code) == 200:
            return r.json()
        else:
            raise ValueError(
                f"Status code: {r.status_code} | Reason: {r.reason}: Invalid APIKey or invalid parameter(s)")

    def delete(self, id):
        requests.delete('https://autobuy.io/api/Product',
                        headers={'content-type': 'application/x-www-form-urlencoded', 'APIKey': self.APIKey},
                        data={'id': id})

    def addStock(self, id, serial):
        productJson = Get.product(self, id=id)
        # couldn't append to the original list. Used a quick solution
        p = []
        for j in productJson['serials']:
            p.append(j)
        p.append(serial)
        p = ','.join(p)
        updatedProduct = Product.update(self, id=productJson['id'], name=productJson['name'], description=productJson['description'],
                                        price=productJson['price'],
                                        productType=productJson['productType'], unlisted=productJson['unlisted'], blockProxy=productJson['blockProxy'],
                                        purchaseMax=productJson['purchaseMax'], purchaseMin=productJson['purchaseMin'],
                                        webhookUrl=productJson['webhookUrl'], stockDelimiter=productJson['stockDelimiter'], serials=p)
        return updatedProduct

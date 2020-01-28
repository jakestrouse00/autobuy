# Unofficial autobuy.io Python Wrapper
An unofficial Python wrapper for the autobuy.io API

## prerequisites
requests==2.22.0

## Installation
```cmd
python -m pip install autobuy
```
## Methods

### Get Methods

#### Get order details
Get the details of a specific order.
```python
from autobuyWrapper.autobuy import get

orderDetails = get.order(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', order='c1497823-370c-4c7a-82cd-dacddb36fc30')
```
 
 #### Get all orders
Lists orders in descending order by creation date in pages of 10.
 ```python
from autobuyWrapper.autobuy import get

orders = get.orders(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', page='1')
```

#### Get all products
This will list all your products out along with the stocked product.
```python
from autobuyWrapper.autobuy import get

allProducts = get.products(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea')
```


#### Get product details
Get a single product by ID.
```python
from autobuyWrapper.autobuy import get

allProducts = get.products(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', id='2cdbdc48-b297-41ad-a234-329db0d2dbea')
```

### Products

#### Create product
Creates a new product.

Only four arguments are required. APIKey, name, description, productType. The rest of the arguments are optional. Optional arguments with default values are: unlisted=False, blockProxy=False, purchaseMax='100000', purchaseMin='1', webhookUrl=None, serials='', stockDelimiter=','. 
```python
from autobuyWrapper.autobuy import product

# Use of product.create() with only required aurguments
newProduct = product.create(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', name='test12', description='just a test', price='9.99', productType='SerialNumber')
```


#### Update product
Updates a product by ID. This call requires all arguments to be present.

```python
from autobuyWrapper.autobuy import product

updatedProduct = product.update(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', id='2cdbdc48-b297-41ad-a234-329db0d2dbea', name='test13', description='updated description', price='8.99', productType='SerialNumber', unlisted=False, blockProxy=False, purchaseMax='100000', purchaseMin='1', webhookUrl='https://ptb.discordapp.com/api/webhooks/618938749723869205/wMjAX1okpWGuMvIScJXk2cU_r8D1qAiPty5W78vs9znoX254i1l7-8gYM4Ew_A3io0r8', serials='newAccount, newAccount2', stockDelimiter=',')
```


#### Delete product
Delete a product by ID.

```python
from autobuyWrapper.autobuy import product

product.delete(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', id='2cdbdc48-b297-41ad-a234-329db0d2dbea')
```

#### Add stock to product
Adds stock to a product. Only one item can be added per call. 
```python
from autobuyWrapper.autobuy import product

updatedProduct = product.addStock(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', id='2cdbdc48-b297-41ad-a234-329db0d2dbea', serial='email@email.com:randomPassword')
```

To add multiple items to the product's stock, loop over a list of the items.

```python
from autobuyWrapper.autobuy import product

items = ['serial1', 'serial2', 'serial3', 'serial4', 'serial5']
for item in items:
    updatedProduct = product.addStock(APIKey='2cdbdc48-b297-41ad-a234-329db0d2dbea', id='2cdbdc48-b297-41ad-a234-329db0d2dbea', serial=item)

```


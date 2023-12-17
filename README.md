# Django Product API

This is a mini Django project with a single app named "Product."

## Endpoints

### 1. List of All Products

#### Endpoint: 127.0.0.1:8000/products/

Returns a JSON array containing details of all products.


### 2. Number of the total products
Returns a JSON object with the total number of products.
#### Endpoint: 127.0.0.1:8000/products/get-status/

### 3. Detail of a Specific Product

#### Endpoint: 127.0.0.1:8000/products/get-status/{product_id}

Returns a JSON array containing details of the given product.

## Model Fields

- `title`: The title of the product.
- `quantity`: The quantity of the product.
- `created_at`: The timestamp of when the product was created.
- `updated_at`: The timestamp of when the product was last updated.


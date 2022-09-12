# wtll-challenge


# Endpoint de usuários

### Listar todos usuários

`GET /api/v1/products/`
* Response: 
```json
[
  {
    "product_url__image": "https://cdn.shopify.com/s/files/1/1602/2781/products/AllSwatches_Render-188588.jpg?v=1605714948",
    "product_url": "https://baebrow.com/products/baebrow-instant-tint-graphite",
    "product_url__created_at": "2019-06-26",
    "consult_date": "2021-02-11",
    "vendas_no_dia": 6
  },
  .
  .
  .
]
```

### Retornar um usuário especifico

`GET /api/v1/products/group/`
* Request: /api/v1/products/group/?init_date=2021-02-11&finish_date=2021-02-12
* Response:
```json
[
  {
    "product_url__image": "https://cdn.shopify.com/s/files/1/1602/2781/products/AllSwatches_Render-188588.jpg?v=1605714948",
    "product_url": "https://baebrow.com/products/baebrow-instant-tint-graphite",
    "product_url__created_at": "2019-06-26",
    "consult_date": "2021-02-11",
    "vendas_no_dia": 6
  },
  {
    "product_url__image": "https://cdn.shopify.com/s/files/1/1602/2781/products/AllSwatches_Render-188588.jpg?v=1605714948",
    "product_url": "https://baebrow.com/products/baebrow-instant-tint-graphite",
    "product_url__created_at": "2019-06-26",
    "consult_date": "2021-02-12",
    "vendas_no_dia": 10
  },
  {
    "product_url__image": "https://cdn.shopify.com/s/files/1/1602/2781/products/AllSwatches_Render-188588.jpg?v=1605714948",
    "product_url": "https://baebrow.com/products/baebrow-instant-tint-graphite",
    "product_url__created_at": "2019-06-26",
    "total_sales": 16,
    "2021-02-11": 6,
    "2021-02-12": 10
  },
  .
  .
  .
]
```

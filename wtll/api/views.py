from rest_framework.decorators import api_view
from rest_framework.response import Response
from itertools import groupby
import requests
import json


def check_in_range(start_date, end_date, current_date):
    return ((current_date >= start_date) and (current_date <= end_date))


@api_view(['GET'])
def list_products(request):
    response_api = requests.get('https://mc3nt37jj5.execute-api.sa-east-1.amazonaws.com/default/hourth_desafio')
    if request.method == 'GET':
        parse_json = json.loads(response_api.text)
        return Response(parse_json)


@api_view(['GET'])
def group_products(request):
    # init_date e finish_date
    init_date = request.query_params.get('init_date')
    finish_date = request.query_params.get('finish_date')
    print(init_date, finish_date)

    response_api = requests.get('https://mc3nt37jj5.execute-api.sa-east-1.amazonaws.com/default/hourth_desafio')
    if request.method == 'GET':
        parse_json = json.loads(response_api.text)
        struct_data = []
        for product in parse_json:
            consult_date = product['consult_date']
            if check_in_range(init_date, finish_date, consult_date):
                struct_data.append(product)

        sorted_products = sorted(struct_data, key=lambda product: product['product_url'])
        grouped_products = [list(result) for key, result in groupby(
            sorted_products, key=lambda product: product['product_url'])]

        for product_list in grouped_products:
            product_sells = map(lambda product: product['vendas_no_dia'], product_list)
            product_list.append({
                'product_url__image': product_list[0]['product_url__image'],
                'product_url': product_list[0]['product_url'],
                'product_url__created_at': product_list[0]['product_url__created_at'],
                'total_sales': sum(product_sells)})
            for product in product_list[:-1]:
                product_list[-1][product['consult_date']] = product['vendas_no_dia']
        return Response(grouped_products)

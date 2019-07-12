#!/bin/sh
python3 /code/ProductCartService.py &
envoy -c /etc/service-envoy.yaml -l debug --service-cluster envoy_product_side_car1 --service-node side_car_node

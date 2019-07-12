#!/bin/sh
python3 /code/PaymentService.py &
envoy -c /etc/service-envoy.yaml -l debug --service-cluster envoy_payment_side_car1 --service-node side_car_node

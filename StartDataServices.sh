#!/bin/sh
python3 /code/DataService.py &
envoy -c /etc/service-envoy.yaml -l debug --service-cluster envoy_data_side_car0 --service-node side_car_node

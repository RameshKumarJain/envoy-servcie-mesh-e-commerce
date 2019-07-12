#!/usr/bin/env python3
from flask import Flask
from flask import request
import os
import requests
import socket
import sys

app = Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id"
]

@app.route('/')
def healthcheck():
    return ('Success')

@app.route('/payment/add-details/<cartdata>')
def add(cartdata):
    requests.get('http://127.0.0.1:90/data/payment/add/{}'.format(cartdata))
    return ('{} added to payment successfully, resolved by host {}.\n'.format(cartdata, socket.gethostname()));

@app.route('/payment/get/')
def get():
    resp = requests.get('http://127.0.0.1:90/data/payment/get')
    return ('payment details : {}, payment amount: {}, resolved by host {}.\n'.format(resp.text, len(resp.text), socket.gethostname()));

@app.route('/payment/pay')
def pay():
    resp = requests.get('http://127.0.0.1:90/data/payment/get')
    result = 'payment details : {}, payment amount: {}.\n Paid Successfully, resolved by host {}.\n'.format(resp.text, len(resp.text), socket.gethostname())
    requests.get('http://127.0.0.1:90/data/payment/clear')
    requests.get('http://127.0.0.1:90/product/cart/clear')
    return (result);

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

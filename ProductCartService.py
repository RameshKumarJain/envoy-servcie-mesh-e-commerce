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

@app.route('/product/add/<productname>')
def addProduct(productname):
    requests.get('http://127.0.0.1:90/data/product/add/{}'.format(productname))
    return ('{} added to product list successfully, resolved by host {}.\n'.format(productname, socket.gethostname()));

@app.route('/product/get')
def getProduct():
    resp = requests.get('http://127.0.0.1:90/data/product/get')
    return ('{}, resolved by host {}.\n'.format(resp.text, socket.gethostname()));

@app.route('/product/add-to-cart/<productname>')
def addToCart(productname):
    requests.get('http://127.0.0.1:90/data/cart/add/{}'.format(productname))
    return ('{} added to cart successfully, resolved by host {}.\n'.format(productname, socket.gethostname()));

@app.route('/product/cart/get')
def getCart():
    resp = requests.get('http://127.0.0.1:90/data/cart/get')
    return ('{}, resolved by host {}.\n'.format(resp.text, socket.gethostname()));

@app.route('/product/cart/clear')
def clearCart():
    resp = requests.get('http://127.0.0.1:90/data/cart/clear')
    return ('cart cleared successfully, resolved by host {}.\n'.format(socket.gethostname()));

@app.route('/product/cart/checkout')
def checkout():
    resp = requests.get('http://127.0.0.1:90/data/cart/get')
    resp = requests.get('http://127.0.0.1:90/payment/add-details/{}'.format(resp.text))
    return ('{}\n'.format(resp.text));

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

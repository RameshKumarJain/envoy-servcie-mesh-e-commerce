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

cartData = []
paymentData = ['']
productData = []

@app.route('/')
def healthcheck():
    return ('Success')


@app.route('/data/payment/add/<paymentdata>')
def addPaymentData(paymentdata):
    paymentData[0] = paymentdata
    return ('Success');

@app.route('/data/payment/get')
def getPaymentData():
    return (paymentData[0]);

@app.route('/data/payment/clear')
def clearPayment():
    paymentData[0] = ''
    return ('Success');

@app.route('/data/product/add/<productname>')
def addProduct(productname):
    productData.append(productname)
    return ('Success');

@app.route('/data/product/get')
def getProductData():
    return ('{}'.format(productData));

@app.route('/data/cart/add/<cartdata>')
def addCartData(cartdata):
    cartData.append(cartdata)
    return ('Success');

@app.route('/data/cart/get')
def getCartData():
    return ('{}'.format(cartData));

@app.route('/data/cart/clear')
def clearCartData():
    cartData.clear()
    return ('Success');

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

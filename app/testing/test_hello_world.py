# -*- coding: utf-8 -*-
"""Some simple hello-world tests"""
from app.testing import client


def test_hello_world(client):
    rv = client.get('/')
    assert b'Hello world' in rv.data


def test_hello_dog(client):
    rv = client.get('/1')
    assert f'Hello'.encode() in rv.data


def test_hello_does_not_exist(client):
    rv = client.get('/1000000000000000000', follow_redirects=True)
    assert b'entity not found' in rv.data

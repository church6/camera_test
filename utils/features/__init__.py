"""
# @author      :  Copyright (C) Church.ZHONG
"""

__version__ = "0.0.1"
__author__ = "Church.ZHONG"
__all__ = ["DEFINED_NAMES_OF_PRODUCTS", "get_variant_feature_by_product", "get_node_by_key"]

import os
from typing import Union
from importlib import import_module
from utils.ulog import Ulog


def get_all_product_names():
    """
    Function :
    """
    # sanity check
    products = []
    dirname = os.path.dirname(__file__)
    for entry in os.scandir(dirname):
        if entry.is_dir(follow_symlinks=False):
            continue
        if entry.is_file(follow_symlinks=False) and entry.name.endswith(".py"):
            products.append(entry.name[:-3])
            continue
    return products


def get_variant_feature_by_product(ulog: Union[Ulog, None] = None):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    product_name = ulog.get_product_name()
    assert product_name is not None
    assert product_name != ""
    assert product_name in DEFINED_NAMES_OF_PRODUCTS
    return import_module(f"utils.features.{product_name}")


def get_node_by_key(ulog: Union[Ulog, None] = None, key: str = ""):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    nodes = get_variant_feature_by_product(ulog=ulog).NODES
    assert nodes is not None
    assert key in nodes, key
    return nodes[key]


DEFINED_NAMES_OF_PRODUCTS = get_all_product_names()

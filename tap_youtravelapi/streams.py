"""Stream type classes for tap-youtravelapi."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_youtravelapi.client import YoutravelApiStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ToursStream(YoutravelApiStream):
    """Define custom stream."""
    name = "tours"
    path = "/serp/tours/?currency=rub&lang=en&take=10000"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("continents", th.ArrayType(
            th.StringType
        )),
        th.Property("countries", th.ArrayType(
            th.StringType
        )),
        th.Property("highlights", th.StringType),
        th.Property("regions", th.ArrayType(
            th.StringType
        )),
        th.Property("locations", th.ArrayType(
            th.StringType
        )),
        th.Property("types", th.ArrayType(
            th.ObjectType(
                th.Property("main", th.StringType),
                th.Property("title", th.StringType),
            )
        )),
        th.Property("expert", th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("rating", th.IntegerType),
            th.Property("count_reviews", th.IntegerType),
            th.Property("avatar", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("dates", th.ObjectType(
            th.Property("total", th.IntegerType),
            th.Property("group", th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("date_from", th.IntegerType),
                th.Property("date_to", th.IntegerType),
                th.Property("guarantee", th.BooleanType),
                th.Property("price", th.NumberType),
                th.Property("prices_with_discount", th.NumberType),
                th.Property("discount_percent", th.NumberType),
                th.Property("free_spaces", th.IntegerType),
            ))
        )),
        th.Property("languages", th.ArrayType(
            th.StringType
        )),
        th.Property("is_new", th.BooleanType),
        th.Property("link", th.StringType),
        th.Property("cancellation", th.BooleanType),
        th.Property("use_custom_refund_policy", th.BooleanType),
        th.Property("is_private", th.BooleanType),
        th.Property("cashback_mir", th.BooleanType),
        th.Property("is_latest", th.BooleanType),
    ).to_dict()


class ToursRuStream(ToursStream):
    name = "tours_ru"
    path = "/serp/tours/?currency=rub&lang=ru&take=10000"
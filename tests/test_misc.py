import json
import os

import pytest

from ocdsadditions.library import Repository, init_repository


@pytest.fixture
def store(tmpdir) -> Repository:
    init_repository(tmpdir)
    repository = Repository(tmpdir)
    return repository


def test_create_then_get_ocid(store):
    store.add_ocid("OCID-1")
    store.get_contracting_process("OCID-1")
    # This test is just that it doesn't crash


def test_create_then_list_ocids(store):
    store.add_ocid("OCID-1")
    ocids = store.list_ocids()
    assert ["OCID-1"] == ocids


def test_create_then_list_extensions(store):
    store.add_ocid("OCID-1")
    extensions = store.get_contracting_process("OCID-1").get_extensions_used()
    assert [] == extensions


def test_data_release_package_with_extensions_1_get_extensions_used(store):
    source_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        "release_package_with_extensions.json",
    )

    with open(source_file) as fp:
        package_data = json.load(fp)
    release_data = package_data["releases"][0]
    del package_data["releases"]

    store.add_ocid("OCID-1")
    store.get_contracting_process("OCID-1").add_release(
        package_data, release_data, "http://www.example.com"
    )

    extensions = store.get_contracting_process("OCID-1").get_extensions_used()
    assert [
        "https://raw.githubusercontent.com/open-contracting-extensions/ocds_metrics_extension/master/extension.json"
    ] == extensions

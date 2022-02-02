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

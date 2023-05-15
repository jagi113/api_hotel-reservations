from fastapi import APIRouter

from hotel.db.interface import DBInterface
from hotel.db.models import DBCustomer
from hotel.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    create_customer,
    read_all_customers,
    read_customer,
    update_customer,
)

router = APIRouter()


@router.get("/customers")
def api_read_all_customers():
    customer_interface = DBInterface(DBCustomer)
    return read_all_customers(customer_interface)


@router.get("/customers/{customer_id}")
def api_read_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return read_customer(customer_id, customer_interface)


@router.post("/customers")
def api_create_customer(customer: CustomerCreateData):
    customer_interface = DBInterface(DBCustomer)
    return create_customer(customer, customer_interface)


@router.post("/customers/{customer_id}")
def api_update_customer(customer_id: int, data: CustomerUpdateData):
    customer_interface = DBInterface(DBCustomer)
    return update_customer(customer_id, data, customer_interface)

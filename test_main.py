"""
test_main.py

Unit tests for the Summative assessment questions in main.py
"""
import pytest
from main import (
    parse_pothole_reports,
    taxi_revenue_tracker,
    electrical_grid_status,
    grant_payment_formatter,
    logistics_chain_validator,
    deep_merge_inventories,
)

def test_parse_pothole_reports():
    raw_data = ["STREET:Bree|SEVERITY:3", "STREET:Alice|SEVERITY:8"]
    expected = {"Bree": 3, "Alice": 8}
    assert parse_pothole_reports(raw_data) == expected

def test_taxi_revenue_tracker():
    trips = [
        {"driver": "Sipho", "fare": 100},
        {"driver": "Amara", "fare": 200},
        {"driver": "Sipho", "fare": 50},
    ]
    expected = {"Sipho": 150, "Amara": 200}
    assert taxi_revenue_tracker(trips) == expected

def test_electrical_grid_status():
    suburbs = {"Gauteng": {"Soweto": "OFF", "Sandton": "ON"}, "Western Cape": {"Langa": "OFF"}}
    expected = ["Soweto", "Langa"]
    result = electrical_grid_status(suburbs)
    assert sorted(result) == sorted(expected)

def test_grant_payment_formatter():
    beneficiaries = [
        {"name": "Lerato", "amount": 1850.5, "id": "950101123456789"},
        {"name": "Thabo", "amount": 2000, "id": "920202987654321"},
    ]
    result = grant_payment_formatter(beneficiaries)
    lines = result.strip().split("\n")
    assert lines[0].startswith("ID: 950101123456789 | Name: Lerato           | Pay: R   1850.50")
    assert lines[1].startswith("ID: 920202987654321 | Name: Thabo            | Pay: R   2000.00")

def test_logistics_chain_validator():
    nodes = [100, 120, 150]
    cargo_weight = 90
    assert logistics_chain_validator(nodes, cargo_weight) is True
    nodes_fail = [100, 80, 150]
    assert logistics_chain_validator(nodes_fail, cargo_weight) is False

def test_deep_merge_inventories():
    store_a = {"Milk": 2}
    store_b = {"Milk": 3, "Bread": 1}
    expected = {"Milk": 5, "Bread": 1}
    assert deep_merge_inventories(store_a, store_b) == expected

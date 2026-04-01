
# Summative: South African Infrastructure & Logistics Simulation

**Assessment: fun-004-summative-final**

## Learning Outcomes Assessed

- **Data Integration:** Combining Strings, Lists, and Dictionaries
- **State Management:** Tracking changes across nested structures
- **Recursion:** Navigating hierarchical data
- **Robustness:** Handling edge cases and formatting output

---

## Questions

### 1. `parse_pothole_reports(raw_data: list) -> dict`

**Scenario:**
The Johannesburg Roads Agency (JRA) receives GPS strings from a mobile app, e.g.:

```
"STREET:Jan Smuts|SEVERITY:5"
```

**Goal:** Convert a list of these strings into a dictionary where the street name is the key and the severity is an integer value.

**Example:**
```python
Input:  ["STREET:Bree|SEVERITY:3", "STREET:Alice|SEVERITY:8"]
Output: {"Bree": 3, "Alice": 8}
```

**Challenge:** Split the string twice and ensure severity is an integer.

---

### 2. `taxi_revenue_tracker(trips: list) -> dict`

**Scenario:**
A taxi association in Khayelitsha tracks daily trips. Each trip is a dictionary:
```python
{"driver": "Sipho", "fare": 150, "passengers": 12}
```

**Goal:** Return a dictionary showing the total revenue earned by each driver.

**Example:**
```python
Input:  [{"driver": "Sipho", "fare": 100}, {"driver": "Amara", "fare": 200}, {"driver": "Sipho", "fare": 50}]
Output: {"Sipho": 150, "Amara": 200}
```

**Challenge:** Check if the driver already exists in your totals dictionary before adding.

---

### 3. `electrical_grid_status(suburbs: dict) -> list`

**Scenario:**
Eskom has a nested dictionary of regions:
```python
{"Gauteng": {"Soweto": "OFF", "Sandton": "ON"}, "Western Cape": {"Langa": "OFF"}}
```

**Goal:** Write a recursive function that returns a flat list of all suburb names that are currently "OFF".

**Example:**
```python
Output: ["Soweto", "Langa"]
```

**Challenge:** The function must work no matter how many levels deep the regions are nested.

---

### 4. `grant_payment_formatter(beneficiaries: list) -> str`

**Scenario:**
SASSA needs a printed payout schedule. You are given a list of dictionaries:
```python
{"name": "Lerato", "amount": 1850.5, "id": "950101..."}
```

**Goal:** Return a single string where each line is formatted as:

```
ID: [15 chars] | Name: [20 chars left-aligned] | Pay: R[10 chars right-aligned, 2 decimals]
```

**Challenge:** Use f-string alignment and padding precisely.

---

### 5. `logistics_chain_validator(nodes: list) -> bool`

**Scenario:**
A supply chain from Durban Harbor to Gauteng is valid ONLY if every "node" in the list has a capacity greater than the "weight" of the cargo.

**Goal:** Write a function that takes a `cargo_weight` and a `nodes` list (list of ints). Return `True` if all nodes can handle it, but return `False` immediately if any node fails.

**Challenge:** Efficiency—stop checking as soon as a node fails.

---

### 6. `deep_merge_inventories(store_a: dict, store_b: dict) -> dict`

**Scenario:**
Two "Spaza" shops are merging. They both have dictionaries of stock:
```python
{"Sugar": 10, "Tea": 5}
```

**Goal:** Create a new dictionary that contains all items from both. If an item exists in both, add their quantities together.

**Example:**
```python
Input:  A={"Milk": 2}, B={"Milk": 3, "Bread": 1}
Output: {"Milk": 5, "Bread": 1}
```
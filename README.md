# pyleapo

[![PyPI](https://img.shields.io/pypi/v/pyleapo?color=green)](https://pypi.org/project/pyleapo/)

An unoffical Python API for accessing your [Leap Card](https://www.leapcard.ie) balance, overview, and travel credit history. Underneath the hood, pyleapo uses [Scrapy](https://scrapy.org) to retrieve its data and therefore brings you an additional suite of options to utilise further if necessary.

## Requirements

- Python 3.5.2+

## Installation

Simply:

```python
pip install pyleapo
```

## Usage

There are three modules to choose from, the samples below showcase each of them one by one.

### 1. Card Overview

Retrieves a card's overview information such as the current balance and more.

#### Code

```python
from pyleapo.overview import get_card_overview

overview = get_card_overview(username='', password='')

print(overview)
```

#### Output

```python
{
  'auto_topup': '...',
  'card_expiry_date': '...',
  'card_issue_date': '...',
  'card_label': '...',
  'card_number': '...',
  'card_status': '...',
  'card_type': '...',
  'travel_credit_balance': '...',
  'travel_credit_status': '...'
}
```

---

### 2. Card History

Retrieves a card's travel credit history as far as it goes back.

#### Code

```python
from pyleapo.history import get_card_history

history = get_card_history(username='', password='')

print(history)
```

#### Output

```python
[
  {
    'amount': '...',
    'balance': '...',
    'date': '...',
    'source': '...',
    'time': '...',
    'transaction_type': '...'
  },
  ...
]
```

---

### 3. Card Overview and History

Retrieves both the overview and history of a card all in one.

#### Code

```python
from pyleapo.aio import get_card_overview_and_history

both = get_card_overview_and_history(username='', password='')

print(both)
```

#### Output

```python
{
  'overview': {
    'auto_topup': '...',
    'card_expiry_date': '...',
    'card_issue_date': '...',
    'card_label': '...',
    'card_number': '...',
    'card_status': '...',
    'card_type': '...',
    'travel_credit_balance': '...',
    'travel_credit_status': '...'
  },
  'events': [
    {
      'amount': '...',
      'balance': '...',
      'date': '...',
      'source': '...',
      'time': '...',
      'transaction_type': '...'
    },
    ...
  ]
}
```

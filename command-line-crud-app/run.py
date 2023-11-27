from typing import List

class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, description={self.description})"

def create_item(items: List[Item], name: str, description: str) -> Item:
    new_id = len(items) + 1
    new_item = Item(id=new_id, name=name, description=description)
    items.append(new_item)
    return new_item

def read_all_items(items: List[Item]) -> List[Item]:
    return items

def search_items(items: List[Item], filter_func) -> List[Item]:
    return [item for item in items if filter_func(item)]

def read_item_by_id(items: List[Item], item_id: int) -> Item:
    for item in items:
        if item.id == item_id:
            return item
    raise ValueError(f"Item with id {item_id} not found")

def update_item(items: List[Item], item_id: int, name: str, description: str) -> Item:
    for item in items:
        if item.id == item_id:
            item.name = name
            item.description = description
            return item
    raise ValueError(f"Item with id {item_id} not found")

def delete_item(items: List[Item], item_id: int) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return
    raise ValueError(f"Item with id {item_id} not found")

#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = "DJJD2150, Ybrayym Abamov"


class Node:
    def __init__(self, key, value=None):
        """This dunder function defines the keys and values and hashes them."""
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """This puts them into readable string format."""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """This compares for potential duplicates."""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """Creates a new instance of NoDict."""
        self.buckets = []
        self.size = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                          for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Adds an additional key/ value pair to NoDict and
        checks for potential duplicates."""
        new_node = Node(key, value)
        random_bucket = new_node.hash % self.size
        for node in enumerate(self.buckets[random_bucket]):
            if new_node == node[1]:
                del self.buckets[random_bucket][node[0]]
        self.buckets[random_bucket].append(new_node)

    def get(self, key):
        """Gets a key/ value pair from NoDict and checks if it exists."""
        value = None
        node_to_find = Node(key)
        random_bucket = node_to_find.hash % self.size
        for node in self.buckets[random_bucket]:
            if node_to_find == node:
                value = node.value
        if value is None:
            raise KeyError(f'{key} not found')
        return value

    def __getitem__(self, key):
        """Enables the square bracket reading behavior."""
        value = self.get(key)
        if value is None:
            raise KeyError(f'{key} not found')
        return value

    def __setitem__(self, key, value):
        """Enables the square bracket assignment behavior."""
        return self.add(key, value)

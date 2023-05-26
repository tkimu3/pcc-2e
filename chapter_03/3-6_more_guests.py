#!/usr/local/bin/python3
guests = ['Shohei Ohtani', 'Brad Pitt', 'Steve Jobs']

for guest in guests:
    msg = f"Dear {guest.title()},\nIt is my pleasure to invite you to the Dinner at my new house\n"
    print(msg)

print(f"\nI found that {guests[-1].title()} can't make the dinner\n")

guests[-1] = 'Bill Gates'

for guest in guests:
    msg = f"Dear {guest.title()},\nIt is my pleasure to invite you to the Dinner at my new house\n"
    print(msg)

print(f"\nI found that the dinner table is bigger than expected, so I can invite more people to the dinner\n")


guests.insert(0, 'Joe Biden')
position = int(len(guests)/2)
guests.insert(position, 'Vladimir Putin')
guests.append('Fumio Kishida')

for guest in guests:
    msg = f"Dear {guest.title()},\nIt is my pleasure to invite you to the Dinner at my new house\n"
    print(msg)
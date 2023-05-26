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

print(f"\nI found that the dinner table won't arrive in time the dinner, so I can only invite two guests to the dinner\n")

while len(guests) > 3:
    guest = guests.pop()
    msg = f"Dear {guest.title()},\nI'm sorry that I can't invite you to the Dinner this time\n"
    print(msg)

for guest in guests:
    msg = f"Dear {guest.title()},\nIt is my pleasure to invite you to the Dinner at my new house\n"
    print(msg)

del guests[:]

print(f"\nI'll make sure of the guest list is empty")
print(guests)
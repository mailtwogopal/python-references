# dictionary stores key value pairs
# dictionary can contain array (marks below), another dictionary (rank below)
record = {'id': 1, "marks": [45, 65, 82, 51, 63], "rank": {"quarterly": 1, "half-yearly": 2, "final": 1}}
print(record)
print(record['marks'])
print(record['rank'])

print("marks" in record) # returns true
print("Marks" in record) # returns false since it is case sensitive


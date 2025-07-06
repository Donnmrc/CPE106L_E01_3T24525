from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["chinook"]
customers = db["customers"]

# Print header
print(f"{'CustomerId':<12} {'FirstName':<15} {'LastName':<15} {'Company':<30} {'Address'}")
print("-" * 90)

# Print each customer
for c in customers.find({}, {"_id": 0, "CustomerId": 1, "FirstName": 1, "LastName": 1, "Company": 1, "Address": 1}):
    print(f"{c.get('CustomerId', ''):<12} {c.get('FirstName', ''):<15} {c.get('LastName', ''):<15} {str(c.get('Company', '')):<30} {c.get('Address', '')}")

client.close()

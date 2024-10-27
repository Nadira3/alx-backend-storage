#!/usr/bin/env python3
""" module that contains database script """


def main():
    """ main function housing the script logic """
    from pymongo import MongoClient

    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Print the total count of logs
    print(f"{collection.count_documents({})} logs")

    # Count the number of each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({"path": "/status"})
    print(f"{status_count} status check")

    # Aggregation pipeline to count occurrences of each IP
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}  # Sort by count in descending order
    ]

    results = collection.aggregate(pipeline)
    print("IPs:")
    counter = 0
    for result in results:
        if counter == 10:
            break
        print(f"\t{result['_id']}: {result['count']}")
        counter += 1


if __name__ == "__main__":
    main()

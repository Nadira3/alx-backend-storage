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


if __name__ == "__main__":
    main()

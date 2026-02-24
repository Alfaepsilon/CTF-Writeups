#Since the flag has simpy been base 64 encoded and then hexxed, we can reverse these operations to get the flag.
echo 53465243657a51784d56383361444e664d32356a4d475178626a6c664e44497a5832677a4d6a4e664e7a42664e5463306558303d | xxd -r -p |  base64 -d

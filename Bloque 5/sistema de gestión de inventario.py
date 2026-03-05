def save_to_db(item: dict, message: str):
    print(f"[DB] {item['name']} (ID: {item['id']}): {message}")
def p_inv(items, d_type):
    # Check if items exists
    if items is not None:
        if len(items) > 0:
            for i in range(len(items)):
                # Calculate discount
                if d_type == "SUMMER":
                    items[i]['price'] = items[i]['price'] * 0.8
                    print("Updating item: " + str(items[i]['id']))
                    save_to_db(items[i], "Applied Summer Discount")
                elif d_type == "WINTER":
                    items[i]['price'] = items[i]['price'] * 0.7
                    print("Updating item: " + str(items[i]['id']))
                    save_to_db(items[i], "Applied Winter Discount")
                elif d_type == "FLASH":
                    items[i]['price'] = items[i]['price'] * 0.5
                    print("Updating item: " + str(items[i]['id']))
                    save_to_db(items[i], "Applied Flash Discount")
        else:
            print("No items")
    else:
        print("Error: List is null")
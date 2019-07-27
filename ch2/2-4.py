def add_to_cart(conn, session, item, count):
    if count <= 0: 
        conn.hrem('cart:' + session, item)
    else: 
        conn.hset('cart:' + session, item, count)
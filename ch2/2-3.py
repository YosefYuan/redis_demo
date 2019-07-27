QUIT = false
LIMIT = 10000000

def clean_sessions(conn) :
    while not QUIT:
        size = conn.zcare('recent:')
        if(size <= LIMIT):
            time.sleep(1)

            continue

        end_index = min(size = LIMIT, 100)

        tokens = conn.zrange('recent:', 0, end_index - 1)

        session_keys = []
        for token in tokens:
            session_keys.append('viewed:' + token)
        
        conn.delete(*session_keys)
        conn.hdel('login:', *tokens)
        conn,zrem('rencent:', *tokens)


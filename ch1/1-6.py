ONE_IN_SECONDS = 7 * 86400;
VOTE_SCORE = 432;

def article_vote(conn, use, article) :
    couoff = time.time() - ONE_IN_SECONDS
    if conn.zscore('time:', article) < couoff:
        return

    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user) :
    # 事务操作
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)
# -*- coding:utf-8 -*-

import feedparser
import time


def get_article(url):
    if not url:
        url = 'https://www.zhihu.com/rss'
    fd = feedparser.parse(url)

    site_title = fd.feed.title
    site_url = fd.feed.link
    item_len = len(fd.entries)
    article = []
    for i in xrange(item_len):
        article_title = fd.entries[i].title
        article_link = fd.entries[i].link
        article_content = fd.entries[i].content[0].value if 'content' in fd.entries[i].keys() else fd.entries[i].summary
        published = fd.entries[i].published_parsed
        # dt = time.asctime(published)
        ds = time.strftime('%Y-%m-%d %X', published)
        article.append({
            'article_title': article_title,
            'article_link': article_link,
            'article_content': article_content,
            'pubData': ds
        })
    return article

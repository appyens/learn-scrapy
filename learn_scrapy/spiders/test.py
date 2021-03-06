import itertools


def crawl_site(url, max_errors=5):

    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = 1

        if html is None:
            num_errors += 1

            if num_errors == max_errors:
                # max errors reached, exit loop
                break
            else:
                num_errors = 0
                # success - can scrape the result
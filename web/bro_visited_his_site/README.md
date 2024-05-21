# bro_visited_his_site

## part 1

bro stored his secrets in the flask app config

hint: SSTI
explicit hint: https://ctftime.org/writeup/10895

## part 2

ok, but can you get /app/flag.txt

explicit hint: https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection/jinja2-ssti

# notes

this is still vulnerable to people fucking with it since it's rce but hopefully having the app directory non-writable is enough
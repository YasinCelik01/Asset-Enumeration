# Add at the end of the command in order to block
# standard output to print anything
STDOUT_DISABLE = ' >/dev/null 2>&1 ' 

subfinder_command = "subfinder -d {DOMAIN}"
# subfinder_command = "subfinder -d {DOMAIN} -ip -active"

# Depth of the endpoints
SPIDER_DEPTH = 1

dig_dns = "dig +yaml {domain}"
dig_rev_dns = "dig +yaml -x {ip}"

SHODAN_API_KEY = "" #'UXFGk1nriNYhnGVLXsyRBrhEBKXMONzr'

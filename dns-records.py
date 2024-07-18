import subprocess
import yaml
import json

from config import dig_dns, dig_rev_dns

def dig(domain: str = None, ip: str = None):
    if not domain and not ip:
        raise Exception('Error: provide domain or IP')
    
    # dns lookup
    if domain:
        cmd_output = subprocess.check_output(dig_dns.format(domain=domain), shell=True)
    
    # reverse dns lookup
    elif ip:
        # not implemented yet
        cmd_output = subprocess.check_output(dig_rev_dns.format(ip=ip), shell=True)

    lst = yaml.unsafe_load(cmd_output)

    return lst[0]['message']['response_message_data']

    
if __name__=='__main__':
    a = (dig('acunn.com'))

import subprocess

def check_ip_addr(addr_lst): 
    results = []
    for addr in addr_lst: 
        
        status, _ = subprocess.getstatusoutput(f'ping /n 1 {addr}')                     
        if status == 0: 
            results.append('yes')
        else: 
            results.append('no')
    return results

n = check_ip_addr(input('Please enter IP addresses separated by commas: ').split(','))

print(n)
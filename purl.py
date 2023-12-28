import argparse
from urllib.parse import urlparse, urlsplit
import http.client

def process_request(request_type, host, url, verbose=False):
    
    # establish connection
    conn = http.client.HTTPConnection(host=host)

    if request_type == "GET":
        
        conn.request(request_type, url=url, headers={"Host": host, "Connection": 'close'})
        response = conn.getresponse()

        if verbose:
            print(f"< {response.status, response.reason}")
            print(f"< {response.msg}")
        
        # print response
        print(f"{response.read().decode('ASCII')}")

def parse_command(args):
    # print("URL: ", args.url)
    # parse url
    parsed_url = urlparse(url=args.url)

    if args.verbose:
        # request type
        verbose_message = "> " + "GET" #args.request_type if args.request_type else "GET"
        verbose_message += " "

        # url path to process
        verbose_message += parsed_url.path
        verbose_message += " "

        # protocol
        verbose_message += parsed_url.scheme.upper()
        print(verbose_message)
        print("> Host:", parsed_url.netloc.split(':')[0])
        print("> User-Agent: purl")
        print(">")
    
    process_request("GET", host= parsed_url.netloc.split(':')[0], url=parsed_url.path, verbose=args.verbose)
    print("----")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="purl", description="curl in python")
    
    parser.add_argument('url', action='store')
    parser.add_argument('-v', '--verbose', action='store_const', const=1, help='display verbose response')
    # parser.add_argument('-x', '--request_type', action='store', default='GET', help='request type to be made')
    
    args = parser.parse_args()

    parse_command(args)

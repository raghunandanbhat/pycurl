import argparse
from urllib.parse import urlparse, urlsplit
import http.client
import sys

def process_request(request_type, host, url, outfile, verbose=False):
    
    # establish connection
    conn = http.client.HTTPConnection(host=host)
        
    conn.request(request_type, url=url, headers={"Host": host, "Connection": 'close'})
    response = conn.getresponse()

    if verbose:
        print(f"< {response.status, response.reason}", file=outfile)
        for k, v in response.msg.items():
            print(f"< {k}: {v}", file=outfile)
        print("", file=outfile)
    
    # print response
    print(f"{response.read().decode('ASCII')}", file=outfile)

def parse_command(args):
    # print("URL: ", args.url)
    # parse url
    # args.url[0] empty might cause error - handle error --- todo
    parsed_url = urlparse(url=args.url[0])

    if args.verbose:
        # request type
        verbose_message = "> " + args.request_type
        verbose_message += " "

        # url path to process
        verbose_message += parsed_url.path
        verbose_message += " "

        # protocol
        verbose_message += parsed_url.scheme.upper()

        print(verbose_message, file=args.output_file)
        print(f"> Host: {parsed_url.netloc.split(':')[0]}", file=args.output_file)
        print("> User-Agent: purl\n>\n", file=args.output_file)
    
    process_request(args.request_type, host= parsed_url.netloc.split(':')[0], url=parsed_url.path, outfile=args.output_file, verbose=args.verbose, )
    print("---Done---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="purl", description="curl in python")
    
    parser.add_argument('url', nargs=argparse.REMAINDER, action='store')
    parser.add_argument('-v', '--verbose', action='store_true', help='display verbose response')
    parser.add_argument('-x', '--request_type', action='store', default='GET', help='request type to be made, default request type is GET')
    parser.add_argument('-o', '--output_file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="write output to a file; writes to system out by default")
    
    args = parser.parse_args()

    parse_command(args)

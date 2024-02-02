import sys
import argparse
import http.client
from urllib.parse import urlsplit
from exceptions import URLRequired

def process_request(request_type, host, path, args):
    """
    Prepare headers to be sent over the request and make a HTTPConnection object
    Then send HTTP request and receive a response. Format the response according
    to options.
    """
    headers = {"Host": host, "Connection": 'close'}
    if args.headers:
        for header in args.headers:
            hdr, value = header.split(':')
            headers[hdr] = value
    conn = http.client.HTTPConnection(host=host)
    conn.request(method=request_type, url=path, body=args.data, headers=headers)
    response = conn.getresponse()
    return response

def make_request(args):
    try:
        # args.url[0] empty might cause error - handle error --- todo
        if not args.url:
            raise URLRequired("A valid URL is required to make a request.")
        
        parsed_url = urlsplit(url=args.url[0])

        if args.verbose:
            verbose_message = f"> {args.request_type} {parsed_url.path} {parsed_url.scheme.upper()}"
            print(verbose_message, file=args.output_file)
            print(f"> Host: {parsed_url.netloc.split(':')[0]}", file=args.output_file)
            print("> User-Agent: purl\n>\n", file=args.output_file)
        
        response = process_request(args.request_type, 
                                    host= parsed_url.netloc, 
                                    path=parsed_url.path, 
                                    args=args)
        
        if args.verbose:
            print(f"< {response.status, response.reason}", file=args.output_file)
            for k, v in response.msg.items():
                print(f"< {k}: {v}", file=args.output_file)
            print("", file=args.output_file)
        print(f"{response.read().decode('ASCII')}", file=args.output_file)

    except URLRequired as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog="purl", description="curl in python")
    parser.add_argument('url', nargs=argparse.REMAINDER, action='store')
    parser.add_argument('-v', '--verbose', action='store_true', help='display verbose response')
    parser.add_argument('-x', '--request_type', action='store', default='GET', help='request type to be made, default request type is GET')
    parser.add_argument('-o', '--output_file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="write output to a file; writes to system out by default")
    parser.add_argument('-H', '--headers', action='append', help='headers for request')
    parser.add_argument('-d', '--data', action='store', help='data to send in request')
    args = parser.parse_args()

    make_request(args)
    
if __name__ == "__main__":
    main()
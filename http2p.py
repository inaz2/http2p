import sys
import urllib2
import readline
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from threading import Thread


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Connection', 'close')
        self.end_headers()
        print >>self.wfile, self.path

    def log_message(self, format, *args):
        pass


def serve(port, HandlerClass=RequestHandler, ServerClass=HTTPServer):
    server_address = ('', port)

    HandlerClass.protocol_version = 'HTTP/1.1'
    httpd = ServerClass(server_address, HandlerClass)

    # sa = httpd.socket.getsockname()
    # print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


def handle_client():
    while True:
        url = raw_input('> ')
        if url:
            f = urllib2.urlopen(url)
            print f.read()
            f.close()


if __name__ == '__main__':
    port = int(sys.argv[1])

    t = Thread(target=serve, args=(port,))
    t.daemon = True
    t.start()

    handle_client()

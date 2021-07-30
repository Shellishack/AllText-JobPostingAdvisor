from http.server import HTTPServer, BaseHTTPRequestHandler
from consume import get_result_bias,get_result_group
import json
from io import BytesIO

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        self.wfile.write(get_result("abc").encode())
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers','X-Requested-With, Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path.endswith('/getbias'):
            self.send_response(200)
            self.send_header('content-type','application/json')
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            body=self.rfile.read(int(self.headers['Content-Length']))

            input=json.loads(body)['data'][0]['jobrequirements']

            
            # print(type(get_result_bias(input)))
            self.wfile.write(get_result_bias(input))
        if self.path.endswith('/getgroup'):
            self.send_response(200)
            self.send_header('content-type','application/json')
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()

            body=self.rfile.read(int(self.headers['Content-Length']))

            input=json.loads(body)['data'][0]['jobrequirements']

            
            # print(type(get_result_group(input)))
            self.wfile.write(get_result_group(input))
def main():
    port=8000
    server=HTTPServer(('',port),APIHandler)
    
    server.serve_forever()

if __name__=='__main__':
    main()
# coco

tshark command for viewing http request
tshark -Y "http.request.method == \"GET\" or http.request.method == \"POST\"" -T fields -e ip.src -e http.request.method -e http.request.full_uri -e http.file_data -f "tcp port 80"
ref: https://stackoverflow.com/questions/45467118/tshark-filtering-http-https-get-request

for tcpdump
ref: https://sites.google.com/site/jimmyxu101/testing/use-tcpdump-to-monitor-http-traffic



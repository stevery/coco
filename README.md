# coco

tshark command for viewing http request
tshark -Y "http.request.method == \"GET\" or http.request.method == \"POST\"" -T fields -e ip.src -e http.request.method -e http.request.full_uri -e http.file_data -f "tcp port 80"

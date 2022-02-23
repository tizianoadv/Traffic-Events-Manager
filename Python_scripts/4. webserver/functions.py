def create_html_template(event_info):
    start = "<!DOCTYPE html><html><head><title>Traffic Events - ZONE : University of Reims</title></head><body>"
    end = "</body></html>"
    file = open("/home/webserver/traffic_app/templates/index.html","a")
    html = event_info + "\n"
    file.write(html)
    file.close()

def erase_html_template():
    file0 = open("/home/webserver/traffic_app/templates/index.html","w")
    html_null = ""
    file0.write(html_null)
    file0.close()
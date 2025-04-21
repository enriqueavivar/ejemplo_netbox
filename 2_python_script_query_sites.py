import requests
import sys

url = "http://localhost:8001/api/dcim/sites/"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 58bd1eb7e4be340fc03858e0796140181e69cb63',
  #'Cookie': 'csrftoken=lWefNayN2tsasHz2AwpP4skzQnyeSiTK'
}

def get_sites(status=None):
    params={}
    if status:
        params['status'] = status
    else:
        print("No status provided, fetching all sites.")
        
    try:
        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        if response.status_code == 200:
            sites = response.json()['results']
            if sites:
                if status:
                    print(f"Sites with status '{status}':")
                for site in sites:
                    print(f"Site Name: {site['name']}, Status: {site['status']}")
            else:
                print("No sites found.")
        else:
            print(f"Error querying the NetBox API: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {e}")

#Check if the parameter exists. If not, makes an empty call
if len(sys.argv) > 1:
    status = sys.argv[1]
    get_sites(status)
else:
    get_sites()
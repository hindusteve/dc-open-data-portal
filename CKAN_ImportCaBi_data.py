import requests
requests.post('http://data.codefordc.org/api/action/resource_create',
              data={"package_id":"95bc730e-cd2b-49e9-a874-5e022524c24a", "type": "file.upload", "url": "anything", "name": "2015 Q1", "format": "csv"},
              headers={"X-CKAN-API-Key": "352a04ff-d465-49b2-9b94-0dc95ea692ec"},
              files=[('upload', file('2015-Q1-Trips-History-Data.csv'))]
              )
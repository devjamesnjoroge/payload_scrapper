import urllib.request, json

def get_items():

    base_url = 'https://gaming.betsafe.co.ke/images/gaming.betsafe.co.ke/manifest.json'

    with urllib.request.urlopen(base_url) as url:
         get_sources_data = url.read()
         get_sources_response = json.loads(get_sources_data)

         print(get_sources_response)

         sources_results = None

         if get_sources_response:
            sources_results = get_sources_response['name'], get_sources_response['icons']

    return sources_results

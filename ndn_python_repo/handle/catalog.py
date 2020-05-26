from ndn.types import *
from ndn.app import NDNApp
from ndn.encoding import Name

app = NDNApp()

@app.route('/217B_Repo/catalog')
def on_interest(name, interest_param, application_param):
    print(f'Received Interest Name: {Name.to_str(name)}')
    app.put_data(name, content=b'zixuan', freshness_period=10000)

async def main():
    pass

app.run_forever(after_start=main())

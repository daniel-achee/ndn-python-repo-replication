

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import asyncio


from ndn.app import NDNApp
from catalog_commands import CatalogCommandClient



app=NDNApp()


async def test1 ():

    catalogComClient= CatalogCommandClient(app,"/217B_Repo/catalog")
    await catalogComClient.add("/foobar/1.txt","087234ab")

asyncio.run(test1())

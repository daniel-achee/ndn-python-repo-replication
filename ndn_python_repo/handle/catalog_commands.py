# -----------------------------------------------------------------------------
# NDN Repo putfile client.
#
# @Author jonnykong@cs.ucla.edu
#         susmit@cs.colostate.edu
# @Date   2019-10-18
# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import asyncio as aio
import logging
import multiprocessing
from ndn.app import NDNApp
from ndn.encoding import Name, NonStrictName, Component, DecodeError
from ndn.types import InterestNack, InterestTimeout,InterestCanceled,ValidationFailure
from ndn.security import KeychainDigest
from ndn.utils import gen_nonce
import os
import platform
from typing import List


class CatalogCommandClient():

    def __init__(self, app: NDNApp,catalog_prefix: str):
        self.app = app
        self.catalog_prefix=catalog_prefix


    async def add(self, data_name :str,hash : str, desired_copies : int=3 ):

        try:
            sql_command="INSERT INTO data (data_name, hash, desired_copies) VALUES ({0}, {1}, {2});".format(data_name,hash,desired_copies)
            name=self.catalog_prefix+"/"+sql_command+"/"+str(gen_nonce())
            data_name, meta_info, content= await self.app.express_interest(name, must_be_fresh=True, can_be_prefix=False, lifetime=1000)
            print(f'Received Data Name: {Name.to_str(data_name)}')
            print(meta_info)
            print(bytes(content) if content else None)
        except InterestNack as e:
            # A NACK is received
            print(f'Nacked with reason={e.reason}')
        except InterestTimeout:
            # Interest times out
            print(f'Timeout')
        except InterestCanceled:
            # Connection to NFD is broken
            print(f'Canceled')
        except ValidationFailure:
            # Validation failure
            print(f'Data failed to validate')
        finally:
            self.app.shutdown()

# import sys
# sys.path.append("..")
import os
from concurrent import futures
import logging
from os import environ
from typing import Callable, List, Tuple
# import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import grpc
import redis
from app.grpc.src.client_pb2_grpc import add_ClientServicer_to_server
from app.grpc.src.favorite_product_pb2_grpc import add_FavoriteProductServicer_to_server
from app.modules.client.infra.server import ClientServer
from app.modules.client.infra.db.client_model import begin_transaction as client_begin_transaction
from app.modules.favorite_product.infra.db.favorite_product_model import begin_transaction as favorite_product_begin_transaction
from app.modules.favorite_product.infra.server import FavoriteProductServer


db_url = os.environ['DATABASE_URL']


ServicerTuple = Tuple[Callable, object]


class Server:

    TIMEOUT: int = 30

    def __init__(self, port='5021', max_workers=10):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.logger.info('Starting service')
        
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        self.port = port

    def servicers_registrations(self, servicers: List[ServicerTuple]):
        for funcs, protobufs in servicers:
            funcs.__call__(protobufs, self.server)

    def start(self):
        self.server.add_insecure_port('[::]:5021')
        self.server.start()
        self.servicers_registrations([
            (add_FavoriteProductServicer_to_server, FavoriteProductServer()),
            (add_ClientServicer_to_server, ClientServer()),
        ])
        
        try:
            self.logger.info(' -----------> Server running on {}'.format(self.port))
            self.server.wait_for_termination()
        except KeyboardInterrupt:
            logging.info('Stopping server')
            self.server.stop(self.TIMEOUT).wait()
            self.logger.info('Server execution terminated')


def init():
    if __name__ == '__main__':
        logging.basicConfig()
        client_begin_transaction()
        favorite_product_begin_transaction()
       
        # redis.Redis(host='localhost', port=6379, decode_responses=True)

        s = Server()
        s.start()
        
init()
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

from app.grpc.src.auth_pb2_grpc import add_AuthServicer_to_server
from app.modules.auth.infra.server import AuthServer
from app.grpc.src.otp_pb2_grpc import add_OTPServicer_to_server
from app.modules.otp.infra.server import OTPServer
# from sqlalchemy.ext.declarative import declarative_base
# from app.database.orm_config.declarative_base import Base
from app.modules.auth.infra.db.auth_model import begin_auth_transaction
from app.modules.otp.infra.db.otp_model import begin_transaction

# engine = db.create_engine('sqlite://service_client_db.db', echo=True)


db_url = os.environ['DATABASE_URL']


ServicerTuple = Tuple[Callable, object]


class Server:

    TIMEOUT: int = 30
    # db_url = os.environ['DATABASE_URL']
    
    # def get_connection():
    #     return create_engine(
    #         url=self.db_url
    #         )

    def __init__(self, port='5022', max_workers=10):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.logger.info('Starting service')
        
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        self.port = port

    def servicers_registrations(self, servicers: List[ServicerTuple]):
        for funcs, protobufs in servicers:
            funcs.__call__(protobufs, self.server)

    def start(self):
        self.server.add_insecure_port('[::]:5022')
        self.server.start()
        self.servicers_registrations([
            (add_AuthServicer_to_server, AuthServer()),
            (add_OTPServicer_to_server, OTPServer())
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
        begin_auth_transaction()
        begin_transaction()
        logging.basicConfig()
        print('[][][][][][][]')
        logging.info('TESTE')
        s = Server()
        s.start()
        # # init_db()
        print('hello word')
        
init()
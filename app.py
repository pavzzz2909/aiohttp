from support.imports import *



app = web.Application()
Base.metadata.create_all(BaseService.engine)



if __name__ == '__main__':
    web.run_app(app)

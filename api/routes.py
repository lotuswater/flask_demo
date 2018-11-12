from api.handlers.hello_world import HelloWorld


# 配置API 路由
def register_routes(api):
    api.add_resource(HelloWorld, '/')

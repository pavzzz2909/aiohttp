from support.imports import *

from app import app
from validator import validate
from models import User, Ad
from schema import USER_CREATE, ADVERTISEMENT_CREATE


class UserView(web.View):

    async def get(self, user_id):
        await user = User.get_by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    async def post(self):
        user = User(**request.json)
        await user.set_password(request.json['password'])
        await user.add()
        return jsonify(user.to_dict())

    async def delete(self, user_id):
        await User.delete_by_id(user_id)
        return jsonify({'message': 'NO_CONTENT'})


class AdvertisementView(web.View):

    async def get(self, advertisement_id):
        instance = await Ad.get_by_id(advertisement_id)
        return jsonify(instance.to_dict())

    @validate('json', ADVERTISEMENT_CREATE)
    async def post(self):
        instance = await Ad(**request.json)
        await instance.add()
        return jsonify(instance.to_dict())

    async def delete(self, advertisement_id):
        await Ad.delete_by_id(advertisement_id)
        return jsonify({'message': 'NO_CONTENT'})




app.router.add_route('GET','/users/{user_id:\d+}',UserView)
app.router.add_route('POST','/users/',UserView)
app.router.add_route('DELETE','/users/{user_id:\d+}',UserView)
app.router.add_route('GET','/advertisements/{advertisement_id:\d+}',AdvertisementView)
app.router.add_route('POST','/advertisements/',AdvertisementView)
app.router.add_route('DELETE','/advertisements/{advertisement_id:\d+}',AdvertisementView)

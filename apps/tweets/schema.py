from rest_framework.schemas.openapi import AutoSchema


class BaseAutoSchema(AutoSchema):
    base_name = ""

    def get_operation_id_base(self, path, method, action):
        if action == "list" and not self.base_name.endswith("s"):
            self.base_name += "s"
        return self.base_name


class UserTweetsSchema(BaseAutoSchema):
    base_name = "UserTweet"

    def get_tags(self, path, method):
        return ["tweets", "users"]

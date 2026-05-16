from litellm.integrations.custom_logger import CustomLogger

class RemoveNameHook(CustomLogger):
    async def async_pre_call_hook(self, user_api_key_dict, cache_hit, data, call_type):
        if isinstance(data, dict) and "messages" in data:
            for msg in data["messages"]:
                if isinstance(msg, dict):
                    msg.pop("name", None)
        return data

remove_name_hook = RemoveNameHook()

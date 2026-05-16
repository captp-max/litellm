from litellm.integrations.custom_logger import CustomLogger

class RemoveNameHook(CustomLogger):
    async def async_pre_call_hook(self, user_api_key_dict, cache_hit, data, call_type):
        """Supprime tous les champs 'name' des messages"""
        if isinstance(data, dict) and "messages" in data and isinstance(data["messages"], list):
            for message in data["messages"]:
                if isinstance(message, dict):
                    message.pop("name", None)  # Supprime si présent
        return data

# Instance à utiliser dans le config
remove_name_hook = RemoveNameHook()

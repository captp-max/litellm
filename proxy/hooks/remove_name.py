from litellm.integrations.custom_logger import CustomLogger

class RemoveNameHook(CustomLogger):
    def async_pre_call_hook(self, user_api_key_dict, cache_hit, data, call_type):
        """Supprime le champ 'name' de tous les messages avant envoi"""
        if isinstance(data, dict) and "messages" in data:
            for message in data["messages"]:
                if isinstance(message, dict) and "name" in message:
                    message.pop("name", None)   # supprime proprement
        return data

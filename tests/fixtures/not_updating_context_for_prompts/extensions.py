from krupy_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        return {"success": True}

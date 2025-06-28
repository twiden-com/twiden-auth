
class DBTransaction:
    def __init__(self):
        self.rollbacks = []
    
    def add_rollback(self, func, *args):
        self.rollbacks.append((func, args))
    
    async def perform_rollbacks(self):
        for func, args in reversed(self.rollbacks):
            try:
                if hasattr(func, '__call__'):
                    await func(*args)
            except Exception as e:
                print(f"Rollback failed: {e}")
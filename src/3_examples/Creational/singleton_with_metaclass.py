
# Implement Singleton using Metaclass
# ------------------------------------
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()

# Both reffer to same object.
# ----------------------------
print(logger1, logger2)

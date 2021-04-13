def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('failed to open database') from exc
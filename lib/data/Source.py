from lib import Service

class Source(Service):
  def __init__(self, thread, id, root):
    super().__init__(thread, id, root)
    self._logger.add_field('service', 'Feed')
    self._logger.add_field('vname', self.__class__.__name__)
  
  def item(self, val = None):
    return {
      'source': self._id,
      'steps': {},
      'data': val
    }

  def next(self, count=10, block=False):
    if self._running or not self._data.count() == 0:
      return self._data.get(count=count, block=block)
    elif self._data.count() == 0:
      raise Exception("Storage is empty, generator is stopped")

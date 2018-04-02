from queue import LifoQueue
from time import sleep

import itertools

from lib.net import Remote
from lib import Service


class Feed(Service):
  def __init__(self, thread, id, root):
    super().__init__(thread, id, root)
    self._logger.add_field('service', 'Feed')
    self._logger.add_field('vname', self.__class__.__name__)

  def get(self, plugin, count=1, timeout=3):
    items = self._data.get(count)
    self._logger.debug("get %s OF %s", len(items), count)
    return items

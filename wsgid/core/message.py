#encoding: utf-8


class Message(object):
  '''
    Represents a mongrel2 raw message
  '''

  def __init__(self, m2message):
    self.server_id, self.client_id,\
        self.path, self.netstring = m2message.split(' ', 3)

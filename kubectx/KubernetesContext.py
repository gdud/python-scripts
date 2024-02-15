class KubernetesContext:
  def __init__(self, name, is_current=False):
    self.name = name
    self.is_current = is_current
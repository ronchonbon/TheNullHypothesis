init -1:

    default HumHumPool = HumHumPoolClass()
            
init -2 python:

    class HumHumClass(object):
        def __init__(self, Owner, body):
            self.Owner = Owner

            self.body = body

    class HumHumThreadClass(object):
        def __init__(self, name, HumHums = None):
            if not HumHums:
                HumHums = []
                
            self.name = name

            self.HumHums = HumHums

        def update(self, H):
            for other_H in self.HumHums:
                if other_H.body == H.body:
                    return

            self.HumHums.append(H)

            return

        def remove(self, H):
            if H.name in self.HumHums.keys():
                del self.HumHums[H.name]

            return

    class HumHumPoolClass(object):
        def __init__(self):
            self.HumHumThreads = {}

        def update(self, H):
            self.HumHumThreads[H.name] = H

            return

        def remove(self, H):
            if H.name in self.HumHumThreads.keys():
                del self.HumHumThreads[H.name]
                
            return
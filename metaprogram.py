from datetime import datetime, timedelta


class A(object):
    valid_for = 10  # key is valid only 10 seconds

    def __init__(self):
        self.key_date = None

    def _check(self):
        # check old key
        if not self.key_date or \
                self.key_date < (datetime.now() - timedelta(seconds=self.valid_for)):
            print 'update key'
            self.key_date = datetime.now()

    def __getattribute__(self, name):
        target = super(A, self).__getattribute__(name)
        if name != '_check' and callable(target):
            self._check()
        return target

    def m1(self):
        print 'm1 call'

    def m2(self):
        print 'm2 call'

    def m3(self):
        print 'm3 call'

    def m4(self):
        print 'm4 call'


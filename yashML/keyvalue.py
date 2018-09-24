import sqlite3
import json
from collections import UserDict

try:
    from cPickle import Pickler, Unpickler
except ImportError:
    from pickle import Pickler, Unpickler

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from UserDict import DictMixin
except ImportError:
    from collections import MutableMapping as DictMixin

class sqlite3keyvaluestore(DictMixin):

    def __init__(self, filenameandpath, tablename='ApplicationConfiguration', serialisationtype='json'):
        """filenameandpath - the name and path to the file
        tablename - the name of the table to create (or use) in the database (this allows the file to be used for other purposes with control over potential name clashes
        serialisationtype - either 'json' or 'pickle', defaults to 'json' - the method used to serialise the value in the database"""
        self.con = sqlite3.connect(filenameandpath)
        self.cur = self.con.cursor()
        self.filenameandpath = filenameandpath
        self.serialisationtype = serialisationtype
        self.tablename = tablename
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='%s';" % self.tablename
        self.cur.execute(query)
        if not self.cur.fetchall():
            query = """CREATE TABLE `%s` (
                                    `k` TEXT,
                                    `v` TEXT,
                                    PRIMARY KEY(k)
                                );""" % self.tablename
            self.cur.execute(query)
            self.con.commit()
            print ('created table')
        if serialisationtype == 'json':
            self.tostring = self._jsontostring
            self.fromstring = self._jsonfromstring
        elif serialisationtype == 'pickle':
            self.tostring = self._pickletostring
            self.fromstring = self._picklefromstring

    def _pickletostring(self,value):
        f = StringIO()
        p = Pickler(f, 0)
        p.dump(value)
        return f.getvalue()

    def _picklefromstring(self,value):
        f = StringIO(value)
        return Unpickler(f).load()

    def _jsontostring(self,value):
        return json.dumps(value)

    def _jsonfromstring(self,value):
        return json.loads(value)

    def keys(self):
        query = "SELECT k FROM %s" % self.tablename
        self.cur.execute(query)
        return [item[0] for item in self.cur.fetchall()]

    def values(self):
        query = "SELECT v FROM %s" % self.tablename
        self.cur.execute(query)
        return [self.fromstring(item[0]) for item in self.cur.fetchall()]

    def items(self):
        query = "SELECT k, v FROM %s" % self.tablename
        self.cur.execute(query)
        return [(item[0],self.fromstring(item[1])) for item in self.cur.fetchall()]

    def __len__(self):
        query = "SELECT Count(*) FROM %s" % self.tablename
        self.cur.execute(query)
        return self.cur.fetchone()[0]

    def has_key(self, key):
        query = "SELECT k FROM %s WHERE k = ?" % self.tablename
        self.cur.execute(query, (key,))
        return bool(self.cur.fetchone())

    def __getitem__(self, key):
        query = "SELECT v FROM %s WHERE k = ?" % self.tablename
        self.cur.execute(query,(key,))
        result = self.cur.fetchone()
        if result:
            return self.fromstring(result[0])
        else:
            raise KeyError

    def __setitem__(self, key, value):
        query = "INSERT OR REPLACE INTO %s (k, v) VALUES (?, ?);" % self.tablename
        self.cur.execute(query,(key, self.tostring(value)))
        self.con.commit()

    def __delitem__(self, key):
        if not self.has_key(key):
            raise KeyError
        else:
            query = "DELETE FROM %s WHERE k = ?" % self.tablename
            self.cur.execute(query,(key,))
            self.con.commit()

    def close(self):
        self.con.close()

    def __del__(self):
        self.con.close()

    def clear(self):
        query = "DELETE FROM %s" % self.tablename
        self.cur.execute(query)

    def copy(self):
        return dict(self.items())

    def iter(self):
        return self.iterkeys()

    def __iter__(self):
        return self.iterkeys()

    def iteritems(self):
        def resultfunction(result):
            return (result[0], self.fromstring(result[1]))
        return databaseiterator(self.filenameandpath, self.tablename, self.serialisationtype, "SELECT k, v FROM %s LIMIT 1 OFFSET " % self.tablename, resultfunction)

    def iterkeys(self):
        def resultfunction(result):
            return result[0]
        return databaseiterator(self.filenameandpath, self.tablename, self.serialisationtype, "SELECT k FROM %s LIMIT 1 OFFSET " % self.tablename, resultfunction)

    def itervalues(self):
        def resultfunction(result):
            return self.fromstring(result[0])
        return databaseiterator(self.filenameandpath, self.tablename, self.serialisationtype, "SELECT v FROM %s LIMIT 1 OFFSET " % self.tablename, resultfunction)


class databaseiterator:
    def __init__(self, filenameandpath, tablename, serialisationtype, query, resultfunction):
        """query should be in the form "SELECT <your code here> LIMIT 1 OFFSET "
        """
        self.con = sqlite3.connect(filenameandpath)
        self.cur = self.con.cursor()
        self.tablename = tablename
        self.query = query
        self.offset = 0
        self.resultfunction = resultfunction

    def __iter__(self):
        return self

    def next(self):
        query = self.query + str(self.offset) + ';'
        self.cur.execute(query)
        result = self.cur.fetchone()
        if result is None:
            raise StopIteration
        else:
            self.offset += 1
            return self.resultfunction(result)


def test1(database):
    """Testing: keys, values, clear, __setitem__, __getitem__"""
    database.clear()
    assert len(database.keys()) == 0
    assert len(database.values()) == 0
    assert len(database.items()) == 0
    database['hello'] = 'world'
    assert database['hello'] == 'world'
    assert len(database.keys()) == 1
    assert len(database.values()) == 1
    assert len(database.items()) == 1
    assert database.keys() == ['hello']
    assert database.values() == ['world']
    assert database.items() == [('hello','world')]
    assert len(database) == 1
    database.clear()
    assert len(database) == 0

def main():
    filename = 'testconfigdatabase.sqlite'

    kvdatabase = sqlite3keyvaluestore(filename, tablename='ApplicationConfiguration', serialisationtype='json')

    test1(kvdatabase)

if __name__ == '__main__':
    main()
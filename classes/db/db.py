from django.db import connection

class DB():

    def connect(self):
        cursor = connection.cursor()
        return cursor

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def Query(self,sql='None'):
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = self.dictfetchall(cursor)
        return rows

    def RowCount(self,sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = self.dictfetchall(cursor)
        cc = rows.count()
        return cc

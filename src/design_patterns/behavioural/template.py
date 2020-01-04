"""
Main class with template method providing some steps to be executed:
    def template_method():
        step1()
        step2()
        pre_step3_hook()
        step3()
        post_step_3_hook()

Subclasses can alter some of these steps.
The hook methods can be used before/after crucial
steps to give subclasses extra extension points
"""


class UsersImport:
    
    def run(self):
        data = self.read_data()
        data = self.transform_data(data)
        self.write_data(data)
    
    def read_data(self):
        raise NotImplementedError()
    
    def transform_data(self, data):
        raise NotImplementedError()
    
    def write_data(self, data):
        print('writing data to file, data = %s' % data)


class UsersImportFromPostgreSQL(UsersImport):
    
    def read_data(self):
        print('reading data from PostgreSQL')
        return [
            ('Harry Potter', 18),
            ('Hulk', 30)
        ]
    
    def transform_data(self, data):
        print('transforming PostgreSQL data')
        return {t[0]: t[1] for t in data}

    
class UsersImportFromMongo(UsersImport):
    
    def read_data(self):
        print('reading data from Mongo')
        return [
            {'name': 'Batman', 'age': 35},
            {'name': 'Rocky', 'age': 26}
        ]
    
    def transform_data(self, data):
        print('transforming Mongo data')
        return {t['name']: t['age'] for t in data}

            
def run():
    UsersImportFromPostgreSQL().run()
    UsersImportFromMongo().run()

    
if __name__ == '__main__':
    run()

import logging, requests
import urllib.parse as par

logging.basicConfig(level=logging.INFO)

class Endpoints():

    def __init__(self) -> None:
        self.client = QuestClient()

    def get_all(self):
        sql = "select pop_id, name, color from pop"
        return self.client.return_results(sql)
    
    def get_by_name(self, pop_name):
        try:
            sql = f"select pop_id, name, color from pop where name = '{pop_name}'"
            return self.client.return_results(sql)
        except:
            return self.get_all()
    
    def get_by_color(self, pop_color):
        try:
            sql = f"SELECT pop_id, name, color FROM pop WHERE color = '{pop_color}'"
            return self.client.return_results(sql)
        except:
            return self.get_all()
        
    def insert(self, pop_name, pop_color):
        try:
            records = [
                { "name": pop_name,"color": pop_color,"id": 99}
            ]
            self.client.insert_record(records)
        except:
            logging.warning("insert failed: name => " + pop_name + ", color => " + pop_color)
            pass
        return self.get_all()


class QuestClient():

    SERVICE_URL = "http://db:9000/exec?query="
    
    def __new__(cls):
        """use singleton design pattern for a single instance"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(QuestClient, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        query = "select * from pop"
        r = requests.get(self.SERVICE_URL + query)
        if r.status_code == 400:
            records = [
    {
      "color": "brown",
      "id": 1,
      "name": "RC Cola"
    },
    {
      "color": "clear",
      "id": 2,
      "name": "Sprite"
    },
    {
      "color": "brown",
      "id": 3,
      "name": "Verners"
    },
    {
      "color": "green",
      "id": 4,
      "name": "Mt. Lightening"
    }
            ]
            self.create_table()
            self.insert_record(records)

    def create_table(self):
        query = 'create table pop'\
            '(pop_id int,'\
            'name String,'\
            'color String,'\
            'timestamp timestamp)'\
            'timestamp(timestamp)'
        r = requests.get(self.SERVICE_URL + query)
        logging.info(r.status_code)

    def insert_record(self, records):
        
        for record in records:
            id = record['id']
            name = record['name']
            color = record['color']

            query = "insert into pop (pop_id, name, color, timestamp) values("\
                + str(id) + ",'"\
                + str(name) + "','" \
                + str(color) +"',systimestamp())"
            r = requests.get(self.SERVICE_URL + query)
        
    def return_results(self, sql):
        try:
            query = par.quote(sql)
            r = requests.get(self.SERVICE_URL + query)
            x = r.json()
            results = [
            {
                "id": o[0],
                "name": o[1],
                "color": o[2]
            } for o in x['dataset']]
            return {'data': results, 'count': x['count']}
        except:
            return sql


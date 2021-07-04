from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, parallel_bulk
from dataloader import SRT
import config
import json
data = SRT("data/S04E01.srt",series="Community",season=4,episode=1)

elastic_client = Elasticsearch(config.ELASTIC_SERVER_URL)
# elastic_client.indices.create(index=config.ELASTIC_INDEX, include_type_name = True)

mapping = elastic_client.indices.get_mapping(index = config.ELASTIC_INDEX)
print(mapping)


js = []
for obj in data.parsed_data:
    action = {
                "index": {
                        "_index": config.ELASTIC_INDEX,
                    }
            }
    js.append(action)
    js.append(obj.__dict__)


print(js)
push = elastic_client.bulk(body = js,index = config.ELASTIC_INDEX)
count = elastic_client.search(index = config.ELASTIC_INDEX)
print(push,count)
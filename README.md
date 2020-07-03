

```bash
# prepare project

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

```

```bash
# run project scrapy

cat websites.txt | python import_list.py
```

```bash
# run project with Docker

#build image
docker build --tag rgr_scrapy . 

cat websites.txt | docker run -i rgr_scrapy

# with volume
cat websites.txt | docker run -v $(pwd)/output.json:/code/result.json -i rgr_scrapy

```

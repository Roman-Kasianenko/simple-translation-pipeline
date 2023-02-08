# :earth_americas: simple-translation-pipeline :earth_americas:

This is simple scrapy pipeline which can we used to translate all fields in scrapy item tou your language.

##### NOTE: currently it is working only with google translate.

## How to install :snake:
```
git clone https://github.com/Roman-Kasianenko/simple-translation-pipeline.git
cd simple-translation-pipeline
python setup.py install
```

## :hammer_and_wrench:Settings:hammer_and_wrench:

❗Fist of all please make sure you setup delay as 1 sec or more. otherwise we can have issues (429 error)

To start using this pipeline we need to add in in scrapy settings file:
```python
ITEM_PIPELINES = {
    'simple_translation_pipeline.pipeline.SimpleTranslatePipeline': 100
}

```

By default it will detect input language automatically, and result language will be `English` 
you can setup input and output language using following settings:

##### To setup input language need ot use:
```python
FROM_LANGUAGE = 'de'
```
##### To setup output language need ot use:
```python
TO_LANGUAGE = 'uk'
```
##### List of fields to translate
```python
# is empty by default, so none of field will be translated
FIELDS_TO_TRANSLATE = ['title', 'description']
```

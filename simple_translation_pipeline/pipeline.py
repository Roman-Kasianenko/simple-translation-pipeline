import translators as ts


class SimpleTranslatePipeline:

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings)

    def __init__(self, settings):
        self.translated_map = {}
        self.field_to_translate = settings.get('FIELDS_TO_TRANSLATE', [])

    def process_item(self, item, spider):
        field_to_translate = self.field_to_translate

        if hasattr(spider, 'field_to_translate'):
            field_to_translate = spider.field_to_translate

        for k, v in item.items():
            if k in field_to_translate and v:
                try:
                    if v in self.translated_map:
                        item[k] = self.translated_map[v]
                    else:
                        translated_value = ts.google(v, if_use_cn_host=False)
                        item[k] = translated_value
                        self.translated_map[v] = translated_value
                except Exception as e:
                    spider.logger.warning(f"Can't translate filed {k} - {v}")
                    item[k] = v
        return item

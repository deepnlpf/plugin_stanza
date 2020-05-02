#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.core.iplugin import IPlugin

class Plugin(IPlugin):
    
    def __init__(self, id_pool, lang, document, pipeline):
        self._id_pool = id_pool
        self._lang = lang
        self._document = document
        self._pipeline = pipeline

    def run(self):
        annotation = self.wrapper()
        annotation = self.out_format(annotation)
        return annotation

    def wrapper(self):
        import stanza, json

        nlp = stanza.Pipeline(lang=self._lang, processors=", ".join(self._pipeline), use_gpu=False)
        doc = nlp(", ".join(self._document['sentences']))
        
        return json.loads(str(doc))

    def out_format(self, annotation):
        from deepnlpf.core.output_format import OutputFormat

        try:
            return OutputFormat().doc_annotation(
                _id_pool=self._id_pool, _id_dataset=self._document['_id_dataset'],
                _id_document=self._document['_id'], tool="stanza", annotation=annotation
                )
        except Exception as err:
            return annotation

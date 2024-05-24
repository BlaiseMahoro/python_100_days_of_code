import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):
    # { ents: [{...}]}
    # html : "<span>..."}
    
    def test_get_ents_returns_dictionary_given_empty_string_causes_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
        
        
    def  test_get_ents_returns_dictionary_given_nonempty_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        ner = NamedEntityClient(model)
        model.returns_doc_ents([])
        ents = ner.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)
        
        
    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_results = {'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html':''}
        self.assertListEqual(result['ents'], expected_results['ents'])
        
        
    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_GROUP(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Lithuania', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_results = {'ents': [{'ent': 'Lithuania', 'label': 'Group'}], 'html':''}
        self.assertListEqual(result['ents'], expected_results['ents'])
        
    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_results = {'ents': [{'ent': 'Australia', 'label': 'Location'}], 'html':''}
        self.assertListEqual(result['ents'], expected_results['ents'])
        
    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}, {'text': 'Judith Polgar', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_results = {'ents': [{'ent': 'Australia', 'label': 'Location'}, {'ent': 'Judith Polgar', 'label': 'Person'}], 'html':''}
        self.assertListEqual(result['ents'], expected_results['ents'])
        
    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_results = {'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html':''}
        self.assertListEqual(result['ents'], expected_results['ents'])
        
        
    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_results = {'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html':''}
        self.assertListEqual(result['ents'], expected_results['ents'])
        
    
        
if __name__ == "__main__":
    unittest.main()


class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """
    
    def __init__(self, model) -> None:
        self.model = model
        
    def returns_doc_ents(self, ents):
        self.ents = ents
        
    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)
    
    
    
class DocTestDouble:
    """
    Test double for spaCy Doc
    """
    
    def __init__(self, sent, ents) -> None:
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]
        
    def patch_method(self, attr, return_value):
        def patched(): return return_value
        set(self, attr, patched)
        return self
        
        
class SpanTestDouble:
    """
    Test double for spaCy span
    """
    
    def __init__(self, text, label) -> None:
        self.text = text
        self.label_ = label
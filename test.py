from dotenv import load_dotenv
import os


RESPONSE_JSON = {
    "1": {
        "no": "1",
        "mcq": "multiple choice questions",
        "options":{
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        
        "correct": "correct answer"
    },
    
    "2": {
        "no": "2",
        "mcq": "multiple choice questions",
        "options":{
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        
        "correct": "correct answer"
    },
    
    "3": {
        "no": "3",
        "mcq": "multiple choice questions",
        "options":{
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        
        "correct": "correct answer"
    }
    
    
}
"response_json": json.dumps(RESPONSE_JSON)
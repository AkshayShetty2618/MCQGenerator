import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
            return text
        except Exception as e:
            raise Exception("error in reding odf file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported format")
    

def get_table_data(quiz_str):
    try:
        quizDict = json.loads(quiz_str)
        quiztable = []


        for key ,value in quizDict.items():
            mcq = value["mcq"]
            options = "||". join(
                [
                    f"(option)-> (option_value)" for option, option_value in value["options"].items()
                ]
            )

            correctval = value["correct"]
            quiztable.append({"MCQ":mcq, "Choices":options, "Correct":correctval})
        return quiztable
    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False
from pyresparser import ResumeParser
data = ResumeParser('./resume1.pdf').get_extracted_data()
print(data)
print(type(data))

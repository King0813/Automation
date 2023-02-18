import pyttsx3, PyPDF2

pdf1 = PyPDF2.PdfReader(open('Business Plan - V1.pdf','rb'))
#pdfdoc = PyPDF2.PdfReader(pdf1)
speaker = pyttsx3.init()

for page_num in range(pdf1.numPages):
    text = pdf1.getPage(page_num).extractText()
    
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
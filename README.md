# Key Terms Extractor


Algorithm created to  analys a pdf text and recognize the main terms discussed within the text, helping the user to get an idea of the main points addressed.
> I'm still working in this project and it need to have its accuracy
> improved

### Libs used:

 - PyTextRank (textRank implementation)
 - Spacy
 - PDFMiner
 - Pandas

### How to install all dependencies:

 1. Run **pip install** to install all dependencies into requeriments.txt
 2. Run **python spacy download en_core_web_sm** to install spacy dependency

 
### How to test the algoritm:

The algorithm checks all pdv files inside the **src/articles** directory, extracts the text into a text file with the same name and stores it in the **src/text-extraction** directory and finally analyzes and saves the result in a CSV file within the **src/results** directory.
If these directories do not exist, you must create them

## Future goals and improvements

 - Improve the accuracy of the algorithm
 - Transform the project into a web application
 - Add new related features

 

#### Author: André Luiz Ximenes G. da Luz
